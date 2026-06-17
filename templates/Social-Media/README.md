# Social-Media

**34 workflows.** Social-media publishing and content workflows.

## What's here
Twitter/X, LinkedIn, Facebook, Instagram, and YouTube automations: scheduled posting, content generation, lead ads, and product-video pipelines.

## When Claude should reach for this folder
Reach for `Social-Media/` when the user wants to publish, schedule, or generate content for social platforms, or pull social data.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Social-Media/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Social-Media/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
