# Embeddings Ollama — `n8n-nodes-langchain.embeddingsOllama`
**Type** `n8n-nodes-langchain.embeddingsOllama` · **ai · sub-node**
**What:** Generates text embeddings using a locally-running Ollama instance.
**Credentials:** `ollamaApi`.

**Key params & gotchas:**
- **Model**: Two listed options with fixed dimensions:
  - `all-minilm` — 384 dimensions
  - `nomic-embed-text` — 768 dimensions
  - Additional models from Ollama library can be entered manually.
- Vector store index dimensions must match the selected model's output — `all-minilm` (384) and `nomic-embed-text` (768) are not interchangeable with OpenAI 1536-dim indexes.
- Ollama server must be running and reachable at the configured credential URL.
- Ideal for fully local/offline RAG pipelines.

**Source:** n8n-nodes-langchain.embeddingsollama.md  [doc-verified]
