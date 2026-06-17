# Azure OpenAI Chat Model — `@n8n/n8n-nodes-langchain.lmChatAzureOpenAi`
**Type** `@n8n/n8n-nodes-langchain.lmChatAzureOpenAi` · **typeVersion** 1 · **ai (sub-node / LLM)**
**What:** Sub-node providing Azure-hosted OpenAI chat models to AI root nodes via Azure OpenAI Service.
**Credentials:** `azureOpenAiApi` (Azure OpenAI endpoint URL + API key).
**Resources / Operations:** LLM provider — connects to root AI nodes via `ai_languageModel` connection type.

**Key params & gotchas:**
- **Model**: must match your Azure deployment name (not the base model name — Azure uses custom deployment names).
- **Response Format**: set to `JSON` to guarantee valid JSON output; use with structured extraction tasks.
- **Frequency Penalty / Presence Penalty**: tune repetition and topic diversity independently.
- **Top P**: nucleus sampling threshold; lower = safer/more focused. Don't set both Temperature and Top P high simultaneously.
- **Timeout / Max Retries**: important for resilience — Azure OpenAI can throttle under load.
- Does NOT support the `NO_PROXY` environment variable.
- Sub-node expression resolution: `{{ }}` expressions evaluated at runtime.

**Source:** n8n-nodes-langchain.lmchatazureopenai.md  [doc-verified]
