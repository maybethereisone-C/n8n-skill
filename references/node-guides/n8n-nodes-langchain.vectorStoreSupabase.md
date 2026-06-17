# Supabase Vector Store — `n8n-nodes-langchain.vectorStoreSupabase`
**Type** `n8n-nodes-langchain.vectorStoreSupabase` · **ai**
**What:** Vector store backed by Supabase (PostgreSQL + pgvector); supports insert, update, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `supabaseApi`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search with limit |
| Insert Documents | Add docs to a Supabase table |
| Update Documents | Update doc by ID |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Prerequisite**: Follow the [Supabase LangChain quickstart](https://supabase.com/docs/guides/ai/langchain?database-method=sql) to set up the table and matching SQL function before use. Deviating from defaults (table name, column names, function name) requires matching changes in the node options.
- **Table Name**: Supabase table with pgvector columns.
- **Query Name** (option): Name of the Supabase SQL function that performs the vector search. Default (from quickstart) is `match_documents`. Must match exactly or retrieval returns nothing.
- **Update Documents** mode requires the document `ID` field.
- **Metadata Filter** (option): Key/value filter applied server-side.

**Source:** n8n-nodes-langchain.vectorstoresupabase.md  [doc-verified]
