# Snowflake — `n8n-nodes-base.snowflake`
**Type** `n8n-nodes-base.snowflake` · **typeVersion** 1 · **action**
**What:** Execute SQL queries and insert/update rows in a Snowflake data warehouse.
**Credentials:** `snowflakeOAuth2Api` (also supports username/password credentials)
**Resources / Operations:**
| Operation |
|---|
| Execute Query (raw SQL) |
| Insert rows in database |
| Update rows in database |

**Key params & gotchas:**
- `authentication` param selects credentials vs OAuth2 — mismatch causes silent auth failures.
- For Insert/Update, `columns` is a comma-separated string of column names, not an array.
- Update requires an `updateKey` (default `id`) — the key column must be in the data.
- Execute Query returns results as items; large result sets are not paginated automatically.

**Source:** n8n-nodes-base.snowflake.md  [doc-verified]
