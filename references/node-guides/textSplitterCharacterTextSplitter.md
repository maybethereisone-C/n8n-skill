# Character Text Splitter — `@n8n/n8n-nodes-langchain.textSplitterCharacterTextSplitter`
**Type** `@n8n/n8n-nodes-langchain.textSplitterCharacterTextSplitter` · **typeVersion** 1 · **ai (sub-node / text splitter)**
**What:** Sub-node that splits document text on a fixed separator character before loading into a vector store or chain.
**Credentials:** None.
**Resources / Operations:** Text splitter provider — connects to document loader nodes via `ai_textSplitter` connection type.

**Key params & gotchas:**
- **Separator**: the character(s) to split on (default `\n\n`). Splits are made at every occurrence; if the separator is rare, chunks may be very large.
- **Chunk Size**: max characters per chunk after splitting.
- **Chunk Overlap**: characters of overlap between adjacent chunks — prevents context loss at boundaries; typically 10–20% of Chunk Size.
- Splits first on the separator, then truncates to Chunk Size. If a single segment exceeds Chunk Size with no separator, it is kept as-is (no hard truncation).
- For hierarchical splitting (paragraphs → sentences → words), use the Recursive Character Text Splitter instead.

**Source:** n8n-nodes-langchain.textsplittercharactertextsplitter.md  [doc-verified]
