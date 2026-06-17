# Airtop — `n8n-nodes-base.airtop`
**Type** `n8n-nodes-base.airtop` · **action**
**What:** Control a cloud-based browser via Airtop to scrape, query, and interact with web pages programmatically.
**Credentials:** Airtop API key credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Session | Create session, Save profile on termination, Terminate session |
| Window | Create a new browser window, Load URL, Take screenshot, Close window |
| Extraction | Query page, Query page with pagination, Smart scrape page |
| Interaction | Click an element, Hover on an element, Type |

## Key params & gotchas
- **Workflow order matters:** Session must be created first → Window created next → then Extraction or Interaction ops. Session ID flows through all subsequent steps.
- **Idle Timeout** on Create Session auto-terminates sessions — always pair with Terminate Session to avoid billing runaway.
- **Query page** and **Query page with pagination** accept a **JSON Output Schema** param to get structured JSON instead of free text.
- "Smart scrape page" returns page content as markdown — useful for LLM ingestion.
- Interaction operations describe elements in natural language (not CSS selectors) — Airtop uses AI to locate them.
- Profile save on termination persists cookies/login state for reuse across sessions.

**Source:** n8n-nodes-base.airtop.md  [doc-verified]
