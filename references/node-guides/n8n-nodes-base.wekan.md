# Wekan — `n8n-nodes-base.wekan`
**Type** `n8n-nodes-base.wekan` · **typeVersion** 1 · **action**
**What:** Manage boards, cards, checklists, and lists in the self-hosted Wekan kanban tool.
**Credentials:** `wekanApi` (username + password + host URL).

## Resources / Operations
| Resource | Operations |
|---|---|
| Board | Create, Delete, Get, Get All (user boards) |
| Card | Create, Delete, Get, Get All, Update |
| Card Comment | Create, Delete, Get, Get All |
| Checklist | Create, Delete, Get, Get All (for card) |
| Checklist Item | Delete, Get, Update |
| List | Create, Delete, Get, Get All (board lists) |

## Key params & gotchas
- **Admin permissions required** to load Author ID, Board ID, and other dynamic parameters via the dropdown loaders. If dropdowns are empty, grant the API user admin role in Wekan settings.
- Card operations require both a `boardId` and a `listId` — provide them in the correct order or the card won't be found.
- Checklist Item has no Create — items are added during Checklist Create; use Update/Delete afterwards.

**Source:** n8n-nodes-base.wekan.md  [doc-verified]
