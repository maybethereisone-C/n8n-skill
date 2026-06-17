# MongoDB Chat Memory — `@n8n/n8n-nodes-langchain.memoryMongoChat`
**Type** `@n8n/n8n-nodes-langchain.memoryMongoChat` · **typeVersion** 1 · **ai (sub-node / memory)**
**What:** Sub-node providing MongoDB-backed persistent chat history to AI Agent root nodes.
**Credentials:** `mongoDb` (MongoDB connection string or host/port/auth).
**Resources / Operations:** Memory provider — connects to root AI nodes via `ai_memory` connection type.

**Key params & gotchas:**
- **Session Key**: key used to namespace conversation history in MongoDB — use `{{ $json.sessionId }}` or a stable per-user/per-conversation identifier to isolate histories.
- **Collection Name**: MongoDB collection to store messages in; auto-created if absent.
- **Database Name**: overrides the database specified in credentials; leave blank to use credential default.
- **Context Window Length**: number of past message pairs (human + AI) passed to the LLM — higher = more context but more tokens per request.
- Single memory instance warning: if multiple workflow executions share the same Session Key simultaneously, they read/write the same history — ensure Session Key is unique per conversation thread.
- Chat history is stored as raw LangChain message objects; do not manually edit the collection schema.

**Source:** n8n-nodes-langchain.memorymongochat.md  [doc-verified]
