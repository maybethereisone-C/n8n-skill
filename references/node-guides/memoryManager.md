# Chat Memory Manager — `n8n-nodes-langchain.memoryManager`
**Type** `n8n-nodes-langchain.memoryManager` · **typeVersion** 1 · **ai**
**What:** Sub-node for programmatic read/write/delete of chat messages in agent memory within a workflow.
**Credentials:** none
**Resources / Operations:**
| Operation Mode | Description |
|---|---|
| Get Many Messages | Retrieve stored chat messages |
| Insert Messages | Add messages to memory (alongside existing or replace all) |
| Delete Messages | Remove last N or all messages |
**Key params & gotchas:**
- **Insert Mode — Override All Messages**: Replaces the entire memory contents — use carefully; there is no undo within a run.
- **Hide Message in Chat**: Controls whether injected messages appear in the n8n chat UI; turn ON to inject silent system context without showing it to the user.
- **Simplify Output**: In Get mode, reduces output to `{sender, text}` pairs — useful for downstream processing without raw LangChain message objects.
- Primary use case: pre-seeding agent memory with context before a conversation starts, or clearing state between workflow runs.
**Source:** n8n-nodes-langchain.memorymanager.md  [doc-verified]
