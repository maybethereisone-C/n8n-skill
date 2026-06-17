# Vonage — `n8n-nodes-base.vonage`
**Type** `n8n-nodes-base.vonage` · **typeVersion** 1 · **action**
**What:** Send SMS messages via the Vonage (formerly Nexmo) Communications API.
**Credentials:** `vonageApi` (API Key + API Secret from Vonage dashboard).
**Resources / Operations:**
| Resource | Operations |
|----------|-----------|
| SMS | Send |

**Key params & gotchas:**
- `from` must be a Vonage virtual number or approved alphanumeric sender ID (alphanumeric IDs not supported in all countries, e.g., USA).
- Delivery receipts require a webhook callback URL configured in Vonage dashboard — not handled by this node directly.
- For WhatsApp or voice, use the Twilio node instead; Vonage node is SMS-only.

**Source:** n8n-nodes-base.vonage.md  [doc-verified]
