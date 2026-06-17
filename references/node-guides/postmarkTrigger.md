# Postmark Trigger — `n8n-nodes-base.postmarkTrigger`
**Type** `n8n-nodes-base.postmarkTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Postmark transactional email event occurs (delivery, open, bounce, spam complaint, inbound message) via webhook.
**Credentials:** `postmarkApi` (server API token).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Delivery | Email successfully delivered |
| Open | Recipient opened the email |
| Bounce | Hard or soft bounce |
| Spam Complaint | Recipient marked as spam |
| Inbound | Inbound email received at a Postmark inbound address |

**Key params & gotchas:**
- Postmark webhooks are **server-scoped** — the n8n webhook URL must be configured in the Postmark **Server Settings → Webhooks** panel; n8n may not auto-register depending on version.
- Each event type requires a separate webhook entry in Postmark (or one n8n workflow per event type).
- Open tracking must be enabled at the server level for Open events to fire.
- Inbound email events arrive with full parsed headers, text, HTML, and attachments as base64.

**Source:** n8n-nodes-base.postmarktrigger.md  [doc-verified]
