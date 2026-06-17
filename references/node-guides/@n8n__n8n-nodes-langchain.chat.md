# Chat — `@n8n/n8n-nodes-langchain.chat`

**Type** `@n8n/n8n-nodes-langchain.chat` · **typeVersion** 1.4 · **ai**

**What:** Sends a message into an active chat session and optionally waits for a human reply — enables multi-turn HITL conversations within a single workflow execution.

**Credentials:** none.

**Resources / Operations:**

| Operation | Description |
|---|---|
| Send Message | Send a message; workflow continues immediately |
| Send and Wait for Response | Send a message and pause until user replies |

**Key params & gotchas:**

- **Prerequisite** — requires a Chat Trigger node in the same workflow with **Response Mode** set to `Using Response Nodes`. Without it the node silently misbehaves.
- **Not supported in Embedded mode** — when Chat Trigger is set to `Embedded`, use Respond to Webhook instead.
- **Not supported in subworkflows** — the Chat node cannot be used inside a subworkflow called as a tool or via Execute Workflow.
- **Not supported as a subagent tool** — cannot be used as a tool node for a nested AI Agent.
- **Send and Wait — Response Types:**
  - `Free Text` — user types any reply; output contains the text.
  - `Approval` — renders inline buttons (Approve / Disapprove). `Block User Input` prevents typed responses. Button labels are configurable.
- **Limit Wait Time** (both response types) — safety timeout; workflow auto-resumes after an interval or wall-clock time if the user never responds.
- **Add Memory Input Connection** (option) — attaches messages to a shared memory sub-node so the full conversation history is visible to a connected Agent. Connect the same memory node to both the Chat Trigger and the Chat node.
- Previously named "Respond to Chat"; the old single "Wait for User Reply" toggle is now the `Send and Wait for Response` operation.

**Source:** n8n-nodes-langchain.chat.md  [doc-verified]
