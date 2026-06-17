# Zep Vector Store — `n8n-nodes-langchain.vectorStoreZep`
**Type** `n8n-nodes-langchain.vectorStoreZep` · **ai**
**What:** Vector store backed by Zep; supports insert, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `zepApi`.

> **Deprecated** — will be removed in a future n8n version. Migrate to an alternative vector store.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search with limit |
| Insert Documents | Add docs to a Zep collection |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Collection Name**: Required in all modes.
- **Embedding Dimensions** (option): Must match between insert and query — changing dimensions after initial insert is not supported.
- **Is Auto Embedded** (Insert mode, default on): n8n handles embedding. Disable to use Zep's own embedding pipeline instead.
- **Metadata Filter** (option): Key/value filter.

**Source:** n8n-nodes-langchain.vectorstorezep.md  [doc-verified]
