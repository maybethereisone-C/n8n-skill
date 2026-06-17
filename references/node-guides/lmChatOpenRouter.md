# OpenRouter Chat Model — `n8n-nodes-langchain.lmChatOpenRouter`
**Type** `n8n-nodes-langchain.lmChatOpenRouter` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides OpenRouter's unified model gateway (100+ models from multiple providers) for AI Agents and chains.
**Credentials:** `openRouterApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded from OpenRouter (account-scoped); includes models from OpenAI, Anthropic, Google, Meta, etc.
- OpenRouter is OpenAI-API-compatible; underlying client is LangChain's OpenAI client.
- **Response Format JSON**: Word `json` must appear in the prompt when using JSON mode.
- Useful for routing to the cheapest/fastest available model without changing node type.
**Source:** n8n-nodes-langchain.lmchatopenrouter.md  [doc-verified]
