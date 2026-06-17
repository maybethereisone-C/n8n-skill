# Flow — `n8n-nodes-base.flow`
**Type** `n8n-nodes-base.flow` · **action**
**What:** Manage tasks in the Flow project management app.
**Credentials:** flowApi (API key + organization ID).

## Resources / Operations
| Resource | Operations |
|---|---|
| Task | Create, Update, Get, Get All |

## Key params & gotchas
- Flow uses **organization ID** + **workspace ID** to scope requests; both are required.
- A companion trigger node exists: `n8n-nodes-base.flowTrigger`.
- Task status and assignee are set via field IDs, not names — look up IDs from a prior Get All call.

**Source:** n8n-nodes-base.flow.md  [doc-verified]
