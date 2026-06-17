# PDF-and-Documents

**57 workflows.** Document generation and extraction workflows.

## What's here
PDF/file extraction, binary read/write, document-to-data parsing, invoice processing, and APITemplate.io document generation.

## When Claude should reach for this folder
Reach for `PDF-and-Documents/` when the user wants to extract text/data from PDFs or files, or generate documents/invoices.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `PDF-and-Documents/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/PDF-and-Documents/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
