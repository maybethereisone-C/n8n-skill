# DevOps

**4 workflows.** Operational and observability workflows.

## What's here
Error logging, alerting, and monitoring patterns for keeping production n8n workflows healthy.

## When Claude should reach for this folder
Reach for `DevOps/` when the user wants error handling, logging, alerting, or operational monitoring for their automations.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `DevOps/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/DevOps/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
