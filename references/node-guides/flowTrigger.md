# Flow Trigger — `n8n-nodes-base.flowTrigger`
**Type** `n8n-nodes-base.flowTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on new events from the Flow task/project management app via webhook.
**Credentials:** `flowApi`

## Events

| Event | Notes |
|---|---|
| New Flow event | Any new activity event in the scoped project/task |

## Key params & gotchas
- `listIds` (Project ID) — required to scope to a project (resource=list or resource=task).
- `taskIds` (Task ID) — required when resource=task.
- The schema shows `resource` options: `list` and `task` — filter at source to avoid noisy all-project webhooks.
- Companion app node available: `n8n-nodes-base.flow`.

**Source:** n8n-nodes-base.flowtrigger.md  [doc-verified]
