# Embeddings Oracle Database — `n8n-nodes-langchain.embeddingsOracleDB`
**Type** `n8n-nodes-langchain.embeddingsOracleDB` · **ai · sub-node**
**What:** Generates text embeddings using ONNX models imported into Oracle Database's AI Vector Search.
**Credentials:** `oracleDb`.

**Key params & gotchas:**
- **Prerequisite**: Oracle Database must support Oracle AI Vector Search AND ONNX model execution. ONNX models must be manually imported into the DB before use.
- **Model**: Loaded from `USER_MINING_MODELS` view — only models accessible to the DB user are listed. Empty list = no imported ONNX models or insufficient privileges.
- Embedding dimensions are determined by the imported ONNX model — must match the target Oracle Database Vector Store table schema.
- Pairing this node with the Oracle Database Vector Store creates a fully on-premises, Oracle-native RAG pipeline.

**Source:** n8n-nodes-langchain.embeddingsoracledb.md  [doc-verified]
