# SeaTable — `n8n-nodes-base.seatable`
**Type** `n8n-nodes-base.seatable` · **action**
**What:** CRUD operations on rows in SeaTable (collaborative spreadsheet/database).
**Credentials:** `seatableApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Row | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- SeaTable credential requires an API token scoped to a specific base (workspace); the token grants access to all tables in that base.
- Table name must match exactly (case-sensitive) as defined in SeaTable.
- Row ID is SeaTable's internal `_id` field (a UUID string) — required for Get, Update, Delete.
- Get All supports filtering and sorting; use Return All or set a Limit.
- Column types (date, link, formula) may require specific value formats — check SeaTable column settings.

**Source:** n8n-nodes-base.seatable.md  [doc-verified]
