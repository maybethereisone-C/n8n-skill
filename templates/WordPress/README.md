# WordPress

**11 workflows.** WordPress content workflows.

## What's here
Creating and updating WordPress posts/pages and publishing generated content to WordPress.

## When Claude should reach for this folder
Reach for `WordPress/` when the user wants to publish or manage WordPress content programmatically.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `WordPress/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/WordPress/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
