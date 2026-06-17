# Webex by Cisco Trigger — `n8n-nodes-base.ciscoWebexTrigger`
**Type** `n8n-nodes-base.ciscoWebexTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on Webex by Cisco events (meetings, messages, rooms, memberships) via webhook.

**Credentials:** `ciscoWebexOAuth2Api` (OAuth2).

**Resources / Operations:**
| Trigger type | What fires it |
|---|---|
| Webhook | Webex events selected during node configuration (messages created, rooms updated, memberships changed, meetings started/ended, etc.) |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with Webex automatically.
- Companion app node: `n8n-nodes-base.ciscoWebex`.

**Source:** n8n-nodes-base.ciscowebextrigger.md  [doc-verified]
