# xAI Grok Chat Model — `n8n-nodes-langchain.lmChatXAIGrok`
**Type** `n8n-nodes-langchain.lmChatXAIGrok` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides xAI's Grok large language models for AI Agents and chains.
**Credentials:** `xAiApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded from xAI Grok API.
- **Max Tokens**: Most Grok models have a 2048-token context length; newer models support up to 32,768. Be explicit about limits to avoid truncation.
- **Response Format JSON**: Word `json` must appear in the prompt when using JSON mode.
**Source:** n8n-nodes-langchain.lmchatxaigrok.md  [doc-verified]
