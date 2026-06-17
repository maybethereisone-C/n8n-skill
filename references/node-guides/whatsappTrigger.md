# WhatsApp Trigger — `n8n-nodes-base.whatsappTrigger`
**Type** `n8n-nodes-base.whatsappTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on WhatsApp Business Platform events (messages, account updates, template status, etc.) via Meta webhook.
**Credentials:** `whatsappApi` (WhatsApp Business Account credentials via Meta app).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Messages | Inbound messages, message status updates (sent/delivered/read) |
| Account Review Update | Account under review status change |
| Account Update | Business account info changed |
| Business Capability Update | Capability limit changes |
| Message Template Quality Update | Template quality score changed |
| Message Template Status Update | Template approved/rejected/paused |
| Phone Number Name Update | Display name change |
| Phone Number Quality Update | Phone number quality rating changed |
| Security | Two-step verification changes |
| Template Category Update | Template category reclassified |

**Key params & gotchas:**
- Trigger type: **webhook** — Meta pushes events to n8n's webhook URL registered in the Meta App Dashboard.
- WhatsApp allows only **one webhook URL per app** — test and production URLs cannot coexist; deactivate the production workflow before testing (this halts live traffic).
- The `Messages` event covers both inbound messages AND delivery receipts (sent/delivered/read) — use a Switch node on `entry[].changes[].value.statuses` vs `messages` to separate them.
- Meta requires webhook verification (GET challenge-response) before it will send events — n8n handles this automatically.

**Source:** n8n-nodes-base.whatsapptrigger.md  [doc-verified]
