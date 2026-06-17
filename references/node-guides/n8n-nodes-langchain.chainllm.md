# Basic LLM Chain — `n8n-nodes-langchain.chainLlm`
**Type** `n8n-nodes-langchain.chainLlm` · **typeVersion** 1 · **ai / cluster root node**
**What:** Simple LLM prompt-response chain — set a prompt, optionally attach an output parser, and get structured or plain text responses from a connected chat model.
**Credentials:** None directly — credentials are on the connected LLM sub-node.

## Key params & gotchas
- **Requires a connected Chat Model sub-node** — the node ignores Chat Messages options if no chat model is connected.
- **Prompt modes:**
  - `Connected Chat Trigger Node` — reads `chatInput` field from upstream. If the field is missing, throws "No prompt specified" error — fix with a Set node renaming the field to `chatInput`.
  - `Define Below` — static text or expression.
- **Require Specific Output Format** — connect an Output Parser sub-node for structured output (JSON schema, item list, etc.).
- **Chat Messages** (AI / System / User) set few-shot examples or system instructions for chat models. User messages support Text, Image (Binary), or Image (URL) types; image detail level (auto/low/high) affects token cost.
- This is the simplest LangChain root node — use AI Agent when tool-calling is needed.

**Source:** n8n-nodes-langchain.chainllm.md  [doc-verified]
