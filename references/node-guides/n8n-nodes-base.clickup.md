# ClickUp — `n8n-nodes-base.clickup`
**Type** `n8n-nodes-base.clickup` · **action**
**What:** Full CRUD across ClickUp tasks, checklists, comments, folders, goals, lists, tags, time entries, and more.
**Credentials:** clickUpApi or clickUpOAuth2Api.

## Resources / Operations
| Resource | Operations |
|---|---|
| Checklist | Create, Delete, Update |
| Checklist Item | Create, Delete, Update |
| Comment | Create, Delete, Get All, Update |
| Folder | Create, Delete, Get, Get All, Update |
| Goal | Create, Delete, Get, Get All, Update |
| Goal Key Result | Create, Delete, Update |
| List | Create, Delete, Get, Get All, Get Members, Get Custom Fields, Update |
| Space Tag | Create, Delete, Get All, Update |
| Task | Create, Delete, Get, Get All, Get Members, Set Custom Field, Update |
| Task List | Add, Remove |
| Task Tag | Add, Remove |
| Task Dependency | Create, Delete |
| Time Entry | Create, Delete, Get, Get All, Start, Stop, Update |
| Time Entry Tag | Add, Get All, Remove |

## Key params & gotchas
- **Get a Task** has two optional toggles: `Include Subtasks` and `Include Markdown Description` (preserves links/rich formatting). Enable `Include Markdown Description` if your task descriptions contain hyperlinks.
- IDs (list ID, folder ID, space ID) are numeric strings — they must come from prior ClickUp node calls or be hardcoded; names are not accepted.
- `Set Custom Field` requires the field UUID, not its display name.
- `Start` / `Stop` time entry operations affect the currently running timer for the authenticated user only.
- Can be used as an AI tool node (supports `--8<-- ai-tools` flag).

**Source:** n8n-nodes-base.clickup.md  [doc-verified]
