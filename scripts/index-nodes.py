#!/usr/bin/env python3
"""Index every built-in n8n node from source into references/node-catalog.md.

Best-effort regex extraction (no TS parse): displayName, node type name, group,
max typeVersion, declared credentials. Re-runnable: point N8N_SRC at the n8n repo.

Usage: python3 index-nodes.py [N8N_SRC] [OUT_MD]
"""
import os, re, sys, glob, json

SRC = sys.argv[1] if len(sys.argv) > 1 else "/Users/tew/Desktop/intern/n8n"
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser(
    "~/.claude/skills/n8n/references/node-catalog.md")

def grab(pat, text, flags=0):
    m = re.search(pat, text, flags)
    return m.group(1).strip() if m else None

def pkg_prefix(path):
    if "nodes-langchain" in path:
        return "@n8n/n8n-nodes-langchain"
    return "n8n-nodes-base"

def parse_versions(text):
    # version: 4.2  | version: [1, 2, 3]  | defaultVersion: 3
    vers = set()
    for m in re.finditer(r"\bversion:\s*(\[[^\]]*\]|[0-9.]+)", text):
        raw = m.group(1)
        if raw.startswith("["):
            for n in re.findall(r"[0-9.]+", raw):
                vers.add(float(n))
        else:
            try: vers.add(float(raw))
            except ValueError: pass
    if not vers:
        return "1"
    mx = max(vers)
    return str(int(mx)) if mx == int(mx) else str(mx)

def parse_creds(text):
    # credentials: [ { name: 'xxx', ... } ]
    block = grab(r"credentials:\s*(\[[\s\S]*?\])", text)
    if not block:
        return ""
    return ",".join(sorted(set(re.findall(r"name:\s*['\"]([^'\"]+)['\"]", block))))

def parse_ops(text):
    # operation option values, best-effort
    ops = set(re.findall(r"value:\s*['\"]([a-zA-Z][a-zA-Z0-9_]*)['\"]", text))
    # keep it short
    return ""  # operations are noisy via regex; omit, keep catalog clean

rows = []
seen = set()
patterns = [
    os.path.join(SRC, "packages/nodes-base/nodes/**/*.node.ts"),
    os.path.join(SRC, "packages/@n8n/nodes-langchain/nodes/**/*.node.ts"),
    os.path.join(SRC, "packages/**/nodes-langchain/**/*.node.ts"),
]
files = []
for p in patterns:
    files.extend(glob.glob(p, recursive=True))
files = sorted(set(files))

for f in files:
    if ".node.ts" not in f or "/__tests__/" in f or ".test." in f:
        continue
    try:
        text = open(f, encoding="utf-8", errors="ignore").read()
    except Exception:
        continue
    # skip versioned-node wrapper bases without a description
    name = grab(r"name:\s*['\"]([a-zA-Z][a-zA-Z0-9]*)['\"]", text)
    disp = grab(r"displayName:\s*['\"]([^'\"]+)['\"]", text)
    if not name or not disp:
        continue
    ntype = f"{pkg_prefix(f)}.{name}"
    if ntype in seen:
        continue
    seen.add(ntype)
    group = grab(r"group:\s*\[([^\]]*)\]", text) or ""
    group = ",".join(re.findall(r"['\"]([^'\"]+)['\"]", group))
    ver = parse_versions(text)
    creds = parse_creds(text)
    is_trigger = "trigger" in name.lower() or "Trigger" in disp or "trigger" in group
    rows.append({
        "disp": disp, "type": ntype, "ver": ver, "group": group or "-",
        "creds": creds or "-", "trigger": "✓" if is_trigger else "",
    })

rows.sort(key=lambda r: r["disp"].lower())

langchain = [r for r in rows if "langchain" in r["type"]]
base = [r for r in rows if "langchain" not in r["type"]]

def table(rs):
    out = ["| Node | type | maxVer | group | trigger | credentials |",
           "|---|---|---|---|---|---|"]
    for r in rs:
        out.append(f"| {r['disp']} | `{r['type']}` | {r['ver']} | {r['group']} | {r['trigger']} | {r['creds']} |")
    return "\n".join(out)

md = []
md.append("# n8n Built-in Node Catalog")
md.append("")
md.append(f"> Auto-indexed from n8n source ({len(rows)} nodes: {len(base)} core + {len(langchain)} LangChain/AI). "
          "Regenerate: `python3 scripts/index-nodes.py`. `maxVer` = highest typeVersion found; "
          "pin it in workflow JSON. WARNING: the regex under-reports versioned nodes (Set/If/Switch/Merge may show 1 but are higher "
          "e.g. Set 3.4, If 2.2) — confirm typeVersion via n8n-mcp get_node before pinning. "
          "Use the dedicated node below before reaching for `httpRequest` — see node-selection.md.")
md.append("")
md.append("## Core nodes (`n8n-nodes-base.*`)")
md.append("")
md.append(table(base))
md.append("")
md.append("## AI / LangChain nodes (`@n8n/n8n-nodes-langchain.*`)")
md.append("")
md.append(table(langchain))
md.append("")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write("\n".join(md))
print(f"WROTE {OUT}")
print(f"nodes={len(rows)} core={len(base)} langchain={len(langchain)} files_scanned={len(files)}")
# sanity spot-checks
for needle in ["whatsApp", "facebookGraphApi", "gmail", "slack", "httpRequest", "Agent"]:
    hit = [r['type'] for r in rows if needle.lower() in r['type'].lower()]
    print(f"  {needle}: {hit[:3]}")
