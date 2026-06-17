# Embeddings Mistral Cloud — `n8n-nodes-langchain.embeddingsMistralCloud`
**Type** `n8n-nodes-langchain.embeddingsMistralCloud` · **ai · sub-node**
**What:** Generates text embeddings using Mistral AI cloud embedding models.
**Credentials:** `mistralCloudApi`.

**Key params & gotchas:**
- **Model**: Select from Mistral embedding models (e.g. `mistral-embed`).
- **Batch Size** (option): Max documents per API request — reduce if hitting rate limits.
- **Strip New Lines** (option): On by default — removes `\n`. Disable only if newlines carry semantic meaning in your documents.
- Mistral embedding dimensions are fixed per model — confirm match with vector store index.

**Source:** n8n-nodes-langchain.embeddingsmistralcloud.md  [doc-verified]
