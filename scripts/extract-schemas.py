#!/usr/bin/env python3
"""Extract per-node schemas from n8n source into references/nodes/<type>.md + an index.

Brace-matching parser over each node directory's *.ts files. Best-effort (TS not
fully parsed): captures typeVersion, resources/operations, and property fields
(name, displayName, type, default, required, gated-by). Confirm edge cases via
n8n-mcp get_node. Re-runnable.

Usage: python3 extract-schemas.py [N8N_SRC] [OUT_DIR]
"""
import os, re, sys, glob, json

SRC = sys.argv[1] if len(sys.argv) > 1 else "/Users/tew/Desktop/intern/n8n"
OUTDIR = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser("~/.claude/skills/n8n/references")
NODES_OUT = os.path.join(OUTDIR, "nodes")
os.makedirs(NODES_OUT, exist_ok=True)

def read(p):
    try: return open(p, encoding="utf-8", errors="ignore").read()
    except Exception: return ""

def first(pat, text, flags=0, d=None):
    m = re.search(pat, text, flags); return m.group(1).strip() if m else d

def match_block(text, open_idx, opener="[", closer="]"):
    """Return substring from opener at open_idx to its matching close."""
    depth, i, n = 0, open_idx, len(text)
    instr = None
    while i < n:
        c = text[i]
        if instr:
            if c == instr and text[i-1] != "\\": instr = None
        elif c in "'\"`": instr = c
        elif c == opener: depth += 1
        elif c == closer:
            depth -= 1
            if depth == 0: return text[open_idx:i+1]
        i += 1
    return text[open_idx:]

def split_top_objects(arr_text):
    """Given '[ {..}, {..} ]', yield each top-level {..} string."""
    objs, depth, start, instr = [], 0, None, None
    for i, c in enumerate(arr_text):
        if instr:
            if c == instr and arr_text[i-1] != "\\": instr = None
            continue
        if c in "'\"`": instr = c; continue
        if c == "{":
            if depth == 0: start = i
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0 and start is not None:
                objs.append(arr_text[start:i+1]); start = None
    return objs

def scalar(obj, key):
    return first(rf"\b{key}:\s*'([^']*)'", obj) or first(rf'\b{key}:\s*"([^"]*)"', obj) \
        or first(rf"\b{key}:\s*(true|false|\[\]|\{{\}}|[0-9.]+)", obj)

def extract_props(text):
    """Find every `properties: [ ... ]` and parse top-level property objects."""
    props = []
    for m in re.finditer(r"properties:\s*\[", text):
        arr = match_block(text, m.end()-1, "[", "]")
        for obj in split_top_objects(arr):
            name = scalar(obj, "name"); disp = scalar(obj, "displayName")
            if not name: continue
            typ = scalar(obj, "type") or ""
            dflt = scalar(obj, "default")
            req = "true" if re.search(r"required:\s*true", obj) else ""
            # gated-by resource/operation via displayOptions.show
            gate = ""
            dop = first(r"displayOptions:\s*(\{)", obj)
            if dop is not None:
                blk = match_block(obj, obj.index("displayOptions:")+len("displayOptions:"), "{", "}")
                res = re.findall(r"resource:\s*\[([^\]]*)\]", blk)
                op = re.findall(r"operation:\s*\[([^\]]*)\]", blk)
                tags = []
                for r in res: tags += [f"res={v}" for v in re.findall(r"'([^']+)'", r)]
                for o in op: tags += [f"op={v}" for v in re.findall(r"'([^']+)'", o)]
                gate = ",".join(tags[:6])
            props.append({"name": name, "disp": disp or name, "type": typ,
                          "default": dflt, "req": req, "gate": gate})
    # dedupe by (name, gate)
    seen, out = set(), []
    for p in props:
        k = (p["name"], p["gate"])
        if k in seen: continue
        seen.add(k); out.append(p)
    return out

def extract_ops(text):
    """resources + operations from option blocks for name:'resource'/'operation'."""
    res, ops = [], []
    for m in re.finditer(r"name:\s*'(resource|operation)'", text):
        kind = m.group(1)
        opt = re.search(r"options:\s*\[", text[m.start():m.start()+8000])
        if not opt: continue
        arr = match_block(text, m.start()+opt.start(), "[", "]")
        vals = re.findall(r"value:\s*'([^']+)'", arr)
        (res if kind == "resource" else ops).extend(vals)
    return sorted(set(res)), sorted(set(ops))

def versions(text):
    vs = set()
    for m in re.finditer(r"\bversion:\s*(\[[^\]]*\]|[0-9.]+)", text):
        raw = m.group(1)
        for n in re.findall(r"[0-9.]+", raw):
            try: vs.add(float(n))
            except: pass
    dv = first(r"defaultVersion:\s*([0-9.]+)", text)
    if dv:
        try: vs.add(float(dv))
        except: pass
    for k in re.findall(r"(\d+(?:\.\d+)?):\s*new\s+\w+Node", text):
        try: vs.add(float(k))
        except: pass
    if not vs: return "1"
    mx = max(vs); return str(int(mx)) if mx == int(mx) else str(mx)

def prefix(path):
    return "@n8n/n8n-nodes-langchain" if "nodes-langchain" in path else "n8n-nodes-base"

# group .node.ts by directory; merge all .ts in that dir for props
entry_files = []
for pat in [f"{SRC}/packages/nodes-base/nodes/**/*.node.ts",
            f"{SRC}/packages/@n8n/nodes-langchain/nodes/**/*.node.ts"]:
    entry_files += glob.glob(pat, recursive=True)
entry_files = sorted(set(f for f in entry_files if "/__tests__/" not in f and ".test." not in f))

