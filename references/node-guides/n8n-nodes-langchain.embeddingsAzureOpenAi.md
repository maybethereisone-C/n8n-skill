# Embeddings Azure OpenAI — `n8n-nodes-langchain.embeddingsAzureOpenAi`
**Type** `n8n-nodes-langchain.embeddingsAzureOpenAi` · **ai · sub-node**
**What:** Generates text embeddings using Azure-hosted OpenAI embedding models.
**Credentials:** `azureOpenAiApi`.

**Key params & gotchas:**
- All configuration is under **Node options** (no required top-level params):
  - **Model (Deployment) Name**: Must match the deployment name in Azure OpenAI Studio, not the model name.
  - **Batch Size**: Number of texts per API call. Reduce if hitting rate limits.
  - **Strip New Lines**: On by default — removes `\n` from input. Disable only if newlines are semantically meaningful.
  - **Timeout**: Seconds before aborting. `-1` = no timeout.
- Deployment name ≠ model name is the most common misconfiguration.

**Source:** n8n-nodes-langchain.embeddingsazureopenai.md  [doc-verified]
