# Postgres Chat Memory — `n8n-nodes-langchain.memoryPostgresChat`
**Type** `n8n-nodes-langchain.memoryPostgresChat` · **typeVersion** 1 · **ai**
**What:** Sub-node that persists chat history in a Postgres table for AI Agents — production-safe in queue mode.
**Credentials:** `postgres`
**Resources / Operations:** No discrete operations — provides persistent memory connection.
**Key params & gotchas:**
- **Table Name**: Auto-created if it doesn't exist. Use a dedicated table (not an existing business table) to avoid schema conflicts.
- **Session Key**: Use a dynamic expression for multi-user workflows. Same key = shared memory across executions.
- **Single memory instance**: All executions with the same Session Key share state — by design for conversation continuity.
- Safe for multi-worker / queue-mode deployments (unlike Simple Memory).
**Source:** n8n-nodes-langchain.memorypostgreschat.md  [doc-verified]
