# Milvus Vector Store — `n8n-nodes-langchain.vectorStoreMilvus`
**Type** `n8n-nodes-langchain.vectorStoreMilvus` · **ai**
**What:** Vector store backed by Milvus; supports insert, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `milvusApi`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search with limit |
| Insert Documents | Add docs to a Milvus collection |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Milvus Collection**: Select or type collection name. Collection must exist in Milvus before use.
- **Clear Collection** (Insert mode option): Deletes all data before inserting. Irreversible.
- **Metadata Filter** (option): Key/value pairs for pre-query filtering.
- Agent-tool `Description` field directly influences when the agent decides to query this store — write it precisely.

**Source:** n8n-nodes-langchain.vectorstoremilvus.md  [doc-verified]
