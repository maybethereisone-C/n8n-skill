# Markdown — `n8n-nodes-base.markdown`
**Type** `n8n-nodes-base.markdown` · **core**

**What:** Converts between Markdown and HTML in both directions.

**Credentials:** none.

**Resources / Operations:**
| Mode | Direction | Parser |
|------|-----------|--------|
| Markdown to HTML | MD → HTML | Showdown (GitHub Flavored MD options available) |
| HTML to Markdown | HTML → MD | node-html-markdown |

**Key params & gotchas:**
- **Destination Key** supports dot notation for nested output (e.g., `level1.level2.key`).
- MD→HTML notable options: `GitHub Code Blocks` (on by default), `Tables Support` (off by default), `Strikethrough`, `Emoji Support`, `Complete HTML Document` (wraps in full DOCTYPE).
- HTML→MD notable options: `Bullet Marker`, `Code Block Fence`, `Max Consecutive New Lines`, `Ignored Elements`.
- `Global Escape Pattern` and `Line Start Escape Pattern` override default escaping — prefer `Text Replacement Pattern` for simpler substitutions.
- Some options interact; test combinations before relying on output format.

**Source:** n8n-nodes-base.markdown.md  [doc-verified]
