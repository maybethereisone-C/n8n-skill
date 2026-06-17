# MultiQuery Retriever — `n8n-nodes-langchain.retrieverMultiQuery`
**Type** `n8n-nodes-langchain.retrieverMultiQuery` · **typeVersion** 1 · **ai**
**What:** Sub-node that generates multiple rephrased versions of a user query using an LLM, retrieves documents for each, and merges deduplicated results — improving recall from vector stores.
**Credentials:** none (delegates to attached LLM and vector store retriever sub-nodes)
**Resources / Operations:** No discrete operations — enhances retrieval quality.
**Key params & gotchas:**
- **Query Count**: How many query variants to generate. More variants = higher recall but more LLM calls and latency.
- Requires two sub-node connections: an **LLM** (for query generation) and a **vector store retriever**.
- Deduplication is automatic — the same document won't appear multiple times in the merged result.
- Most valuable when a single query phrasing misses relevant documents due to vocabulary mismatch.
**Source:** n8n-nodes-langchain.retrievermultiquery.md  [doc-verified]
