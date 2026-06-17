# Moonshot Kimi Chat Model — `n8n-nodes-langchain.lmChatMoonshot`
**Type** `n8n-nodes-langchain.lmChatMoonshot` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides Moonshot AI's Kimi chat models for AI Agents and chains.
**Credentials:** `moonshotApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Default `kimi-k2.5`; not dynamically loaded — select from static list.
- **Response Format**: Supports `text` or JSON mode.
- **Timeout**: Default 360,000 ms (6 minutes) — unusually long; shorten for production to avoid stalled executions.
- **Top P vs Temperature**: Doc explicitly states to change one or the other, not both.
**Source:** n8n-nodes-langchain.lmchatmoonshot.md  [doc-verified]
