# Vector Store Question Answer Tool — `@n8n/n8n-nodes-langchain.toolVectorStore`

**Type** `@n8n/n8n-nodes-langchain.toolVectorStore` · **typeVersion** 1 · **ai**

**What:** AI tool sub-node that lets an agent query a connected vector store and get summarized answers from retrieved chunks.

**Credentials:** None directly — credentials are on the Vector Store sub-node connected to this node's input.

**Resources / Operations:**

| Parameter | Detail |
|-----------|--------|
| Description of Data | Free-text describing what's in the vector store (shapes agent's decision to use this tool) |
| Limit | Max number of chunks to retrieve |

**Key params & gotchas:**
- **Node name matters**: n8n builds the tool description as `"Useful for when you need to answer questions about [node name]…"`. Rename the node to something descriptive (e.g. "ProductDocs").
- **Avoid special characters** in the node name — they cause runtime agent errors. Use only alphanumerics, spaces, dashes, underscores.
- Spaces in the node name become underscores in the tool description seen by the LLM.
- The connected Vector Store sub-node (Pinecone, Qdrant, Supabase, etc.) must also be configured with its own credentials.
- Sub-node — connect to AI Agent's Tools input; also requires a Vector Store node connected to its own input.

**Source:** n8n-nodes-langchain.toolvectorstore.md  [doc-verified]
