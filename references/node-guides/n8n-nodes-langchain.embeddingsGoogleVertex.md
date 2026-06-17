# Embeddings Google Vertex — `n8n-nodes-langchain.embeddingsGoogleVertex`
**Type** `n8n-nodes-langchain.embeddingsGoogleVertex` · **ai · sub-node**
**What:** Generates text embeddings using Google Vertex AI embedding models (service-account auth).
**Credentials:** `googleServiceAccount`.

**Key params & gotchas:**
- **Model**: Select from dynamically loaded Vertex AI embedding models. See [Vertex AI text embeddings API docs](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api) for current model names and dimension specs.
- Uses Google Service Account credentials (not the `googleAiApi` key used by Gemini/PaLM nodes) — ensure the SA has the `Vertex AI User` IAM role.
- Dimensions must match your vector store index configuration.

**Source:** n8n-nodes-langchain.embeddingsgooglevertex.md  [doc-verified]
