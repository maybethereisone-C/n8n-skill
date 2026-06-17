# AI Agent Tool — `@n8n/n8n-nodes-langchain.toolAiAgent`
**Type** `@n8n/n8n-nodes-langchain.toolAiAgent` · **typeVersion** 1 · **ai (sub-node / tool)**
**What:** Sub-node that wraps a nested AI agent as a callable tool for a parent agent — enables multi-agent hierarchies without sub-workflows.
**Credentials:** None directly — the nested agent connects its own Chat Model sub-node.
**Resources / Operations:** Tool provider — connects to Tools Agent root nodes via `ai_tool` connection type.

**Key params & gotchas:**
- **Description**: tells the parent agent when to delegate to this sub-agent — be specific (e.g., "Use this agent to search the web and summarize results"). Vague descriptions cause the parent to under-use or misuse the sub-agent.
- **Prompt (User Message)**: the instruction passed to the nested agent when invoked. Can include `$fromAI()` placeholders so the parent agent dynamically fills in the query.
- **Require Specific Output Format**: when on, connect an output parser sub-node to enforce structured output from the nested agent.
- **Enable Fallback Model**: connect a backup Chat Model sub-node — activates if the primary model fails.
- **Max Iterations**: caps the nested agent's tool-calling loops to prevent runaway execution.
- **Return Intermediate Steps**: exposes the nested agent's reasoning steps in the parent's output — useful for debugging multi-agent pipelines.
- **Batch Processing**: use Batch Size + Delay Between Batches for rate-limit-sensitive nested agents.
- Nesting is supported multiple levels deep, but increases latency and token cost multiplicatively.

**Source:** n8n-nodes-langchain.toolaiagent.md  [doc-verified]
