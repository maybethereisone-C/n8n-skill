# Default Data Loader — `n8n-nodes-langchain.documentDefaultDataLoader`
**Type** `n8n-nodes-langchain.documentDefaultDataLoader` · **ai · sub-node**
**What:** Loads binary files or JSON from workflow input and prepares them as LangChain documents for vector stores or summarization chains.
**Credentials:** None.

**Key params & gotchas:**
- **Text Splitting**: `Simple` (Recursive Character Splitter, chunk=1000, overlap=200) or `Custom` (connect a splitter sub-node for fine control).
- **Type of Data**: `Binary` or `JSON`.
- **Mode**: `Load All Input Data` or `Load Specific Data` (expression-based; can mix static text + expressions to build a custom document).
- **Data Format** (Binary mode): Set to `Automatically Detect by MIME Type` unless you need to force a specific format. If the MIME type doesn't match a forced format, the node errors; auto-detect falls back to plain text on unknown types.
- **Metadata** (option): Key/value pairs attached to every document chunk — used by vector store metadata filters at retrieval time. Set these consistently if you plan to filter by source, author, etc.
- This is the standard document loader for most RAG pipelines; use GitHub Document Loader only for GitHub-sourced repos (and note it is deprecated).

**Source:** n8n-nodes-langchain.documentdefaultdataloader.md  [doc-verified]
