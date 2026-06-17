# Redis Vector Store — `n8n-nodes-langchain.vectorStoreRedis`
**Type** `n8n-nodes-langchain.vectorStoreRedis` · **ai**
**What:** Vector store backed by Redis Query Engine (RediSearch); supports insert, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `redis`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search from Redis index |
| Insert Documents | Add docs to a Redis vector index |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Prerequisite**: Redis must have the Query Engine enabled — Redis OSS ≥ 8.0, Redis Cloud, or Redis Software. Standard Redis without the module will fail.
- **Redis Index**: Node auto-creates a new index if one doesn't exist. Only pre-create if you need a custom schema.
- **Metadata Filter** (option): OR semantics — at least one filter field must match (unlike most other vector stores that use AND). Critical distinction.
- **Redis Configuration Options** (option): Customize `Metadata Key`, `Key Prefix`, `Content Key`, `Embedding Key` — must match your existing index schema if reusing one.
- **Insert Options**:
  - `Overwrite Documents`: Also deletes and recreates the index — use with care.
  - `Time-to-Live`: Expires individual documents (not the index).
- **Include Metadata** (option): Available on Get Many and As Tool modes; toggle to include/exclude metadata in results.

**Source:** n8n-nodes-langchain.vectorstoreredis.md  [doc-verified]
