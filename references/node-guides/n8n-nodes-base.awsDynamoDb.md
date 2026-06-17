# AWS DynamoDB — `n8n-nodes-base.awsDynamoDb`
**Type** `n8n-nodes-base.awsDynamoDb` · **action**
**What:** Create, read, update, and delete items in AWS DynamoDB tables.
**Credentials:** AWS credential (access key + secret, with DynamoDB permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Item | Create or update (upsert/put), Delete, Get, Get All |

## Key params & gotchas
- **Create/Update uses PutItem** — it replaces the entire item if the key exists, not a partial update. To patch specific attributes use the HTTP Request node with UpdateItem.
- **Table name** and **partition key value** are required for all single-item operations.
- "Get All" performs a Scan (full table scan) — expensive on large tables. Use with caution; prefer Query via HTTP Request for key-conditioned reads.
- DynamoDB attribute types must be specified (S=string, N=number, B=binary) — n8n handles this via the **Data Type** column in the expression UI.
- IAM permissions: `dynamodb:PutItem`, `dynamodb:GetItem`, `dynamodb:DeleteItem`, `dynamodb:Scan`.

**Source:** n8n-nodes-base.awsdynamodb.md  [doc-verified]
