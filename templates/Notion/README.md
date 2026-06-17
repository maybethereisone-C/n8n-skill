# Notion

**13 workflows.** Notion database and page workflows.

## What's here
Creating and updating Notion pages and databases, syncing Notion with other tools, and Notion-as-CMS automations.

## When Claude should reach for this folder
Reach for `Notion/` when the user wants to read or write Notion databases/pages or sync Notion with another system.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Notion/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Notion/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
