# Embeddings HuggingFace Inference — `n8n-nodes-langchain.embeddingsHuggingFaceInference`
**Type** `n8n-nodes-langchain.embeddingsHuggingFaceInference` · **ai · sub-node**
**What:** Generates text embeddings via HuggingFace Inference API or a custom self-hosted inference endpoint.
**Credentials:** `huggingFaceApi`.

**Key params & gotchas:**
- **Model**: Select or enter a HuggingFace model ID that supports the feature-extraction (embedding) task.
- **Custom Inference Endpoint** (option): URL of a self-hosted HuggingFace Inference Endpoint. When set, the **Model** field is ignored — the endpoint itself determines the model.
- Dimensions depend on the selected model — verify against your vector store index before first use.
- Free HuggingFace Inference API has rate limits and cold-start delays; use a dedicated endpoint for production.

**Source:** n8n-nodes-langchain.embeddingshuggingfaceinference.md  [doc-verified]
