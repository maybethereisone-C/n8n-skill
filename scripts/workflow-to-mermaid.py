#!/usr/bin/env python3
# Adapted from Zie619/n8n-workflows (MIT). Rewritten stdlib-only for the n8n skill.
"""Render an n8n workflow JSON as a Mermaid `graph TD` diagram (stdout).

Nodes become labelled boxes; edges come from the `connections` map. Trigger
nodes get a rounded shape so the entry point is obvious.

Usage: python3 workflow-to-mermaid.py <workflow.json>
"""
import json
import re
import sys


def is_trigger(node_type):
    t = str(node_type or "").lower()
    return "trigger" in t or t.endswith("manualtrigger")


def node_id(name, table):
    """Stable, mermaid-safe id for a node name."""
    if name in table:
        return table[name]
    safe = re.sub(r"[^A-Za-z0-9]", "_", name) or "n"
    nid = f"n{len(table)}_{safe}"[:60]
    table[name] = nid
    return nid


def esc(label):
    """Escape a label for use inside a mermaid node bracket."""
    return str(label).replace('"', "'").replace("\n", " ").strip() or "?"


def main(argv):
    if len(argv) < 2:
        print("usage: python3 workflow-to-mermaid.py <workflow.json>", file=sys.stderr)
        return 2

    try:
        with open(argv[1], encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        print(f"error: cannot load workflow: {e}", file=sys.stderr)
        return 1

    if not isinstance(data, dict):
        print("error: top-level JSON is not an object", file=sys.stderr)
        return 1

    nodes = data.get("nodes") or []
    connections = data.get("connections") or {}

    type_by_name = {}
    ids = {}
    lines = ["graph TD"]

    for node in nodes:
        if not isinstance(node, dict):
            continue
        name = node.get("name")
        if not name:
            continue
        ntype = node.get("type", "")
        type_by_name[name] = ntype
        nid = node_id(name, ids)
        label = esc(name)
        if is_trigger(ntype):
            lines.append(f'    {nid}(["{label}"])')  # rounded = trigger
        else:
            lines.append(f'    {nid}["{label}"]')

    for src, outputs in connections.items():
        if not isinstance(outputs, dict):
            continue
        src_id = node_id(src, ids)
        for _output_name, branches in outputs.items():
            if not isinstance(branches, list):
                continue
            for branch in branches:
                if not isinstance(branch, list):
                    continue
                for conn in branch:
                    if isinstance(conn, dict) and conn.get("node"):
                        lines.append(f"    {src_id} --> {node_id(conn['node'], ids)}")

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
