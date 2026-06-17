# PGVector Vector Store — `n8n-nodes-langchain.vectorStorePGVector`
**Type** `n8n-nodes-langchain.vectorStorePGVector` · **ai**
**What:** Vector store backed by the pgvector PostgreSQL extension; supports insert, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `postgres`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search from a PG table |
| Insert Documents | Add docs to a PGVector table |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Table name**: Required in all modes; must exist with pgvector extension enabled.
- **Collection** (option): Logical dataset separation within a table using an extra column + a separate tracking table (`Collection Table Name`). Useful for multi-tenant setups.
- **Column Names** (option): Override default column names for ID, vector, content, and metadata fields. Must match your actual schema if it differs from defaults.
- **Metadata Filter** (option): Key/value filter applied server-side.
- Ensure `CREATE EXTENSION IF NOT EXISTS vector;` is run on your Postgres database before first use.

**Source:** n8n-nodes-langchain.vectorstorepgvector.md  [doc-verified]
