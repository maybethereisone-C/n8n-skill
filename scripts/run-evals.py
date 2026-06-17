#!/usr/bin/env python3
"""Behavioral eval harness for the n8n skill (stdlib, no deps).

Evals are query -> expected_behavior checklists (Evaluation-Driven Development).
There is no LLM call here: an agent answers the `query` using the skill, then
self-checks the answer against the printed checklist. `validate` is a CI gate
that fails on malformed eval files.

Usage:
    python3 scripts/run-evals.py list [--category C]
    python3 scripts/run-evals.py show <id>
    python3 scripts/run-evals.py validate
    python3 scripts/run-evals.py --category security      # == list --category security
"""
import json
import sys
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parent.parent / "evals"
REQUIRED = ("id", "category", "query", "ref", "expected_behavior")


def load_all():
    """Return (evals, errors). evals: list of dicts. errors: list of (path, msg)."""
    evals, errors = [], []
    for p in sorted(EVALS_DIR.glob("*.json")):
        try:
            data = json.loads(p.read_text())
        except json.JSONDecodeError as e:
            errors.append((p.name, f"invalid JSON: {e}"))
            continue
        for key in REQUIRED:
            if key not in data:
                errors.append((p.name, f"missing required key: {key}"))
        eb = data.get("expected_behavior")
        if eb is not None and (not isinstance(eb, list) or not eb):
            errors.append((p.name, "expected_behavior must be a non-empty array"))
        data["_file"] = p.name
        evals.append(data)
    return evals, errors


def cmd_validate(evals, errors):
    if errors:
        for name, msg in errors:
            print(f"FAIL  {name}: {msg}")
        print(f"\n{len(errors)} problem(s) across eval files.")
        return 1
    # id uniqueness
    seen = {}
    dupes = 0
    for e in evals:
        if e.get("id") in seen:
            print(f"FAIL  duplicate id '{e['id']}' in {e['_file']} and {seen[e['id']]}")
            dupes += 1
        else:
            seen[e["id"]] = e["_file"]
    if dupes:
        return 1
    print(f"OK  {len(evals)} eval(s) valid.")
    return 0


def cmd_list(evals, category=None):
    shown = 0
    for e in evals:
        if category and e.get("category") != category:
            continue
        print(f"  [{e.get('category','?'):<14}] {e.get('id','?'):<22} {e.get('query','')}")
        shown += 1
    if category and shown == 0:
        cats = sorted({e.get("category") for e in evals})
        print(f"(no evals in category '{category}'. categories: {', '.join(cats)})")
        return 1
    return 0


def cmd_show(evals, eval_id):
    for e in evals:
        if e.get("id") == eval_id:
            print(f"id:       {e['id']}")
            print(f"category: {e['category']}")
            print(f"ref:      {e['ref']}")
            print(f"query:    {e['query']}")
            print("expected_behavior:")
            for i, b in enumerate(e["expected_behavior"], 1):
                print(f"  {i}. {b}")
            return 0
    print(f"no eval with id '{eval_id}'. Run `list` to see ids.")
    return 1


def main(argv):
    args = argv[1:]
    category = None
    if "--category" in args:
        i = args.index("--category")
        try:
            category = args[i + 1]
        except IndexError:
            print("--category needs a value")
            return 2
        del args[i:i + 2]

    cmd = args[0] if args else ("list" if category else "list")
    evals, errors = load_all()

    if cmd == "validate":
        return cmd_validate(evals, errors)
    # for non-validate commands, surface malformed files but keep going
    for name, msg in errors:
        print(f"WARN  {name}: {msg}", file=sys.stderr)
    if cmd == "list":
        return cmd_list(evals, category)
    if cmd == "show":
        if len(args) < 2:
            print("usage: run-evals.py show <id>")
            return 2
        return cmd_show(evals, args[1])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
