# Mautic Trigger — `n8n-nodes-base.mauticTrigger`
**Type** `n8n-nodes-base.mauticTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Mautic marketing automation event occurs (contact activity, form submit, campaign event, etc.) via webhook.
**Credentials:** `mauticApi` (username/password) or `mauticOAuth2Api`.
**Resources / Operations:**
| Event category | Examples |
|---|---|
| Contact | Created, updated, deleted, identified |
| Form | Submission |
| Campaign | Entry, exit, action |
| Email | Opened, clicked, bounced |
| Page | Hit |

**Key params & gotchas:**
- n8n registers the Mautic webhook automatically on workflow activation (via Mautic's Webhook API).
- Mautic sends batched payloads — each trigger execution may contain an array of events; iterate with a Split In Batches node if needed.
- Self-hosted Mautic: ensure the n8n webhook URL is reachable from the Mautic server.

**Source:** n8n-nodes-base.mautictrigger.md  [doc-verified]
