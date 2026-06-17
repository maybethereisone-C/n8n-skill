# HR-and-Recruitment

**4 workflows.** HR and recruiting workflows.

## What's here
Resume screening, candidate intake, and recruitment-pipeline automations.

## When Claude should reach for this folder
Reach for `HR-and-Recruitment/` when the user wants to automate hiring, resume parsing, or candidate workflows.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `HR-and-Recruitment/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/HR-and-Recruitment/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
