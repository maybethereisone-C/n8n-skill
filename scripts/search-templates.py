#!/usr/bin/env python3
# Adapted from Zie619/n8n-workflows (MIT). Rewritten stdlib-only for the n8n skill.
"""Full-text search over bundled n8n template workflows.

`index [DIR]`   build a SQLite FTS5 index of every *.json workflow under DIR
                (default: ~/.claude/skills/n8n/templates/, recursive). Each row
                indexes name + node types + a generated description.
`search "<q>"`  return matching templates (relative path + name).

DB lives at ~/.claude/skills/n8n/scripts/.templates.db. Uses FTS5 when the
sqlite3 build supports it; otherwise falls back to a LIKE scan automatically.
"""
import glob
import json
import os
import sqlite3
import sys

SKILL = os.path.expanduser("~/.claude/skills/n8n")
DEFAULT_DIR = os.path.join(SKILL, "templates")
DB_PATH = os.path.join(SKILL, "scripts", ".templates.db")


def fts5_available(con):
    try:
        con.execute("CREATE VIRTUAL TABLE _fts_probe USING fts5(x)")
        con.execute("DROP TABLE _fts_probe")
        return True
    except sqlite3.OperationalError:
        return False


def is_trigger(node_type):
    t = str(node_type or "").lower()
    return "trigger" in t or t.endswith("manualtrigger")


def describe(name, node_types):
    """Build a short, searchable description from parsed workflow facts."""
    short = sorted({t.split(".")[-1] for t in node_types})
    trig = sorted({t.split(".")[-1] for t in node_types if is_trigger(t)})
    parts = [name]
    if trig:
        parts.append("triggered by " + ", ".join(trig))
    if short:
        parts.append("uses " + ", ".join(short))
    return ". ".join(parts)


def parse_workflow(path):
    """Return (name, integrations_str, description) or None if not a workflow."""
    try:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict) or not isinstance(data.get("nodes"), list):
        return None
    name = data.get("name") or os.path.splitext(os.path.basename(path))[0]
    node_types = [n.get("type", "") for n in data["nodes"] if isinstance(n, dict)]
    integrations = " ".join(sorted({t.split(".")[-1] for t in node_types if t}))
    return (name, integrations, describe(name, node_types))


def build_index(src_dir):
    src_dir = os.path.abspath(os.path.expanduser(src_dir))
    files = sorted(glob.glob(os.path.join(src_dir, "**", "*.json"), recursive=True))

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    con = sqlite3.connect(DB_PATH)
    use_fts = fts5_available(con)

    if use_fts:
        con.execute(
            "CREATE VIRTUAL TABLE templates USING fts5("
            "path, name, integrations, description)")
    else:
        con.execute(
            "CREATE TABLE templates (path TEXT, name TEXT, "
            "integrations TEXT, description TEXT)")

    n = 0
    for f in files:
        parsed = parse_workflow(f)
        if not parsed:
            continue
        name, integrations, description = parsed
        rel = os.path.relpath(f, src_dir)
        con.execute(
            "INSERT INTO templates (path, name, integrations, description) "
            "VALUES (?, ?, ?, ?)", (rel, name, integrations, description))
        n += 1

    con.execute("CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v TEXT)")
    con.execute("INSERT OR REPLACE INTO meta VALUES ('src_dir', ?)", (src_dir,))
    con.commit()
    con.close()
    print(f"INDEXED {n} template(s) from {src_dir}")
    print(f"  engine: {'FTS5' if use_fts else 'LIKE fallback'}  db: {DB_PATH}")
    return 0


def run_search(query):
    if not os.path.exists(DB_PATH):
        print("error: no index. Run `search-templates.py index` first.", file=sys.stderr)
        return 1
    con = sqlite3.connect(DB_PATH)

    is_fts = False
    try:
        row = con.execute(
            "SELECT sql FROM sqlite_master WHERE name='templates'").fetchone()
        is_fts = bool(row) and "fts5" in (row[0] or "").lower()
    except sqlite3.OperationalError:
        pass

    rows = []
    if is_fts:
        try:
            rows = con.execute(
                "SELECT path, name FROM templates WHERE templates MATCH ? "
                "ORDER BY rank", (query,)).fetchall()
        except sqlite3.OperationalError:
            rows = []  # bad FTS syntax -> fall through to LIKE
    if not rows:
        like = f"%{query}%"
        rows = con.execute(
            "SELECT path, name FROM templates WHERE "
            "name LIKE ? OR integrations LIKE ? OR description LIKE ?",
            (like, like, like)).fetchall()
    con.close()

    if not rows:
        print(f"no templates match: {query}")
        return 0
    print(f"{len(rows)} match(es) for '{query}':")
    for path, name in rows:
        print(f"  {path}  —  {name}")
    return 0


def main(argv):
    if len(argv) < 2 or argv[1] not in ("index", "search"):
        print("usage: python3 search-templates.py index [DIR]", file=sys.stderr)
        print("       python3 search-templates.py search \"<query>\"", file=sys.stderr)
        return 2
    if argv[1] == "index":
        return build_index(argv[2] if len(argv) > 2 else DEFAULT_DIR)
    if len(argv) < 3:
        print("error: search needs a query string", file=sys.stderr)
        return 2
    return run_search(argv[2])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
