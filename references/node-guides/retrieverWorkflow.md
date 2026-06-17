# Workflow Retriever — `@n8n/n8n-nodes-langchain.retrieverWorkflow`
**Type** `@n8n/n8n-nodes-langchain.retrieverWorkflow` · **typeVersion** 1 · **ai (sub-node / retriever)**
**What:** Sub-node that calls another n8n workflow as a retriever, enabling custom retrieval logic (vector search, DB lookup, etc.) inside AI chains.
**Credentials:** None — uses n8n internal workflow execution.
**Resources / Operations:** Retriever provider — connects to Retrieval QA Chain or other retriever-consuming root nodes via `ai_retriever` connection type.

**Key params & gotchas:**
- **Source**: either `Database` (enter a workflow ID) or `Parameter` (paste full workflow JSON inline).
- The called workflow receives the retriever query as input and must return documents in LangChain Document format (`pageContent` + `metadata`).
- **Workflow values**: pass static or dynamic values into the called workflow via the Workflow Values section.
- Sub-node expression resolution: expressions are evaluated at runtime, not design time — the called workflow ID can be dynamic.
- Use this when your retrieval logic is too complex for a standard vector store retriever (e.g., hybrid search, multi-source fan-out, custom re-ranking).

**Source:** n8n-nodes-langchain.retrieverworkflow.md  [doc-verified]
