# Summarization Chain — `n8n-nodes-langchain.chainSummarization`
**Type** `n8n-nodes-langchain.chainSummarization` · **ai**
**What:** Summarizes one or more documents using a connected LLM; supports Map Reduce, Refine, and Stuff strategies.
**Credentials:** None (LLM sub-node provides credentials).
**Resources / Operations:** Single operation — summarize documents.

**Key params & gotchas:**
- **Data to Summarize**: `Use Node Input (JSON)`, `Use Node Input (Binary)`, or `Use Document Loader` — determines what connector is expected upstream.
- **Chunking Strategy** (for node-input modes): `Simple` (set chars-per-chunk + overlap) or `Advanced` (connect a text-splitter sub-node).
- **Summarization Method** (Add Option): `Map Reduce` (recommended for large docs, parallelisable), `Refine` (iterative, slower), `Stuff` (single-pass, small docs only — will fail if doc exceeds context window).
- Prompt templates must contain the `"{text}"` placeholder; missing it causes a runtime error.
- Map Reduce and Refine use separate prompts for individual summaries vs. final combination — both must be customised together or left at defaults.

**Source:** n8n-nodes-langchain.chainsummarization.md  [doc-verified]
