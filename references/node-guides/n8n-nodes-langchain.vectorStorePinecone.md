# Pinecone Vector Store — `n8n-nodes-langchain.vectorStorePinecone`
**Type** `n8n-nodes-langchain.vectorStorePinecone` · **ai**
**What:** Vector store backed by Pinecone; supports insert, update, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `pineconeApi`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search with score |
| Insert Documents | Add docs to a Pinecone index |
| Update Documents | Update doc by ID |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Pinecone Index**: Select from fetched list or enter name. Index must already exist in Pinecone (node does not auto-create).
- **Pinecone Namespace** (option): Sub-partition within an index for logical isolation. Leave blank to use the default namespace.
- **Clear Namespace** (Insert mode option): Deletes all docs in the namespace before inserting. Irreversible — use with caution.
- **Metadata Filter** (option): Key/value filter applied server-side.
- Index dimensions must match the embedding model's output dimension — mismatch causes insert failure.
- Find your index name and namespace in the Pinecone console under the Indexes tab.

**Source:** n8n-nodes-langchain.vectorstorepinecone.md  [doc-verified]
