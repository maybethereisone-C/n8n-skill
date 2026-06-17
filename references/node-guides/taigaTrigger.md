# Taiga Trigger — `n8n-nodes-base.taigaTrigger`
**Type** `n8n-nodes-base.taigaTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Taiga project management events (sprints, user stories, tasks, issues, etc.) via webhook.
**Credentials:** `taigaApi` (username + password + server URL for self-hosted).
**Resources / Operations:**
| Object | Events |
|---|---|
| Epic | Created / Changed / Deleted |
| Issue | Created / Changed / Deleted |
| Milestone (Sprint) | Created / Changed / Deleted |
| Task | Created / Changed / Deleted |
| User Story | Created / Changed / Deleted |
| Wiki Page | Created / Changed / Deleted |

**Key params & gotchas:**
- Trigger type: **webhook** — Taiga pushes change notifications to n8n's webhook URL.
- Supports both Taiga cloud (`https://api.taiga.io`) and self-hosted instances; set the server URL in credentials accordingly.
- The webhook payload includes a `change` object describing what field changed and its old/new values — useful for filtering downstream.

**Source:** n8n-nodes-base.taigatrigger.md  [doc-verified]
