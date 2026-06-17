# Database

**50 workflows.** SQL/NoSQL database workflows.

## What's here
Postgres, MySQL, Supabase, MongoDB, Redis, Elasticsearch, BigQuery, and Excel-as-data flows, including Supabase Postgres vector storage.

## When Claude should reach for this folder
Reach for `Database/` when the user needs to query or persist data in a real database, or use Postgres/Supabase as a vector store.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Database/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Database/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
