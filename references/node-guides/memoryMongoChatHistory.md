# MongoDB Chat Memory — `n8n-nodes-langchain.memoryMongoChatHistory`
**Type** `n8n-nodes-langchain.memoryMongoChatHistory` · **typeVersion** 1 · **ai**
**What:** Sub-node that persists chat history in a MongoDB collection for AI Agents — supports multi-worker deployments.
**Credentials:** `mongoDb`
**Resources / Operations:** No discrete operations — provides persistent memory connection.
**Key params & gotchas:**
- **Session Key**: Scopes which conversation is stored/retrieved. Use a dynamic expression (e.g. `{{ $json.sessionId }}`) for multi-user workflows.
- **Collection Name**: Auto-created if it doesn't exist.
- **Database Name**: If omitted, uses the database specified in credentials.
- **Single memory instance**: All workflow executions sharing the same Session Key read/write the same memory — intentional for continuity, but can cause cross-contamination if keys are reused across unrelated users.
**Source:** n8n-nodes-langchain.memorymongochat.md  [doc-verified]
