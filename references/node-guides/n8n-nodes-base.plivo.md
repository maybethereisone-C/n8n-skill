# Plivo — `n8n-nodes-base.plivo`
**Type** `n8n-nodes-base.plivo` · **action**
**What:** Send SMS, MMS, and initiate voice calls via the Plivo communications platform.
**Credentials:** `plivoApi` (Auth ID + Auth Token)

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Call | Make a voice call |
| MMS | Send an MMS message |
| SMS | Send an SMS message |

## Key params & gotchas
- MMS is **US and Canada only** — sending to other regions will fail silently or return an error.
- Voice Call requires a valid `answer_url` (a publicly reachable URL returning Plivo XML) — without it the call connects but plays nothing.
- Phone numbers must be in E.164 format (e.g., `+14155551234`).
- Sender number must be a Plivo-owned DID or verified caller ID on the account.

**Source:** n8n-nodes-base.plivo.md  [doc-verified]