nodes = {}  # type -> data
for ef in entry_files:
    txt = read(ef)
    # identity must come from the node's (base)description object, not a stray property
    dm = re.search(r"(?:baseDescription|description)\s*(?::[^=\n]*)?=\s*\{", txt)
    if not dm: continue
    descblk = match_block(txt, dm.end()-1, "{", "}")
    name = first(r"name:\s*'([a-zA-Z][a-zA-Z0-9]*)'", descblk)
    disp = first(r"displayName:\s*'([^']+)'", descblk)
    if not name or not disp: continue
    ntype = f"{prefix(ef)}.{name}"
    nodedir = os.path.dirname(ef)
    if ntype in nodes: continue
    # gather all .ts under the node dir for properties/ops/versions
    dirtexts = txt
    for tf in glob.glob(f"{nodedir}/**/*.ts", recursive=True):
        if tf != ef and ".test." not in tf and "/__tests__/" not in tf:
            dirtexts += "\n" + read(tf)
    res, ops = extract_ops(dirtexts)
    props = extract_props(dirtexts)
    creds = sorted(set(re.findall(r"name:\s*'([a-zA-Z0-9]+(?:Api|OAuth2Api|Credentials?))'", dirtexts)))
    grp = first(r"group:\s*\[([^\]]*)\]", txt) or ""
    grp = ",".join(re.findall(r"'([^']+)'", grp))
    nodes[ntype] = {"type": ntype, "disp": disp, "group": grp or "-",
                    "ver": versions(dirtexts), "res": res, "ops": ops,
                    "props": props, "creds": creds, "trigger": bool(re.search("trigger", name, re.I))}

# clean phantoms: drop property-titled mis-parses; case-insensitive dedupe keeping richest
BAD_TITLES = {"authentication","resource","operation","additional fields","options",
              "credentials","fields","additional options","simplify"}
cleaned = {}
for nt, d in nodes.items():
    if d["disp"].strip().lower() in BAD_TITLES:
        continue
    key = nt.lower()
    score = len(d["ops"]) + len(d["props"])
    cur = cleaned.get(key)
    if cur is None or score > cur[1]:
        cleaned[key] = (nt, score, d)
nodes = {v[0]: v[2] for v in cleaned.values()}

# write per-node md
def safe(t): return t.replace("/", "__")
for nt, d in nodes.items():
    lines = [f"# {d['disp']}  (`{d['type']}`)", "",
             f"- typeVersion (max): **{d['ver']}**  | group: {d['group']}  | trigger: {'yes' if d['trigger'] else 'no'}",
             f"- credentials: {', '.join(d['creds']) or '—'}"]
    if d["res"]: lines.append(f"- resources: {', '.join(d['res'])}")
    if d["ops"]: lines.append(f"- operations: {', '.join(d['ops'])}")
    lines += ["", "## Parameters", "",
              "| name | displayName | type | default | req | gated by |",
              "|---|---|---|---|---|---|"]
    for p in d["props"]:
        lines.append(f"| `{p['name']}` | {p['disp']} | {p['type']} | {p['default'] if p['default'] is not None else ''} | {p['req']} | {p['gate']} |")
    if not d["props"]:
        lines.append("| _(properties not statically extractable — confirm via n8n-mcp get_node)_ |||||| ")
    lines.append("")
    open(os.path.join(NODES_OUT, safe(nt)+".md"), "w", encoding="utf-8").write("\n".join(lines))

# rebuild catalog index
rows = sorted(nodes.values(), key=lambda d: d["disp"].lower())
base = [r for r in rows if "langchain" not in r["type"]]
lc = [r for r in rows if "langchain" in r["type"]]
def idx(rs):
    out = ["| Node | type | maxVer | trig | #ops | #params | schema |", "|---|---|---|---|---|---|---|"]
    for r in rs:
        out.append(f"| {r['disp']} | `{r['type']}` | {r['ver']} | {'✓' if r['trigger'] else ''} | {len(r['ops'])} | {len(r['props'])} | [schema](nodes/{r['type'].replace('/','__')}.md) |")
    return "\n".join(out)
md = ["# n8n Built-in Node Catalog (full per-node schemas)", "",
      f"> Source-extracted from n8n v2.26.0 ({len(rows)} nodes: {len(base)} core + {len(lc)} AI/LangChain). "
      "Each row links to a per-node schema in `nodes/` (resources, operations, full parameter list). "
      "Regenerate: `python3 scripts/extract-schemas.py`. Best-effort TS parse — for nested/imported props or exact "
      "typeVersion edge cases, confirm via n8n-mcp `get_node`. Prefer the dedicated node over `httpRequest` (node-selection.md).",
      "", "## Core nodes (`n8n-nodes-base.*`)", "", idx(base),
      "", "## AI / LangChain nodes (`@n8n/n8n-nodes-langchain.*`)", "", idx(lc), ""]
open(os.path.join(OUTDIR, "node-catalog.md"), "w", encoding="utf-8").write("\n".join(md))

tot_props = sum(len(d["props"]) for d in nodes.values())
tot_ops = sum(len(d["ops"]) for d in nodes.values())
print(f"nodes={len(nodes)} core={len(base)} lc={len(lc)} total_params={tot_props} total_ops={tot_ops}")
print(f"per-node files in {NODES_OUT}")
for nd in ["n8n-nodes-base.slack","n8n-nodes-base.facebookGraphApi","n8n-nodes-base.whatsApp","n8n-nodes-base.googleSheets"]:
    d = nodes.get(nd); print(f"  {nd}: ver={d['ver']} ops={len(d['ops'])} params={len(d['props'])}" if d else f"  {nd}: MISSING")
