# Item List Output Parser — `n8n-nodes-langchain.outputParserItemList`
**Type** `n8n-nodes-langchain.outputParserItemList` · **typeVersion** 1 · **ai**
**What:** Sub-node that parses LLM output into a list of discrete items split by a separator.
**Credentials:** none
**Resources / Operations:** No discrete operations — transforms LLM text output into an array.
**Key params & gotchas:**
- **Number of Items**: `-1` = unlimited. Set a positive integer to cap list length (excess items are dropped).
- **Separator**: Defaults to newline (`\n`). Change to comma, pipe, etc. to match your prompt's expected output format.
- Prompt engineering tip: explicitly instruct the model to output one item per line (or per separator) to avoid parse errors.
- Produces n8n items from the parsed list — downstream nodes receive individual items, not a raw array.
**Source:** n8n-nodes-langchain.outputparseritemlist.md  [doc-verified]
