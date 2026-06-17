# n8n Template Sources

Where to get n8n workflow templates, with license and quality notes.
Facts verified against the GitHub API and each source on **2026-06-17**.

> **License reality first:** n8n's own workflow content is **fair-code** under the
> **Sustainable Use License**, not OSI open-source. Practically: redistribute only
> *free* and *non-commercial*, and keep attribution. Many "MIT" GitHub mirrors are
> bulk scrapes of n8n.io content, so their MIT claim is questionable — verify before
> you redistribute or ship anything commercially.

## Sources

| Source | Scale | License | Updated | Notes |
|---|---|---|---|---|
| **[n8n.io/workflows](https://n8n.io/workflows/)** (official) | ~10,170 workflows | n8n Sustainable Use License (free) | live | Search/filter, 1-click import. **Best overall.** |
| **[n8n.io/creators](https://n8n.io/creators/)** (official) | hundreds each | Sustainable Use License | live | Verified creators (e.g. Rahul Joshi — 261 workflows). |
| **[Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows)** | 4,343 workflow JSONs | MIT (questionable for scraped) | 2026-05-31 | 55,175★. Mega-dump (incl. scraped from n8n.io), mixed quality. FTS search UI at [zie619.github.io/n8n-workflows](https://zie619.github.io/n8n-workflows/). 16-category business-domain taxonomy in `references/template-categories/`. |
| **[enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates)** | ~301 templates | **NOASSERTION** (NOT MIT — check before redistribute) | 2026-06-01 | 23,044★. **Best curated.** 18 department-tagged categories (below). |
| **[oxbshw/Open-Workflow-Library](https://github.com/oxbshw/Open-Workflow-Library)** | — | MIT | 2026-05-24 | 541★. |
| **[ScraperNode/awesome-n8n-templates](https://github.com/ScraperNode/awesome-n8n-templates)** | 8,697 JSONs | — | — | 30★. Auto-scraped mirror of n8n.io (**redundant**). |
| **[restyler/awesome-n8n](https://github.com/restyler/awesome-n8n)** | — | — | 2026-01-20 | 2,914★. **NOT templates** — ranked list of top-100 community *nodes* by monthly npm downloads (5,834 total nodes indexed). See `references/community-nodes.md`. |
| **[pixeljets.com](https://pixeljets.com/blog/n8n/)** | blog | — | active | Practitioner blog: production patterns, web scraping in n8n, converting workflows to SaaS products. Higher signal-to-noise than average tutorials. |
| **Nate Herk** | ~90–100+ templates | paid / gated | — | Gated in his paid "AI Automation Society Plus" Skool (~$99/mo). The repo's `templates/nate-herk-templates/` folder is his course set. |

### enescingoz categories (17)
`AI_Research_RAG` · `OpenAI_and_LLMs` · `Gmail` · `Slack` · `Telegram` ·
`WhatsApp` · `Instagram_Twitter_Social_Media` · `Notion` · `Airtable` ·
`WordPress` · `HR` · `PDF` · `Database` · `Forms` · `Discord` ·
`Google_Drive_Sheets` · `Other`

## Which to pick

- **AI-agent / marketing automation** → **enescingoz/awesome-n8n-templates** + **n8n.io/workflows** (and **Nate Herk**'s paid set if you have access).
- **General production workflows** → **n8n.io/workflows** + **Zie619/n8n-workflows**.

Skip ScraperNode (redundant mirror of n8n.io) and restyler (it's a node/tutorial
list, not templates).

## Using the bundled tooling

The skill bundles a few JSON templates under `templates/` (incl.
`templates/nate-herk-templates/`). Two stdlib-only scripts work over them:

**Search templates** (`scripts/search-templates.py` — SQLite FTS5, LIKE fallback):

```bash
# Build / rebuild the index over ~/.claude/skills/n8n/templates/ (recursive)
python3 ~/.claude/skills/n8n/scripts/search-templates.py index

# Find templates by name, node type, or generated description
python3 ~/.claude/skills/n8n/scripts/search-templates.py search "rag agent"
python3 ~/.claude/skills/n8n/scripts/search-templates.py search "slack"
```

**Validate before importing** (`scripts/validate-workflow.py` — catches the
structural problems that make `n8n import:workflow` fail, e.g. a missing top-level
`id`, broken connection targets, or duplicate node names):

```bash
python3 ~/.claude/skills/n8n/scripts/validate-workflow.py path/to/workflow.json [...]
# exit 0 = all PASS (warnings ok), exit 1 = at least one FAIL
```

**Visualize a workflow** (`scripts/workflow-to-mermaid.py` — Mermaid `graph TD`):

```bash
python3 ~/.claude/skills/n8n/scripts/workflow-to-mermaid.py path/to/workflow.json
```

Recommended flow when pulling a template from any source above: **download →
`validate-workflow.py` → `workflow-to-mermaid.py` to eyeball the shape →** import.
