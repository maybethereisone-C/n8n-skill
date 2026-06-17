# Embeddings Cohere — `n8n-nodes-langchain.embeddingsCohere`
**Type** `n8n-nodes-langchain.embeddingsCohere` · **ai · sub-node**
**What:** Generates text embeddings using Cohere's embedding models.
**Credentials:** `cohereApi`.

**Key params & gotchas:**
- **Model**: Three fixed options (dimensions in parens):
  - `Embed-English-v2.0` (4096)
  - `Embed-English-Light-v2.0` (1024)
  - `Embed-Multilingual-v2.0` (768)
- Vector store index dimensions must match the selected model's output dimensions — mismatch = insert failure.
- For non-English content, use the Multilingual model (768 dims).

**Source:** n8n-nodes-langchain.embeddingscohere.md  [doc-verified]
