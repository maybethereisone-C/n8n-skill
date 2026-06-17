# Slack

**27 workflows.** Slack messaging and bot workflows.

## What's here
Posting messages and alerts, slash-command and event handlers, channel notifications, and Slack-as-frontend for agents.

## When Claude should reach for this folder
Reach for `Slack/` when the user wants to send Slack messages, build a Slack bot, or push notifications/alerts into Slack.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Slack/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Slack/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
