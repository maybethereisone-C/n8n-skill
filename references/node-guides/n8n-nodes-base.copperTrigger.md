# Copper Trigger — `n8n-nodes-base.copperTrigger`
**Type** `n8n-nodes-base.copperTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on CRM record lifecycle events from Copper (Google Workspace-integrated CRM).

**Credentials:** `copperApi` (email + API key).

**Resources / Operations:**
| Event |
|---|
| Delete |
| New |
| Update |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with Copper on activation.
- Events apply across all record types in Copper (leads, people, companies, opportunities, projects, tasks) — use downstream filtering on `$.type` to narrow by entity type.
- Companion app node: `n8n-nodes-base.copper`.

**Source:** n8n-nodes-base.coppertrigger.md  [doc-verified]
