# Simple Vector Store — `n8n-nodes-langchain.vectorStoreInMemory`
**Type** `n8n-nodes-langchain.vectorStoreInMemory` · **ai**
**What:** In-app memory vector store for development/prototyping; data is not persisted across restarts.
**Credentials:** None.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search from memory key |
| Insert Documents | Write to a named memory key |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Development use only** — n8n explicitly warns against production use.
- **Data is not persistent**: lost on restart and may be purged under memory pressure.
- **Memory keys are global** across the entire instance — any user/workflow with the key can read the data. Do not store sensitive information.
- **Clear Store** (Insert mode): Wipes the key before inserting. Useful for rebuild-on-trigger patterns, dangerous if multiple workflows share a key.
- **n8n Cloud limits**: 100 MB max / 7-day TTL via `N8N_VECTOR_STORE_MAX_MEMORY` and `N8N_VECTOR_STORE_TTL_HOURS`. Self-hosted defaults to unlimited (-1).
- Prefer Pinecone/PGVector/Supabase for any workflow that must survive a restart.

**Source:** n8n-nodes-langchain.vectorstoreinmemory.md  [doc-verified]
