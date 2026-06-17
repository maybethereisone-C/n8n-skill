# Embeddings OpenAI — `n8n-nodes-langchain.embeddingsOpenAi`
**Type** `n8n-nodes-langchain.embeddingsOpenAi` · **ai · sub-node**
**What:** Generates text embeddings using OpenAI embedding models (or compatible self-hosted endpoints).
**Credentials:** `openAiApi`.

**Key params & gotchas:**
- All configuration is in **Node options**:
  - **Model**: Select embedding model (e.g. `text-embedding-3-small` = 1536 dims, `text-embedding-3-large` = 3072 dims).
  - **Base URL**: Override to point at a self-hosted OpenAI-compatible endpoint (e.g. LM Studio, vLLM). When set, the credential API key still applies.
  - **Batch Size**: Max texts per request. Reduce on rate-limited accounts.
  - **Strip New Lines**: On by default.
  - **Timeout**: Seconds; `-1` = no timeout.
- Most widely used embedding node — the default for most n8n RAG templates.
- Vector store indexes built with one model cannot be queried with another (dimension mismatch); don't switch models after indexing.

**Source:** n8n-nodes-langchain.embeddingsopenai.md  [doc-verified]
