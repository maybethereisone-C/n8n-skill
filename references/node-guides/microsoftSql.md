# Microsoft SQL — `n8n-nodes-base.microsoftSql`
**Type** `n8n-nodes-base.microsoftSql` · **typeVersion** 1 · **action**
**What:** Execute queries and perform CRUD operations against a Microsoft SQL Server (T-SQL) database.
**Credentials:** Microsoft SQL (`microsoftSqlApi`) — host, port, database, username, password (+ TLS options).
**Resources / Operations:**
| Operation |
|---|
| Execute SQL query |
| Insert rows |
| Update rows |
| Delete rows |

**Key params & gotchas:**
- **Execute SQL** accepts any T-SQL including stored procedure calls (`EXEC`), multi-statement batches, and DDL.
- Insert/Update/Delete are structured helpers that build parameterized queries — safer than string-concatenation in Execute SQL.
- Uses the `mssql` Node.js driver; connection pool is managed per-workflow execution.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.microsoftsql.md  [doc-verified]
