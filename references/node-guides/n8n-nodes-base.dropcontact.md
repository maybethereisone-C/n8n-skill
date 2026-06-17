# Dropcontact — `n8n-nodes-base.dropcontact`
**Type** `n8n-nodes-base.dropcontact` · **action**
**What:** Enrich and verify B2B contact data (email finding, validation, GDPR-compliant) via Dropcontact.
**Credentials:** dropcontactApi (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Enrich, Fetch Request |

## Key params & gotchas
- **Enrich** submits a contact enrichment batch — it returns a `request_id` immediately (async); use **Fetch Request** with that ID to retrieve results once ready.
- Enrichment is asynchronous — poll with a Wait + Fetch cycle; typical latency is seconds to minutes.
- Input can include first name, last name, company, and website/domain; at minimum first+last+company or email is needed.
- GDPR-compliant by design: Dropcontact doesn't store submitted data.

**Source:** n8n-nodes-base.dropcontact.md  [doc-verified]
