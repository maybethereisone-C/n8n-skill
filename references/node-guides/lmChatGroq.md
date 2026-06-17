# Groq Chat Model — `n8n-nodes-langchain.lmChatGroq`
**Type** `n8n-nodes-langchain.lmChatGroq` · **typeVersion** 1 · **ai**
**What:** Sub-node that provides Groq's ultra-fast inference chat models for AI Agents and chains.
**Credentials:** `groqApi`
**Resources / Operations:** No discrete operations — exposes a chat LLM connection point.
**Key params & gotchas:**
- **Model**: Dynamically loaded from Groq API.
- Only **Max Tokens** and **Temperature** are exposed as options (minimal controls vs other providers).
- Groq is primarily valued for speed (LPU inference); useful in latency-sensitive agent loops.
**Source:** n8n-nodes-langchain.lmchatgroq.md  [doc-verified]
