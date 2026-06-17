#!/usr/bin/env python3
# Adapted from Zie619/n8n-workflows (MIT). Rewritten stdlib-only for the n8n skill.
"""Validate n8n workflow JSON files for import-readiness.

Checks per workflow (FAIL = blocks import / WARN = best-practice):
  - valid JSON; has `nodes` (array) and `connections` (object)
  - top-level `id` present (WARN if missing — `n8n import:workflow` fails without it)
  - every node has name, type, typeVersion, position (length-2 array)
  - node names are unique
  - every connections key references an existing node name; every target
    {node} in connection arrays references an existing node name
  - at least one trigger node (type contains 'trigger' or == manualTrigger) (WARN)

Usage: python3 validate-workflow.py <workflow.json> [more.json ...]
Exit 0 if every file passes (warnings allowed), 1 if any file FAILs.
"""
import json
import os
import sys


def is_trigger(node_type):
    t = str(node_type or "").lower()
    return "trigger" in t or t.endswith("manualtrigger")


def validate(path):
    """Return (fails, warns) lists of message strings for one workflow file."""
    fails, warns = [], []

    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        return (["file not found"], [])
    except json.JSONDecodeError as e:
        return ([f"invalid JSON: {e}"], [])
    except OSError as e:
        return ([f"cannot read file: {e}"], [])

    if not isinstance(data, dict):
        return (["top-level JSON is not an object"], [])

    nodes = data.get("nodes")
    if not isinstance(nodes, list):
        fails.append("missing or non-array `nodes`")
        nodes = []

    connections = data.get("connections")
    if not isinstance(connections, dict):
        fails.append("missing or non-object `connections`")
        connections = {}

    # Top-level id (import:workflow fails without it)
    if not data.get("id"):
        warns.append("no top-level `id` (CLI `n8n import:workflow` fails without it)")

    # Per-node structure
    names = []
    for i, node in enumerate(nodes):
        if not isinstance(node, dict):
            fails.append(f"node[{i}] is not an object")
            continue
        label = node.get("name") or f"node[{i}]"
        if not node.get("name"):
            fails.append(f"node[{i}] missing `name`")
        else:
            names.append(node["name"])
        if not node.get("type"):
            fails.append(f"node '{label}' missing `type`")
        if "typeVersion" not in node:
            fails.append(f"node '{label}' missing `typeVersion`")
        pos = node.get("position")
        if not (isinstance(pos, list) and len(pos) == 2):
            fails.append(f"node '{label}' missing/invalid `position` (need len-2 array)")

    # Unique names
    name_set = set(names)
    if len(names) != len(name_set):
        dupes = sorted({n for n in names if names.count(n) > 1})
        fails.append(f"duplicate node name(s): {', '.join(dupes)}")

    # Connection integrity
    for src, outputs in connections.items():
        if src not in name_set:
            fails.append(f"connection source '{src}' is not an existing node")
        if not isinstance(outputs, dict):
            continue
        for _output_name, branches in outputs.items():
            if not isinstance(branches, list):
                continue
            for branch in branches:
                if not isinstance(branch, list):
                    continue
                for conn in branch:
                    if isinstance(conn, dict):
                        tgt = conn.get("node")
                        if tgt is not None and tgt not in name_set:
                            fails.append(
                                f"connection from '{src}' targets unknown node '{tgt}'")

    # Trigger presence
    if nodes and not any(is_trigger(n.get("type")) for n in nodes if isinstance(n, dict)):
        warns.append("no trigger node found (workflow can't start on its own)")

    return (fails, warns)


def main(argv):
    paths = argv[1:]
    if not paths:
        print("usage: python3 validate-workflow.py <workflow.json> [...]", file=sys.stderr)
        return 2

    any_fail = False
    for path in paths:
        fails, warns = validate(path)
        base = os.path.basename(path)
        if fails:
            any_fail = True
            print(f"FAIL  {base}  ({len(fails)} error(s), {len(warns)} warning(s))")
        else:
            tail = f"  ({len(warns)} warning(s))" if warns else ""
            print(f"PASS  {base}{tail}")
        for m in fails:
            print(f"        ERROR: {m}")
        for m in warns:
            print(f"        WARN:  {m}")

    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
