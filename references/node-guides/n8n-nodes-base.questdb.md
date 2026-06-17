# QuestDB — `n8n-nodes-base.questdb`
**Type** `n8n-nodes-base.questdb` · **action**
**What:** Execute SQL queries and insert rows into a QuestDB time-series database.
**Credentials:** `questDb`

## Resources / Operations
| Operation |
|-----------|
| Execute a SQL query |
| Insert rows in database |

## Key params & gotchas
- QuestDB uses PostgreSQL wire protocol; credential setup mirrors Postgres (host, port, user, password, database).
- **Column type annotation**: when inserting, append `:type` to column names in the Columns field to specify QuestDB types (e.g., `id:int,name:text,ts:timestamp`). Without this, QuestDB infers types which may be incorrect for timestamps or ints.
- QuestDB is append-optimized — use Insert for time-series ingestion; UPDATE/DELETE are limited in QuestDB semantics.
- Timestamp columns must be in microseconds or nanoseconds — n8n Date expressions may need explicit conversion.

**Source:** n8n-nodes-base.questdb.md  [doc-verified]
