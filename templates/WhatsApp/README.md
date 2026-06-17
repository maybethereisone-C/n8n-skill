# WhatsApp

**6 workflows.** WhatsApp Business messaging workflows.

## What's here
WhatsApp send/receive flows and WhatsApp-as-channel for support and notification bots.

## When Claude should reach for this folder
Reach for `WhatsApp/` when the user wants to send or receive WhatsApp messages or build a WhatsApp support/notification bot.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `WhatsApp/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/WhatsApp/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
