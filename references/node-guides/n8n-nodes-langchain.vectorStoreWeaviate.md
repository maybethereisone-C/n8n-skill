# Weaviate Vector Store — `n8n-nodes-langchain.vectorStoreWeaviate`
**Type** `n8n-nodes-langchain.vectorStoreWeaviate` · **ai**
**What:** Vector store backed by Weaviate; supports insert, similarity search, hybrid search, chain/tool retrieval, and agent-tool modes with optional multi-tenancy.
**Credentials:** `weaviateApi`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity (or hybrid) search |
| Insert Documents | Add docs to a Weaviate collection |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Weaviate Collection**: Name of the target collection. Must exist (node does not auto-create).
- **Embedding Batch Size** (Insert mode): Default 200. Tune down for large/rich documents to avoid timeouts.
- **Multi-tenancy**: Must be enabled at first ingestion by providing a `Tenant Name`. Cannot be toggled after collection creation. Multiple users sharing one workflow each need their own tenant to prevent history bleed.
- **Search Filters** (option): JSON object with `AND`/`OR` logic and operators like `Equal`, `Like`, `containsAny`, `greaterThan`, `isNull`, `withinGeoRange`. Operators are case-insensitive.
- **Hybrid search** options: `Query Text`, `Alpha` (1.0 = pure vector, 0.0 = pure keyword, default 0.5), `Fusion Type` (Relative Score or Ranked), `Auto Cut Limit`, `Query Properties` (weighted with `^`), `Max Vector Distance`.
- **Metadata Keys** (option): Limit which metadata properties are returned — reduces network overhead.
- **Clear Data** (Insert mode): Wipes entire collection or tenant before insert. Irreversible.
- `Include Metadata` option available on Get Many and As Tool modes.
- Timeout options (`Init Timeout`, `Insert Timeout`, `Query Timeout`) in seconds — increase for large collections or slow networks.
- `Skip Init Checks` disables connection-time health checks — use only if startup latency is a problem.

**Source:** n8n-nodes-langchain.vectorstoreweaviate.md  [doc-verified]
