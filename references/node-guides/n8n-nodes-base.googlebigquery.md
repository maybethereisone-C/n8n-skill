# Google BigQuery — `n8n-nodes-base.googleBigQuery`
**Type** `n8n-nodes-base.googleBigQuery` · **typeVersion** 2 · **action**
**What:** Executes SQL queries against BigQuery and inserts rows into tables.
**Credentials:** `googleBigQueryOAuth2Api` (OAuth2) or `googleApi` (service account — preferred for automation).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| (top-level) | Execute Query |
| (top-level) | Insert |

**Key params & gotchas:**
- **Execute Query**: runs a standard SQL query; use `projectId` + full `dataset.table` references in SQL. Results are paginated — set "Return All" or provide a page size.
- **Insert**: streams rows into a table; requires `projectId`, `datasetId`, `tableId`. Streaming inserts have eventual-consistency — rows may not appear in queries immediately (usually seconds, but can be minutes).
- Service account must have `bigquery.jobs.create` and appropriate dataset-level permissions; OAuth2 inherits the authenticated user's IAM roles.
- Long-running queries: BigQuery runs them async; the node polls until completion. Very large queries may hit n8n's execution timeout — use scheduled exports for massive datasets instead.
- Insert does NOT support DML (UPDATE/DELETE); use Execute Query for those.

**Minimal example — query:**
```json
{
  "resource": "query",
  "operation": "executeQuery",
  "projectId": "my-project",
  "sqlQuery": "SELECT id, name FROM `my-project.my_dataset.users` LIMIT 100"
}
```

**Source:** n8n-nodes-base.googlebigquery.md  [doc-verified]
