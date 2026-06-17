# Mailgun — `n8n-nodes-base.mailgun`
**Type** `n8n-nodes-base.mailgun` · **typeVersion** 1 · **action**
**What:** Send transactional emails via Mailgun.
**Credentials:** `mailgunApi` (API key + domain).

## Resources / Operations
| Resource | Operations |
|---|---|
| (flat) | Send Email |

## Key params & gotchas
- **Send Email** supports `to`, `cc`, `bcc`, `subject`, `text`, `html`, and file attachments (binary input).
- The **domain** must be configured and verified in Mailgun — the credential domain and the sending domain must match.
- Mailgun has US and EU API endpoints; the credential must point to the correct regional base URL (`api.mailgun.net` vs `api.eu.mailgun.net`).
- For high-volume sending, pair with a Split In Batches loop; Mailgun rate limits apply per account.
- For receiving emails or tracking events (opens/clicks/bounces), use webhooks (not this node).

**Source:** n8n-nodes-base.mailgun.md  [doc-verified]
