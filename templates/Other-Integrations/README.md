# Other-Integrations

**1532 workflows.** Catch-all integrations and reusable building blocks.

## What's here
Generic n8n plumbing (Manual/Schedule/Webhook/Wait triggers, Code, Filter, Split Out, Merge, control-flow nodes) plus hundreds of SaaS connectors not covered by a dedicated topic (CRM, project management, payments, calendars, etc.). The largest folder by far.

## When Claude should reach for this folder
Reach for `Other-Integrations/` when no dedicated topic fits, or the user wants a generic trigger/control-flow pattern, a Code-node example, or a connector for a niche SaaS tool. Search by keyword before assuming a pattern is missing.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Other-Integrations/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Other-Integrations/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
