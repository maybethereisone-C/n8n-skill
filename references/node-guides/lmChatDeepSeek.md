# DeepSeek Chat Model — `n8n-nodes-langchain.lmChatDeepSeek`
**Type** `n8n-nodes-langchain.lmChatDeepSeek` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides DeepSeek chat models (OpenAI-API-compatible) for AI Agents and chains.
**Credentials:** `deepSeekApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded; only models available to your account appear.
- **Base URL**: Override to point at a self-hosted or proxied endpoint (useful for private DeepSeek deployments).
- **Response Format**: Set to **JSON** to guarantee valid JSON output — must include the word `json` in your prompt.
- **Frequency / Presence Penalty**: Use one or the other to control repetition/topic diversity; stacking both can produce unpredictable results.
- DeepSeek is OpenAI-spec compatible; LangChain's OpenAI client is used under the hood.
**Source:** n8n-nodes-langchain.lmchatdeepseek.md  [doc-verified]
