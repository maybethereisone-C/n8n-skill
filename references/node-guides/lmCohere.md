# Cohere Model — `n8n-nodes-langchain.lmCohere`
**Type** `n8n-nodes-langchain.lmCohere` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides Cohere's completion (non-chat) LLM for Basic LLM Chain — does NOT support tool use.
**Credentials:** `cohereApi`
**Resources / Operations:** No discrete operations — exposes a completion LLM connection point.
**Key params & gotchas:**
- **No tools support**: Cannot connect to the AI Agent node. Must pair with the **Basic LLM Chain** node instead.
- No Model param in the doc — uses a default Cohere model. Options only expose Max Tokens and Temperature.
- Use `lmChatCohere` instead when you need agent/tool calling capability.
**Source:** n8n-nodes-langchain.lmcohere.md  [doc-verified]
