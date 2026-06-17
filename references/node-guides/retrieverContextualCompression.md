# Contextual Compression Retriever — `n8n-nodes-langchain.retrieverContextualCompression`
**Type** `n8n-nodes-langchain.retrieverContextualCompression` · **typeVersion** 1 · **ai**
**What:** Sub-node that wraps a vector store retriever and compresses/filters retrieved documents using the query context before passing them to the LLM.
**Credentials:** none (delegates to attached retriever and LLM sub-nodes)
**Resources / Operations:** No discrete operations — post-processes retrieval results.
**Key params & gotchas:**
- Requires two sub-node connections: a **vector store retriever** and an **LLM** (used for compression).
- The LLM extracts only the relevant portions of each retrieved document — reduces token usage in the prompt context.
- Adds one LLM call per retrieval cycle — trade-off: lower context tokens vs. extra latency/cost.
- Most effective when documents are long and only small excerpts are relevant to the query.
**Source:** n8n-nodes-langchain.retrievercontextualcompression.md  [doc-verified]
