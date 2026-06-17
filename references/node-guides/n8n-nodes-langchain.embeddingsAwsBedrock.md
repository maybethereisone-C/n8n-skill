# Embeddings AWS Bedrock — `n8n-nodes-langchain.embeddingsAwsBedrock`
**Type** `n8n-nodes-langchain.embeddingsAwsBedrock` · **ai · sub-node**
**What:** Generates text embeddings using AWS Bedrock foundation models; connects to vector store or summarization nodes.
**Credentials:** `aws` (IAM access key) or `awsAssumeRole` (temporary role).

**Key params & gotchas:**
- **Authentication**: Choose IAM or Assume Role — select matching credential type.
- **Model**: If dropdown is empty, the IAM role lacks `bedrock:ListFoundationModels` permission. Switch field to Expression mode and enter the model ID directly (e.g. `amazon.titan-embed-text-v2:0`).
- Embedding dimensions vary by model — ensure they match your vector store index configuration.
- Does not support `NO_PROXY` environment variable.

**Source:** n8n-nodes-langchain.embeddingsawsbedrock.md  [doc-verified]
