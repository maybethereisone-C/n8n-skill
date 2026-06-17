# CrateDB — `n8n-nodes-base.cratedb`
**Type** `n8n-nodes-base.cratedb` · **action**
**What:** Execute SQL queries and insert/update rows in CrateDB (distributed SQL database).
**Credentials:** crateDb (host, port, user, password, database).

## Resources / Operations
| Operation |
|---|
| Execute SQL query |
| Insert rows in database |
| Update rows in database |

## Key params & gotchas
- **Column type annotation:** Append `:type` to column names when inserting/updating to specify CrateDB types. Example: `id:int,name:text`. Without this, the node infers types and may choose wrong ones.
- **Execute query** accepts raw SQL strings — use `${{ $json.value }}` expressions carefully to avoid SQL injection in dynamic workflows.
- CrateDB uses PostgreSQL wire protocol; credentials are the same shape as Postgres.

**Source:** n8n-nodes-base.cratedb.md  [doc-verified]
