#!/usr/bin/env python3
"""Index every template workflow JSON into references/templates-catalog.md.
Parses each JSON (no LLM): trigger, node types used, node count, connection count.
Usage: python3 index-templates.py [TEMPLATES_DIR] [OUT_MD]
"""
import os, sys, json, glob

SRC = sys.argv[1] if len(sys.argv) > 1 else "/Users/tew/Desktop/intern/n8n_templates"
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser(
    "~/.claude/skills/n8n/references/templates-catalog.md")

files = sorted(glob.glob(f"{SRC}/**/*.json", recursive=True))
rows = []
for f in files:
    try:
        w = json.load(open(f, encoding="utf-8", errors="ignore"))
    except Exception:
        continue
    if not isinstance(w, dict):
        continue
    nodes = w.get("nodes")
    if not isinstance(nodes, list):
        continue  # not a workflow (e.g. _chapters.json)
    types = [n.get("type", "?") for n in nodes]
    trig = sorted({t for t in types if "trigger" in t.lower() or t.endswith("manualTrigger")})
    uniq = sorted(set(types))
    rows.append({
        "name": os.path.basename(f),
        "dir": os.path.relpath(os.path.dirname(f), SRC),
        "nodes": len(nodes),
        "conns": len(w.get("connections", {})),
        "trigger": ", ".join(t.split(".")[-1] for t in trig) or "—",
        "types": ", ".join(sorted(set(t.split(".")[-1] for t in uniq))),
    })

md = ["# Template Catalog (all source workflows analyzed)", "",
      f"> Auto-parsed from `{SRC}` ({len(rows)} workflow JSONs). Shows trigger + every node type each uses. "
      "Bundled & cleaned subset lives in `templates/` (see templates/README.md). Regenerate: `python3 scripts/index-templates.py`.",
      "", "| Template | nodes | conns | trigger | node types used |",
      "|---|---|---|---|---|"]
for r in sorted(rows, key=lambda r: r["name"].lower()):
    md.append(f"| `{r['name']}` | {r['nodes']} | {r['conns']} | {r['trigger']} | {r['types']} |")
md.append("")
open(OUT, "w", encoding="utf-8").write("\n".join(md))
print(f"WROTE {OUT}  ({len(rows)} workflows indexed)")
