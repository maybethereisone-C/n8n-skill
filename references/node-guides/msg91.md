# MSG91 — `n8n-nodes-base.msg91`
**Type** `n8n-nodes-base.msg91` · **typeVersion** 1 · **action**
**What:** Send SMS messages via MSG91 (India-focused SMS gateway).
**Credentials:** MSG91 API key (`msg91Api`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| SMS | Send SMS |

**Key params & gotchas:**
- Requires a **Sender ID** registered in the MSG91 dashboard (Settings → Sender Id). New sender IDs require approval.
- Indian DLT regulations require pre-approved templates and registered headers; non-compliant messages will be rejected.
- Phone numbers must include country code (e.g., `919876543210` for India).

**Source:** n8n-nodes-base.msg91.md  [doc-verified]
