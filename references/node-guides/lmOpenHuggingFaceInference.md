# Hugging Face Inference Model — `n8n-nodes-langchain.lmOpenHuggingFaceInference`
**Type** `n8n-nodes-langchain.lmOpenHuggingFaceInference` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides Hugging Face Inference API models (completion, not chat) for Basic LLM Chain workflows.
**Credentials:** `huggingFaceApi`
**Resources / Operations:** No discrete operations — exposes a completion LLM connection point.
**Key params & gotchas:**
- **No tools support**: Cannot connect to the AI Agent node. Use with **Basic LLM Chain** only.
- **Custom Inference Endpoint**: Override to point at a private/dedicated HF inference endpoint — critical for gated or custom-deployed models.
- **Top K**: Available (not present in most other providers) — useful for fine-grained control over token selection diversity.
**Source:** n8n-nodes-langchain.lmopenhuggingfaceinference.md  [doc-verified]
