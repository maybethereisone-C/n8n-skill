# Postgres — `n8n-nodes-base.postgres`
**Type** `n8n-nodes-base.postgres` · **action**
**What:** Execute SQL queries and perform row-level CRUD operations on a PostgreSQL database.
**Credentials:** `postgres`

## Resources / Operations
| Operation | Description |
|-----------|-------------|
| Delete | Delete entire table (Truncate/Drop) or matching rows |
| Execute Query | Run arbitrary SQL with optional query parameters |
| Insert | Insert rows; manual or auto column mapping |
| Insert or Update | Upsert rows into a table |
| Select | Select rows with optional filter, sort, and limit |
| Update | Update rows matching conditions |

## Key params & gotchas
- Supports use as an AI tool node.
- **Query Batching** options: `Single Query` (all items in one call), `Independently` (one query per item), `Transaction` (all-or-nothing rollback on failure). Choose `Transaction` for atomic bulk operations.
- **Output Large-Format Numbers As → Text** is critical when columns contain `NUMERIC` or `BIGINT` values > 16 digits — JavaScript's float64 will silently corrupt them otherwise.
- **Execute Query → Query Parameters**: Use `$1`, `$2` tokens and the **Query Parameters** field (comma-separated or expression returning an array) to build safe prepared statements that prevent SQL injection. Example: `SELECT * FROM $1:name WHERE email = $2` with params `{{ ['users', $json.email] }}`.
- **Delete → Truncate → Restart Sequences**: resets auto-increment counters. Use with care in production.
- **Delete → Drop**: permanently removes table structure — irreversible.
- **Skip on Conflict** (Insert): silently ignores unique/exclusion constraint violations instead of erroring.
- **Replace Empty Strings with NULL**: useful when piping spreadsheet exports where empty cells arrive as `""`.
- Schema and table can be selected from a list or entered by name (useful with expressions).
- A companion trigger node (`n8n-nodes-base.postgresTrigger`) is available for change-data-capture workflows.

**Source:** n8n-nodes-base.postgres/index.md  [doc-verified]
