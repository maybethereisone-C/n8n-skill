# Cohere Chat Model — `n8n-nodes-langchain.lmChatCohere`
**Type** `n8n-nodes-langchain.lmChatCohere` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides Cohere's Command chat models as the LLM for AI Agents and chains.
**Credentials:** `cohereApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded from Cohere API (only models your account has access to appear).
- **Sampling Temperature**: Controls randomness; higher = more creative, higher hallucination risk.
- **Max Retries**: Retry count on transient API failures.
**Source:** n8n-nodes-langchain.lmchatcohere.md  [doc-verified]
