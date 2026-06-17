# Reranker Cohere — `n8n-nodes-langchain.rerankerCohere`
**Type** `n8n-nodes-langchain.rerankerCohere` · **typeVersion** 1 · **ai**
**What:** Sub-node that reranks documents retrieved from a vector store using Cohere's reranking models, improving relevance ordering before passing to the LLM.
**Credentials:** `cohereApi`
**Resources / Operations:** No discrete operations — post-processes vector store retrieval results.
**Key params & gotchas:**
- **Model**: Choose from Cohere's rerank model family (e.g. `rerank-english-v3.0`, `rerank-multilingual-v3.0`).
- Connects to a vector store retriever node; outputs a reordered list of documents sorted by descending relevance to the query.
- Adds a Cohere API call per retrieval — increases latency and cost; most valuable when the vector store returns many low-quality candidates.
- Use when semantic similarity alone (cosine/dot product) produces poor ranking for your domain.
**Source:** n8n-nodes-langchain.rerankercohere.md  [doc-verified]
