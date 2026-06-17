# Chat Trigger — `@n8n/n8n-nodes-langchain.chatTrigger`

**Type** `@n8n/n8n-nodes-langchain.chatTrigger` · **typeVersion** 1.4 · **trigger · ai**

**What:** Entry-point trigger for chatbot workflows; exposes a hosted or embedded chat interface and fires once per user message. Must connect to an Agent or Chain root node.

**Credentials:** Optional: Basic Auth credential (when `Authentication = Basic Auth`); n8n User Auth (requires logged-in n8n account).

**Resources / Operations:** Single trigger — fires on every inbound chat message.

**Key params & gotchas:**

- **Execution count** — each user message = one workflow execution. A 10-message conversation burns 10 executions.
- **Make Chat Publicly Available** — off by default; keep off during development. Turn on only when publishing.
- **Mode:**
  - `Hosted Chat` — n8n serves the UI at the shown URL; configurable title, subtitle, placeholder, initial messages.
  - `Embedded Chat` — you host the UI using `@n8n/chat` npm widget or a custom interface that POSTs to the webhook URL.
- **Authentication:** `None` (public), `Basic Auth` (single shared credential), `n8n User Auth` (n8n account required).
- **Load Previous Session** — `From Memory` requires connecting both this node and the Agent to the same memory sub-node; that's the single source of truth for history.
- **Response Mode:**
  - `When Last Node Finishes` — auto-returns last node output as chat reply.
  - `Using Response Nodes` — reply is controlled by a Chat node or Respond to Webhook node; use for HITL or custom formatting.
  - `Streaming response` — real-time token streaming; requires a streaming-capable node (e.g. AI Agent with streaming).
- **Set the chat response manually** — the Chat Trigger reads the `output` or `text` field of the last node. If your final node uses a different field name, the trigger sends the entire object as the reply.
- **Make Available in n8n Chat Hub** — exposes the agent in the n8n Chat Hub sidebar; requires `Agent Name` and optional `Agent Description` / icon.
- Replaces the Manual Chat Trigger node from n8n v1.24.0.

**Source:** n8n-nodes-langchain.chattrigger/index.md  [doc-verified]
