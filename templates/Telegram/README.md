# Telegram

**141 workflows.** Telegram bot and messaging workflows.

## What's here
Telegram bot triggers, message send/receive, media handling, and Telegram-as-frontend for AI agents and automations. The single largest messaging collection here.

## When Claude should reach for this folder
Reach for `Telegram/` when the user wants a Telegram bot, chat interface, or notification channel via Telegram.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Telegram/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Telegram/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
