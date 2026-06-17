# Embeddings Lemonade — `n8n-nodes-langchain.embeddingsLemonade`
**Type** `n8n-nodes-langchain.embeddingsLemonade` · **ai · sub-node**
**What:** Generates text embeddings using models hosted on a local/self-managed Lemonade server.
**Credentials:** `lemonadeApi`.

**Key params & gotchas:**
- **Model**: Selected from models loaded and served by the configured Lemonade server instance — list is dynamic. If empty, check that the Lemonade server is running and the credential endpoint is correct.
- Suitable for air-gapped or privacy-sensitive deployments where cloud embedding APIs are not permitted.
- Dimensions are model-dependent — match to vector store index configuration.

**Source:** n8n-nodes-langchain.embeddingslemonade.md  [doc-verified]
