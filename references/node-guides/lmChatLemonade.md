# Lemonade Chat Model — `n8n-nodes-langchain.lmChatLemonade`
**Type** `n8n-nodes-langchain.lmChatLemonade` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides chat models hosted by a local/remote Lemonade server for AI Agents and chains.
**Credentials:** `lemonadeApi` (Lemonade server URL + auth)
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Supplied by the Lemonade server — if no models appear, check server config and credentials.
- **Max Tokens to Generate**: Default `-1` (no limit); large values can produce very long outputs and block the workflow.
- **Stop Sequences**: Comma-separated strings; useful for structured generation where you want the model to halt at a delimiter.
- Lemonade is a local LLM management server — this node is the on-premise/private-LLM alternative to cloud providers.
**Source:** n8n-nodes-langchain.lmchatlemonade.md  [doc-verified]
