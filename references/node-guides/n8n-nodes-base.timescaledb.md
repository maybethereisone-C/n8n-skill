# TimescaleDB — `n8n-nodes-base.timescaledb`
**Type** `n8n-nodes-base.timescaledb` · **typeVersion** 1 · **action**
**What:** Execute SQL queries and insert/update rows in TimescaleDB (PostgreSQL time-series extension).
**Credentials:** `timescaleDb`
**Resources / Operations:**
| Operation |
|---|
| Execute SQL Query |
| Insert rows in database |
| Update rows in database |

**Key params & gotchas:**
- To specify a column's data type explicitly, append `:type` to the column name in the **Columns** field: e.g. `id:int,name:text`. Required when TimescaleDB cannot infer type from value.
- TimescaleDB hypertables behave like regular tables for INSERT/UPDATE; chunk management is automatic.
- For time-series queries, use Execute SQL with `time_bucket()` and other TimescaleDB functions.

**Source:** n8n-nodes-base.timescaledb.md  [doc-verified]
