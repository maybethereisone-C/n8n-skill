# Qdrant Vector Store — `n8n-nodes-langchain.vectorStoreQdrant`
**Type** `n8n-nodes-langchain.vectorStoreQdrant` · **ai**
**What:** Vector store backed by Qdrant; supports insert, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `qdrantApi`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search with limit |
| Insert Documents | Add docs to a Qdrant collection |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Qdrant collection name**: Must exist in Qdrant (or be auto-created — depends on Qdrant server config).
- **Collection Config** (Insert mode option): JSON payload for Qdrant collection creation parameters (vector size, distance metric). Only used when the node creates the collection. Refer to Qdrant Collections docs for the schema.
- **Metadata Filter** (option): Key/value filter. Multiple entries = AND query. Available in Get Many and both Retrieve modes.
- No built-in update mode — to update a doc, re-insert with the same ID or delete + re-insert.

**Source:** n8n-nodes-langchain.vectorstoreqdrant.md  [doc-verified]
