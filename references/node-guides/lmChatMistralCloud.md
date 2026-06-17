# Mistral Cloud Chat Model — `n8n-nodes-langchain.lmChatMistralCloud`
**Type** `n8n-nodes-langchain.lmChatMistralCloud` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides Mistral AI cloud chat models for AI Agents and chains.
**Credentials:** `mistralCloudApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded from Mistral Cloud (account-scoped).
- **Enable Safe Mode**: Injects a safety system prompt at the beginning of the conversation — disables some creative/sensitive use cases but adds a guardrail layer.
- **Random Seed**: Setting a seed makes responses deterministic across identical calls — useful for regression testing prompts.
**Source:** n8n-nodes-langchain.lmchatmistralcloud.md  [doc-verified]
