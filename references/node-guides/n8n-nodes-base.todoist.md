# Todoist — `n8n-nodes-base.todoist`
**Type** `n8n-nodes-base.todoist` · **typeVersion** 1 · **action**
**What:** Create, read, update, delete, close, and reopen tasks in Todoist.
**Credentials:** `todoistApi` or `todoistOAuth2Api`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Task | Create, Close, Delete, Get, Get All, Reopen, Update |

**Key params & gotchas:**
- "Close" marks a task complete; "Reopen" marks it incomplete — distinct from Delete.
- Tasks can be assigned to projects/sections by ID; use the Todoist API to discover IDs.
- Supports AI tool use (appears in `--8<-- ai-tools snippet`) — can be used as an AI agent tool.

**Source:** n8n-nodes-base.todoist.md  [doc-verified]
