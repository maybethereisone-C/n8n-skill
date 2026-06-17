# Embeddings Google Gemini — `n8n-nodes-langchain.embeddingsGoogleGemini`
**Type** `n8n-nodes-langchain.embeddingsGoogleGemini` · **ai · sub-node**
**What:** Generates text embeddings using Google Gemini embedding models via the Google AI API.
**Credentials:** `googleAiApi`.

**Key params & gotchas:**
- **Model**: Select from dynamically loaded list; check [Google Gemini models docs](https://ai.google.dev/models/gemini) for current embedding model IDs and dimensions.
- Dimensions vary by model — confirm they match your vector store index before first insert.

**Source:** n8n-nodes-langchain.embeddingsgooglegemini.md  [doc-verified]
