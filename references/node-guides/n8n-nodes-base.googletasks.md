# Google Tasks — `n8n-nodes-base.googleTasks`
**Type** `n8n-nodes-base.googleTasks` · **typeVersion** 1 · **action**
**What:** Creates, reads, updates, and deletes tasks in Google Tasks task lists.
**Credentials:** `googleTasksOAuth2Api` (OAuth2).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Task | Create (add to task list), Delete, Get, Get All, Update |

**Key params & gotchas:**
- Requires a **Task List ID** — obtain it via the Google Tasks API or by inspecting the URL in the web UI (it's in the path after `lists/`).
- Due dates must be in RFC 3339 format (`2024-12-31T00:00:00Z`); the time component is ignored — Google Tasks stores only the date.
- Completed tasks are hidden in the default Google Tasks UI but remain in the API; Get All returns them only if `showCompleted=true` is set in additional options.
- There is no "Get All Task Lists" operation in this node — hardcode or retrieve task list IDs via the HTTP Request node calling `tasks.googleapis.com/tasks/v1/users/@me/lists`.

**Source:** n8n-nodes-base.googletasks.md  [doc-verified]
