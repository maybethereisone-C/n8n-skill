# Lemonade Model — `n8n-nodes-langchain.lmLemonade`
**Type** `n8n-nodes-langchain.lmLemonade` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides text completion (non-chat) models hosted on a Lemonade server for Basic LLM Chain workflows.
**Credentials:** `lemonadeApi`
**Resources / Operations:** No discrete operations — exposes a completion LLM connection point.
**Key params & gotchas:**
- **Model**: Sourced from the Lemonade server; not a cloud API.
- **Max Tokens to Generate**: Default `-1` (unlimited). Large values can block the execution thread.
- **Stop Sequences**: Comma-separated; useful for structured generation (e.g. JSON boundaries).
- This is the completion (non-chat) variant — use `lmChatLemonade` for chat/agent workflows.
**Source:** n8n-nodes-langchain.lmlemonade.md  [doc-verified]
