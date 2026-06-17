# Web-Scraping

**190 workflows.** Web scraping and data-extraction workflows.

## What's here
Apify and Firecrawl scrapers, HTTP-request-based extraction, crawling, and site-content harvesting pipelines. The HTTP-request reference collection lives here.

## When Claude should reach for this folder
Reach for `Web-Scraping/` when the user wants to scrape a website, crawl pages, call an arbitrary HTTP API, or extract structured data from the web.

## Usage
- Search all templates (result paths are prefixed with the topic folder, so filter on `Web-Scraping/`): `python3 scripts/search-templates.py search "<query>"`
- Validate before importing: `python3 scripts/validate-workflow.py templates/Web-Scraping/<file>.json`
- All credentials, API keys, and personal emails in these files are redacted (`REDACTED`, `REDACTED_JWT`, `you@example.com`). Re-add your own credentials in n8n after import.
