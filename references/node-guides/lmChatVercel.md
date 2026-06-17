# Vercel AI Gateway Chat Model — `n8n-nodes-langchain.lmChatVercel`
**Type** `n8n-nodes-langchain.lmChatVercel` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides models via Vercel AI Gateway (a unified proxy over multiple AI providers) for AI Agents and chains.
**Credentials:** `vercelApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded from the AI Gateway (account-scoped).
- Vercel AI Gateway is OpenAI-API-compatible; LangChain's OpenAI client is used under the hood.
- **Response Format JSON**: Word `json` must appear in the prompt.
- Provides observability, rate-limiting, and provider-switching through the Vercel dashboard — useful for teams already on Vercel infrastructure.
**Source:** n8n-nodes-langchain.lmchatvercel.md  [doc-verified]
