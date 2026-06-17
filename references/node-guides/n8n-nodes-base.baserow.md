# Baserow — `n8n-nodes-base.baserow`
**Type** `n8n-nodes-base.baserow` · **action**
**What:** Create, read, update, and delete rows in Baserow open-source database tables.
**Credentials:** Baserow credential (host URL + username/password or token).

## Resources / Operations
| Resource | Operations |
|---|---|
| Row | Create, Delete, Get, Get Many, Update (single row) |
| Row | Create multiple, Delete multiple, Update multiple (batch) |

## Key params & gotchas
- **Table ID** is required — find it in the Baserow URL (`/database/<id>/table/<table_id>/`).
- Batch operations (Create/Delete/Update multiple) reduce API calls significantly for bulk work.
- "Get Many" supports filtering, sorting, and search — use the **Filters** option for server-side filtering.
- Field names in payloads must exactly match column names in Baserow; mismatches are silently ignored.
- Self-hosted Baserow: set the host URL in the credential to your instance URL.

**Source:** n8n-nodes-base.baserow.md  [doc-verified]
