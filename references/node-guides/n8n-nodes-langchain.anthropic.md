# Anthropic — `n8n-nodes-langchain.anthropic`
**Type** `n8n-nodes-langchain.anthropic` · **typeVersion** 1 · **action/ai**
**What:** Interact with Anthropic's Claude models for text completions, document/image analysis, file management, and prompt engineering utilities.
**Credentials:** `anthropicApi` (API key from console.anthropic.com).

## Resources / Operations
| Resource | Operations |
|---|---|
| Document | Analyze Document |
| File | Upload File, Get File Metadata, List Files, Delete File |
| Image | Analyze Image |
| Prompt | Generate Prompt, Improve Prompt, Templatize Prompt |
| Text | Message a Model |

## Key params & gotchas
- **Prompt utilities** (Generate, Improve, Templatize) are meta-operations that use Claude to engineer prompts — useful for automated prompt optimization pipelines.
- **File operations** use the Anthropic Files API for persistent file storage across requests; files can be referenced by ID in subsequent calls.
- **Analyze Document/Image** passes binary data or URLs to Claude's vision/document capabilities.
- For LangChain-style sub-node use (as an LLM for AI Agent or Chain nodes), use `n8n-nodes-langchain.lmChatAnthropic` instead — this node is for direct API calls.
- Rate limits and model availability vary by API tier.

**Source:** n8n-nodes-langchain.anthropic.md  [doc-verified]
