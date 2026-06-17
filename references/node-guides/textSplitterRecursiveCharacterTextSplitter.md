# Recursive Character Text Splitter — `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
**Type** `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter` · **typeVersion** 1 · **ai (sub-node / text splitter)**
**What:** Sub-node that recursively splits document text (paragraphs → sentences → words) to maximize semantic coherence of chunks.
**Credentials:** None.
**Resources / Operations:** Text splitter provider — connects to document loader nodes via `ai_textSplitter` connection type.

**Key params & gotchas:**
- **Chunk Size**: max characters per chunk.
- **Chunk Overlap**: character overlap between adjacent chunks — prevents context loss at chunk boundaries.
- Splits hierarchy: `\n\n` → `\n` → ` ` → `""` (character). Falls through to next separator only when needed — keeps paragraphs and sentences together as long as they fit in Chunk Size.
- **Preferred over Character Text Splitter** for prose documents (articles, PDFs, emails) because it preserves semantic units.
- No separator configuration — the recursive set is fixed. Use Character Text Splitter when you need a custom separator (e.g., `---` for markdown sections).

**Source:** n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md  [doc-verified]
