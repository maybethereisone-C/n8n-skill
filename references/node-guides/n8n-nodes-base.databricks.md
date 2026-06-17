# Databricks — `n8n-nodes-base.databricks`
**Type** `n8n-nodes-base.databricks` · **action**
**What:** Execute Databricks SQL queries, manage Unity Catalog objects, interact with Genie AI conversations, query ML model serving endpoints, and work with vector search indexes.
**Credentials:** databricksApi (host URL + personal access token or OAuth).

## Resources / Operations
| Resource | Operations |
|---|---|
| Databricks SQL | Execute Query |
| File (DBFS) | Create Dir, Delete Dir, Delete File, Download File, Get Metadata, List Dir, Upload File |
| Genie | Create Conversation Message, Execute Message SQL, Get Conversation Message, Get Genie Space, Get Query Results, Start Conversation |
| Model Serving | Query Endpoint |
| Unity Catalog | Create/Delete/Get/List/Update Catalog; Create/Delete/Get/List Function; Get/List Table; Create/Delete/Get/List/Update Volume |
| Vector Search | Create Index, Get Index, List Indexes, Query Index |

## Key params & gotchas
- **SQL Execute Query** runs against a SQL Warehouse — requires the Warehouse ID (not cluster ID).
- **Genie** operations enable conversational SQL generation; Start Conversation first, then Create Conversation Message, poll with Get Conversation Message until complete, then Execute Message SQL to run the generated query.
- **Model Serving Query Endpoint** sends a JSON payload to a registered model endpoint; shape the input to match the model's input schema.
- **Vector Search Query Index** requires the index name and a query vector (array of floats); `num_results` controls how many nearest neighbors are returned.
- Can be used as an AI tool node.
- "Operation not supported" error is plan/feature-gated.

**Source:** n8n-nodes-base.databricks.md  [doc-verified]
