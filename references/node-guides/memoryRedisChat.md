# Redis Chat Memory — `n8n-nodes-langchain.memoryRedisChat`
**Type** `n8n-nodes-langchain.memoryRedisChat` · **typeVersion** 1 · **ai**
**What:** Sub-node that persists chat history in Redis for AI Agents — production-safe in queue mode.
**Credentials:** `redis`
**Resources / Operations:** No discrete operations — provides persistent memory connection.
**Key params & gotchas:**
- **Session Time To Live**: Sets TTL in seconds on the Redis key — critical for preventing unbounded memory growth in high-volume bots. If unset, keys persist indefinitely.
- **Session Key**: Scopes the conversation. Use a dynamic value (e.g. user ID) for multi-user workflows.
- **Single memory instance**: Same Session Key = shared memory across concurrent executions.
- Best choice for high-throughput, queue-mode n8n deployments due to Redis speed.
**Source:** n8n-nodes-langchain.memoryredischat.md  [doc-verified]
