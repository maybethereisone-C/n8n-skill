# Asana Trigger — `n8n-nodes-base.asanaTrigger`
**Type** `n8n-nodes-base.asanaTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on Asana workspace/project events via webhook (task and project activity).

**Credentials:** `asanaApi` (personal access token) or `asanaOAuth2Api`.

**Resources / Operations:**
| Event |
|---|
| New Asana event (generic — any webhook event configured in Asana) |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with Asana on workflow activation.
- The generic "New Asana event" means all event types arrive at this trigger — use downstream filtering on `$.action` (added, changed, removed, deleted) and `$.resource.resource_type` to branch.
- Companion app node: `n8n-nodes-base.asana`.

**Source:** n8n-nodes-base.asanatrigger.md  [doc-verified]
