# Google-Sheets-and-Drive

**57 workflows.** Google Sheets, Drive, Docs, and Slides workflows.

## What's here
Reading/writing spreadsheets, Drive file management, Docs generation, and Sheets-as-database patterns.

## When Claude should reach for this folder
Reach for `Google-Sheets-and-Drive/` when the user wants to read/write Google Sheets, manage Drive files, or generate Google Docs/Slides.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Google-Sheets-and-Drive/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Google-Sheets-and-Drive/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
