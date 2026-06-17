# Oracle Database Vector Store — `n8n-nodes-langchain.vectorStoreOracleDB`
**Type** `n8n-nodes-langchain.vectorStoreOracleDB` · **ai**
**What:** Vector store backed by Oracle Database AI Vector Search; supports insert, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `oracleDb`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search from a table |
| Insert Documents | Add docs to an Oracle vector table |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Prerequisite**: Oracle Database must support Oracle AI Vector Search (23ai or patched 19c/21c).
- **Table Name**: Node auto-creates the vector table if it doesn't exist.
- **Distance Strategy** (option): Cosine, Inner Product, Euclidean, Manhattan, Euclidean Squared, Hamming — must match what your data was indexed with.
- **Metadata Filter**: Supports rich operators (`$gte`, `$nin`, `$and`, nested objects) beyond simple key/value; multiple UI fields = AND query.
- Metadata is set via the document loader at insert time.

**Source:** n8n-nodes-langchain.vectorstoreoracledb.md  [doc-verified]
