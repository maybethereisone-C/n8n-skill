# Clockify — `n8n-nodes-base.clockify`
**Type** `n8n-nodes-base.clockify` · **action**
**What:** Manage Clockify projects, tags, tasks, and time entries.
**Credentials:** clockifyApi (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Project | Create, Delete, Get, Get All, Update |
| Tag | Create, Delete, Get All, Update |
| Task | Create, Delete, Get, Get All, Update |
| Time Entry | Create, Delete, Get, Update |

## Key params & gotchas
- All operations require a **Workspace ID** — select it from the dropdown (populated from credentials).
- Time entries need ISO 8601 start/end times; an open-ended entry (no end) represents a running timer.
- "Operation not supported" can appear if the Clockify plan doesn't include the feature (e.g., tasks require paid plan).

**Source:** n8n-nodes-base.clockify.md  [doc-verified]
