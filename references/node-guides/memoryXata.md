# Xata — `n8n-nodes-langchain.memoryXata`
**Type** `n8n-nodes-langchain.memoryXata` · **typeVersion** 1 · **ai**
**What:** Sub-node that uses Xata (serverless database) as a chat memory store for AI Agents.
**Credentials:** `xataApi`
**Resources / Operations:** No discrete operations — provides persistent memory connection.
**Key params & gotchas:**
- **Session ID**: Scopes the conversation (note: called "Session ID" here vs "Session Key" in other memory nodes — same concept).
- **Context Window Length**: Number of prior interactions retained in context.
- Single memory instance: same Session ID = shared state across executions.
**Source:** n8n-nodes-langchain.memoryxata.md  [doc-verified]
