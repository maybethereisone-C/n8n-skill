# ClickUp Trigger — `n8n-nodes-base.clickUpTrigger`
**Type** `n8n-nodes-base.clickUpTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on ClickUp project/task lifecycle events via webhook.

**Credentials:** `clickUpApi` (personal API token) or `clickUpOAuth2Api`.

**Resources / Operations:**
| Resource | Events |
|---|---|
| Key result | Created · Deleted · Updated |
| List | Created · Deleted · Updated |
| Space | Created · Deleted · Updated |
| Task | Assignee updated · Comment posted · Comment updated · Created · Deleted · Due date updated · Moved · Status updated · Tag updated · Time estimate updated · Time tracked updated · Updated |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook on activation.
- Workspace ID is required to scope the webhook — events from all spaces/lists/tasks in that workspace can be received.
- Companion app node: `n8n-nodes-base.clickUp`.

**Source:** n8n-nodes-base.clickuptrigger.md  [doc-verified]
