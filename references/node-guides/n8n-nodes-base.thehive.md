# TheHive — `n8n-nodes-base.thehive`
**Type** `n8n-nodes-base.thehive` · **typeVersion** 1 · **action**
**What:** Manage security incident response resources (alerts, cases, logs, observables, tasks) in TheHive v3/v4.
**Credentials:** `theHiveApi`
**Resources / Operations:**
| Resource | Notes |
|---|---|
| Alert | Operations vary by API version (v3/v4) |
| Case | Operations vary by API version |
| Log | Operations vary by API version |
| Observable | Operations vary by API version |
| Task | Operations vary by API version |

**Key params & gotchas:**
- **Use this node for TheHive API v3 or v4 only.** For v5, use `n8n-nodes-base.thehive5`.
- Available operations are determined by the API version selected in credentials — create credentials first, then return to the node to see operations.
- Companion trigger node available: `n8n-nodes-base.theHiveTrigger`.

**Source:** n8n-nodes-base.thehive.md  [doc-verified]
