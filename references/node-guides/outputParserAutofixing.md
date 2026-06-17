# Auto-fixing Output Parser — `n8n-nodes-langchain.outputParserAutofixing`
**Type** `n8n-nodes-langchain.outputParserAutofixing` · **typeVersion** 1 · **ai**
**What:** Sub-node that wraps another output parser and uses a second LLM call to correct malformed output when the primary parser fails.
**Credentials:** none (delegates to attached LLM and parser sub-nodes)
**Resources / Operations:** No discrete operations — wraps another parser node.
**Key params & gotchas:**
- Requires two sub-node connections: an inner **output parser** (e.g. Structured Output Parser) and an **LLM** for the fix-up call.
- Adds a second LLM call on parse failure — increases latency and cost; only use when output format correctness is critical.
- Best combined with Structured Output Parser when the schema is strict and the primary model occasionally produces invalid JSON.
**Source:** n8n-nodes-langchain.outputparserautofixing.md  [doc-verified]
