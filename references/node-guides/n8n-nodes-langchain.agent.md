# AI Agent — `n8n-nodes-langchain.agent`
**Type** `n8n-nodes-langchain.agent` · **typeVersion** ≥1.82 (Tools Agent only) · **ai / cluster root node**
**What:** Autonomous LLM agent that reasons over tool outputs to achieve a goal. Requires at least one tool sub-node connected; acts as a cluster root node.
**Credentials:** None directly — credentials are on the connected LLM and tool sub-nodes.

## Key params & gotchas
- **Requires at least one Tool sub-node** connected. Without a tool, the node won't run.
- **Prior to v1.82.0**, the node had selectable agent types (Conversational, OpenAI Functions, ReAct, Plan-and-Execute, SQL, Tools). All types were removed; the node now always runs as **Tools Agent** — the recommended mode. Existing workflows set to Tools Agent continue to work.
- Connect an LLM sub-node (e.g., `lmChatOpenAi`, `lmChatAnthropic`) to the **Chat Model** connector.
- Connect Memory sub-nodes to the **Memory** connector for multi-turn conversation.
- **Prompt** can be sourced from a connected Chat Trigger node (`chatInput` field) or defined inline.
- Tool sub-nodes provide capabilities: HTTP Request, Calculator, Code, Workflow, Vector Store, etc.
- Common failure: missing `chatInput` field when using "Connected Chat Trigger Node" prompt mode — use Set node to rename the field if needed.

**Source:** n8n-nodes-langchain.agent/index.md  [doc-verified]
