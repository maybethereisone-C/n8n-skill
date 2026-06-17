# Embeddings Google PaLM — `n8n-nodes-langchain.embeddingsGooglePalm`
**Type** `n8n-nodes-langchain.embeddingsGooglePalm` · **ai · sub-node**
**What:** Generates text embeddings using Google PaLM embedding models via the Google AI API.
**Credentials:** `googleAiApi`.

**Key params & gotchas:**
- **Model**: Dynamically loaded from the Google PaLM API — only models available to your account appear. If the list is empty, check API enablement and account access.
- PaLM embedding models are distinct from Gemini models; use the Embeddings Google Gemini node for newer Gemini-family embedding models.

**Source:** n8n-nodes-langchain.embeddingsgooglepalm.md  [doc-verified]
