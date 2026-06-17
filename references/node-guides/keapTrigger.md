# Keap Trigger — `n8n-nodes-base.keapTrigger`
**Type** `n8n-nodes-base.keapTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires a workflow when a Keap (Infusionsoft) CRM/marketing event occurs via webhook.
**Credentials:** `keapOAuth2Api` (OAuth2).
**Resources / Operations:**
| Event category | Examples |
|---|---|
| Contact | Contact created, updated, merged |
| Order / Invoice | Order placed, invoice paid |
| Tag | Tag applied / removed |
| Task | Task completed |

**Key params & gotchas:**
- n8n auto-registers the webhook on activation and deletes it on deactivation.
- Keap webhooks require a published app with webhook permission; sandbox accounts may have limited event types.
- The payload structure differs between Keap Classic (Infusionsoft) and Keap Pro/Max — check which API version your credential targets.

**Source:** n8n-nodes-base.keaptrigger.md  [doc-verified]
