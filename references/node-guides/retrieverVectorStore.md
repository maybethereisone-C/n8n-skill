# Vector Store Retriever — `n8n-nodes-langchain.retrieverVectorStore`
**Type** `n8n-nodes-langchain.retrieverVectorStore` · **typeVersion** 1 · **ai**
**What:** Sub-node that wraps a vector store and exposes it as a retriever for AI Agents, chains, and advanced retriever nodes.
**Credentials:** none (delegates to attached vector store sub-node)
**Resources / Operations:** No discrete operations — bridges vector store to retriever interface.
**Key params & gotchas:**
- **Limit**: Maximum number of documents to return per query. Keep low (4–10) for prompt efficiency; too many results bloat the LLM context.
- Requires a **vector store** sub-node attached to it (e.g. Pinecone, Qdrant, Supabase Vector Store).
- This node is the standard way to connect a vector store to an AI Agent's retrieval tool — without it, the agent cannot query the store.
- Can be wrapped by MultiQuery Retriever or Contextual Compression Retriever for enhanced retrieval quality.
**Source:** n8n-nodes-langchain.retrievervectorstore.md  [doc-verified]
