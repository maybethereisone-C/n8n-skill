# Discord

**7 workflows.** Discord bot and notification workflows.

## What's here
Discord message posting, bot triggers, and community/notification automations.

## When Claude should reach for this folder
Reach for `Discord/` when the user wants to post to Discord, build a Discord bot, or route alerts to a Discord channel.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Discord/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Discord/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
