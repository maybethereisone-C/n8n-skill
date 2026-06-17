# Chroma Vector Store — `n8n-nodes-langchain.vectorStoreChroma`
**Type** `n8n-nodes-langchain.vectorStoreChroma` · **ai**
**What:** Vector store backed by Chroma; supports insert, similarity search, chain/tool retrieval, and agent-tool modes.
**Credentials:** `chromaApi`.

**Resources / Operations:**
| Mode | Description |
|------|-------------|
| Get Many | Similarity search with score |
| Insert Documents | Add docs to a Chroma collection |
| Retrieve Documents (As Vector Store for Chain/Tool) | Connect to retriever/chain |
| Retrieve Documents (As Tool for AI Agent) | Expose as named tool to agent |

**Key params & gotchas:**
- **Chroma collection name**: Select from fetched list or enter manually. Collection must exist unless the Chroma server auto-creates on insert.
- **Metadata Filter** (option, Get Many + Retrieve modes): Key/value pairs filtered server-side before returning results.
- Agent-tool mode requires `Description` — be specific so the LLM knows when to invoke it.

**Source:** n8n-nodes-langchain.vectorstorechroma.md  [doc-verified]
