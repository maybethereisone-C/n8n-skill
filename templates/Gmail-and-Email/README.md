# Gmail-and-Email

**68 workflows.** Email send/read and inbox-automation workflows.

## What's here
Gmail and Outlook send/read, IMAP polling, auto-reply and triage, newsletter/ESP integrations (Mailchimp, Mailerlite, Mailjet, Lemlist, ConvertKit), and a voice-driven email agent.

## When Claude should reach for this folder
Reach for `Gmail-and-Email/` when the user wants to send, read, label, summarize, or auto-respond to email, or integrate a mail provider.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Gmail-and-Email/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Gmail-and-Email/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
