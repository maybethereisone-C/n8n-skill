# n8n Template Library — unified, secret-scrubbed reference workflows

**2,390 workflows across 19 topic folders.** A merged, all-in-one library of real n8n workflows organized by what they *do*, not who authored them. Import any file into n8n → Workflows → Import from File.

All secrets are scrubbed for public use: API keys → `REDACTED`, JWTs → `REDACTED_JWT`, personal emails → `you@example.com`. Re-add real values through n8n **credentials** after import — never inline.

## Topics

| Folder | Count | Purpose |
|---|---:|---|
| [`AI-Agents/`](AI-Agents/) | 107 | LLM agents, orchestrators, prompt chaining/routing/parallelization, image gen. |
| [`RAG-and-Vector/`](RAG-and-Vector/) | 35 | Retrieval-augmented generation, embeddings, vector stores, doc Q&A. |
| [`Gmail-and-Email/`](Gmail-and-Email/) | 68 | Gmail/Outlook/IMAP send-read, triage, auto-reply, ESP integrations. |
| [`Slack/`](Slack/) | 27 | Slack messages, bots, alerts, slash/event handlers. |
| [`Telegram/`](Telegram/) | 141 | Telegram bots, chat interfaces, notification channels. |
| [`WhatsApp/`](WhatsApp/) | 6 | WhatsApp Business send/receive and support bots. |
| [`Discord/`](Discord/) | 7 | Discord bots and channel notifications. |
| [`Social-Media/`](Social-Media/) | 34 | Twitter/X, LinkedIn, Facebook, Instagram, YouTube publishing & content. |
| [`Google-Sheets-and-Drive/`](Google-Sheets-and-Drive/) | 57 | Sheets, Drive, Docs, Slides read/write and Sheets-as-DB. |
| [`Notion/`](Notion/) | 13 | Notion page/database CRUD and sync. |
| [`Airtable/`](Airtable/) | 14 | Airtable + Baserow/NocoDB/Grist no-code-DB records. |
| [`Database/`](Database/) | 50 | Postgres, MySQL, Supabase, MongoDB, Redis, Elasticsearch, BigQuery. |
| [`Forms-and-Surveys/`](Forms-and-Surveys/) | 33 | n8n Form, Typeform, Jotform, Wufoo, SurveyMonkey intake. |
| [`PDF-and-Documents/`](PDF-and-Documents/) | 57 | File/PDF extraction, document generation, invoices. |
| [`HR-and-Recruitment/`](HR-and-Recruitment/) | 4 | Resume screening and recruiting pipelines. |
| [`WordPress/`](WordPress/) | 11 | WordPress post/page publishing. |
| [`DevOps/`](DevOps/) | 4 | Error logging, alerting, operational monitoring. |
| [`Web-Scraping/`](Web-Scraping/) | 190 | Apify/Firecrawl scrapers, HTTP-request extraction, crawling. |
| [`Other-Integrations/`](Other-Integrations/) | 1532 | Generic triggers/control-flow + hundreds of niche SaaS connectors. Search before assuming a pattern is missing. |

Each folder has its own `README.md` describing what it holds and when Claude should reach for it.

## How to search

Build the index once, then query (results are `topic/file.json — workflow name`):

```bash
python3 scripts/search-templates.py index templates
python3 scripts/search-templates.py search "telegram openai agent"
```

FTS5 matches name, integration node types, and a generated description; it falls back to a LIKE scan automatically. Filter by topic by reading the path prefix in each result.

## How to validate

Before importing or reusing a workflow:

```bash
python3 scripts/validate-workflow.py templates/<Topic>/<file>.json
```

## Production hardening

These are real-world and demo workflows — most lack production hardening (error workflows, retries, secured webhooks). That hardening is what the rest of this skill adds:

1. Read the matching `references/*.md` for the deep pattern.
2. Import the JSON; inspect node wiring (connections are keyed by node **name**).
3. Run `references/production-checklist.md` against it — add an error workflow, retries, logging, and secure any trigger.

See also `references/category-taxonomy/` (source category data) and `references/template-index-llms.txt` (LLM-readable template index).
