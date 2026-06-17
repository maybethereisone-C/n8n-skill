# UpLead — `n8n-nodes-base.uplead`
**Type** `n8n-nodes-base.uplead` · **typeVersion** 1 · **action**
**What:** Enrich company and person records using UpLead's B2B data platform (consumes credits per call).
**Credentials:** `upleadApi` (API key).
**Resources / Operations:**
| Resource | Operation |
|----------|-----------|
| Company | Enrich |
| Person | Enrich |

**Key params & gotchas:** Each enrichment call consumes UpLead credits. Company enrich takes a domain; Person enrich typically takes email or LinkedIn URL. Returns contact details, company firmographics, and tech stack data.
**Source:** n8n-nodes-base.uplead.md  [doc-verified]
