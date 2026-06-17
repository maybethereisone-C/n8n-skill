# MongoDB Atlas Vector Store — `n8n-nodes-langchain.vectorStoreMongoDBAtlas`
**Type** `n8n-nodes-langchain.vectorStoreMongoDBAtlas` · **ai**
**What:** Vector store backed by MongoDB Atlas Vector Search; supports insert, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `mongoDb`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search |
| Insert Documents | Add docs to a collection |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Prerequisite**: A Vector Search index must be manually created in MongoDB Atlas before use — the node does NOT auto-create it. Create via Atlas UI with `"type": "vector"` and set `numDimensions` to match your embedding model (e.g. `1536` for OpenAI `text-embedding-3-small`).
- Required fields in every mode: **Mongo Collection**, **Vector Index Name**, **Embedding Field**, **Metadata Field** — all must match the Atlas index schema exactly.
- **Metadata Filter** (option): Key/value filter applied before returning results.
- Dimension mismatch between embedding model and Atlas index = insert failure.

**Source:** n8n-nodes-langchain.vectorstoremongodbatlas.md  [doc-verified]
