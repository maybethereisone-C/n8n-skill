# Azure AI Search Vector Store — `n8n-nodes-langchain.vectorStoreAzureAiSearch`
**Type** `n8n-nodes-langchain.vectorStoreAzureAiSearch` · **ai**
**What:** Vector store backed by Azure AI Search (formerly Cognitive Search); supports insert, retrieval, and agent-tool modes with hybrid/semantic search.
**Credentials:** `azureAiSearchApi` (admin key for writes, query key for read-only).

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search; returns docs + scores |
| Insert Documents | Batch-upload embeddings (auto-creates index if absent) |
| Update Documents | Update existing docs by ID |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connects to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Exposes as named tool to agent |

**Key params & gotchas:**
- **Endpoint**: Must be `https://<service>.search.windows.net` — wrong format = connection error.
- **Index auto-creation**: On first insert, node creates index with HNSW cosine + 1536-dim vector field. If your embedding model outputs different dimensions, pre-create the index with the correct `vectorSearchDimensions` or inserts will fail.
- **Query Mode** (option): `Vector` (pure semantic), `Keyword` (BM25), `Hybrid` (default, RRF fusion), `Semantic Hybrid` (needs semantic configuration in index).
- **Semantic reranking** requires a semantic configuration defined in the Azure index; set `Semantic Configuration` option to match.
- **OData Filter** syntax: metadata fields use `metadata/<fieldName>` prefix (e.g. `metadata/source eq 'docs'`). Filtered fields must be marked `filterable` in the index schema.
- **Batch Size** (insert): Controls upload batching only — embedding batching is set in the embeddings sub-node.
- Admin API key required for inserts; query key sufficient for reads.

**Source:** n8n-nodes-langchain.vectorstoreazureaisearch.md  [doc-verified]
