# Token Splitter — `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
**Type** `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter` · **typeVersion** 1 · **ai (sub-node / text splitter)**
**What:** Sub-node that splits text by BPE token count rather than character count — ensures chunks fit within LLM token limits precisely.
**Credentials:** None.
**Resources / Operations:** Text splitter provider — connects to document loader nodes via `ai_textSplitter` connection type.

**Key params & gotchas:**
- **Chunk Size**: max tokens per chunk (not characters). Use this when you need to respect a model's context window measured in tokens.
- **Chunk Overlap**: token overlap between adjacent chunks.
- Uses tiktoken (BPE) tokenization — token count differs from character count (roughly 1 token ≈ 4 chars for English). A 1000-token chunk ≈ 750 words.
- More accurate than character splitters for fitting chunks into models with strict token budgets (e.g., embedding models with 512-token limits).
- Slightly slower than character splitters due to tokenization overhead.

**Source:** n8n-nodes-langchain.textsplittertokensplitter.md  [doc-verified]
