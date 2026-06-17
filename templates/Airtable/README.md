# Airtable

**14 workflows.** Airtable and no-code-database workflows.

## What's here
Airtable record CRUD plus Baserow, NocoDB, and Grist alternatives used as backing stores.

## When Claude should reach for this folder
Reach for `Airtable/` when the user wants to read/write Airtable (or a no-code DB) records or use one as a lightweight backend.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Airtable/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Airtable/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
