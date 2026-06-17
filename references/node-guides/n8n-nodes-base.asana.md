# Asana — `n8n-nodes-base.asana`
**Type** `n8n-nodes-base.asana` · **action**
**What:** Create and manage Asana projects, tasks, subtasks, comments, tags, and users.
**Credentials:** Asana OAuth2 or personal access token credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Project | Create, Delete, Get, Get All, Update |
| Subtask | Create, Get All |
| Task | Create, Delete, Get, Get All, Move, Search, Update |
| Task Comment | Add, Remove |
| Task Tag | Add, Remove |
| Task Project | Add to project, Remove from project |
| User | Get, Get All |

## Key params & gotchas
- **Breaking change:** Some ops broke on 2023-01-17 due to Asana API changes — requires n8n ≥ 1.22.2.
- Task **Workspace** or **Project** must be specified when creating tasks.
- "Move" task changes its position within a project section — requires section GID.
- "Search" uses Asana's task search API; supports filtering by assignee, project, completion status, and due date.
- Subtasks require the parent task GID; Get All subtasks takes a task GID.

**Source:** n8n-nodes-base.asana.md  [doc-verified]
