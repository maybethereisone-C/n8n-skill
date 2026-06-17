# MiniMax Chat Model — `n8n-nodes-langchain.lmChatMiniMax`
**Type** `n8n-nodes-langchain.lmChatMiniMax` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides MiniMax chat models (including reasoning models) for AI Agents and chains.
**Credentials:** `minimaxApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Hide Thinking** (default ON): Strips `<think>` tags from reasoning model output. Turn OFF to expose chain-of-thought in the output — useful for debugging or when downstream nodes need to parse reasoning.
- **Model**: Not dynamically loaded — select from a static list; check [MiniMax model docs](https://platform.minimax.io/docs/guides/models-intro) for current IDs.
**Source:** n8n-nodes-langchain.lmchatminimax.md  [doc-verified]
