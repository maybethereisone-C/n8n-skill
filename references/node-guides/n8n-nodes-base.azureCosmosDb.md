# Azure Cosmos DB — `n8n-nodes-base.azureCosmosDb`
**Type** `n8n-nodes-base.azureCosmosDb` · **action**
**What:** Create, query, and manage containers and items in Azure Cosmos DB (NoSQL API).
**Credentials:** Azure Cosmos DB credential (account URI + key, or Azure AD).

## Resources / Operations
| Resource | Operations |
|---|---|
| Container | Create, Delete, Get, Get Many |
| Item | Create, Delete, Get, Get Many, Execute Query, Update |

## Key params & gotchas
- **Item/Execute Query:** Uses Cosmos DB SQL syntax. Use `$1`, `$2`… as positional placeholders — n8n converts these to `@Param1`, `@Param2` before sending. Example: `SELECT * FROM c WHERE c.status = $1`.
- **Query Parameters vs Query Parameters (JSON):** Plain Query Parameters sends all values as strings — Cosmos DB does type-sensitive comparisons, so `WHERE c.count = $1` with value `"5"` won't match a stored number `5`. Use Query Parameters (JSON) `[5]` to preserve numeric types.
- **Integers > Number.MAX_SAFE_INTEGER** lose precision in JSON — known limitation of Query Parameters (JSON).
- **Simplify** option (default on) strips internal `_` prefixed metadata fields from returned items.
- Container operations require the database ID; item operations require both database ID and container ID.

**Source:** n8n-nodes-base.azurecosmosdb.md  [doc-verified]
