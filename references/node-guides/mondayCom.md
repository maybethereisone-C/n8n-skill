# monday.com — `n8n-nodes-base.mondayCom`
**Type** `n8n-nodes-base.mondayCom` · **typeVersion** 1 · **action**
**What:** Automate monday.com boards: manage boards, columns, groups, and items (work items/rows).
**Credentials:** monday.com API token (`mondayComApi`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Board | Archive, Create, Get, Get All |
| Board Column | Create, Get All |
| Board Group | Create, Delete, Get List |
| Board Item | Add update, Change column value, Change multiple column values, Create, Delete, Get, Get All, Get by column value, Move to group |

**Key params & gotchas:**
- Requires n8n **v1.22.6 or above**.
- **Change column value** / **Change multiple column values** accept JSON-encoded column value objects matching monday.com's column API format (e.g., `{"text": "value"}` for text columns, `{"date": "2024-01-15"}` for date columns).
- **Get items by column value** is useful for lookups but requires the column ID (not display name).
- Board Item "Add update" posts a text update (comment) to an existing item's activity log.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.mondaycom.md  [doc-verified]
