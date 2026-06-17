# Think Tool — `@n8n/n8n-nodes-langchain.toolThink`

**Type** `@n8n/n8n-nodes-langchain.toolThink` · **typeVersion** 1 · **ai**

**What:** Zero-config AI tool sub-node that gives an agent a "scratchpad" to reason through complex queries before answering — Anthropic-style extended thinking as an explicit tool call.

**Credentials:** None.

**Resources / Operations:** No configurable parameters. The agent invokes this tool when it needs to reason step-by-step; n8n returns the agent's own reasoning text back to it.

**Key params & gotchas:**
- No parameters to set — just wire it to an AI Agent's Tools input.
- Particularly valuable for multi-step logic, math, or ambiguous questions where a flat prompt answer often fails.
- The agent decides *when* to call this tool; you can't force it to always think first from this node alone (use system prompt instructions if needed).

**Source:** n8n-nodes-langchain.toolthink.md  [doc-verified]
