# Simple Memory — `n8n-nodes-langchain.memoryBufferWindow`
**Type** `n8n-nodes-langchain.memoryBufferWindow` · **typeVersion** 1 · **ai**
**What:** Sub-node that persists a sliding window of chat history in-process (in workflow memory) for AI Agents.
**Credentials:** none
**Resources / Operations:** No discrete operations — provides memory connection to Agent/Chain nodes.
**Key params & gotchas:**
- **Session Key**: Scopes the memory store within the workflow. Different keys = independent conversation threads in the same workflow.
- **Context Window Length**: Number of prior interaction pairs (user + AI) kept in context; older messages are dropped.
- **Queue mode incompatible**: If n8n runs in queue mode with multiple workers, this node breaks because memory is in-process and workers don't share state. Use Redis, Postgres, or MongoDB memory nodes instead.
- Simplest option for single-worker or development setups.
**Source:** n8n-nodes-langchain.memorybufferwindow/index.md  [doc-verified]
