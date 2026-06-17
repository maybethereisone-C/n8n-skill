# Structured Output Parser — `n8n-nodes-langchain.outputParserStructured`
**Type** `n8n-nodes-langchain.outputParserStructured` · **typeVersion** 1 · **ai**
**What:** Sub-node that validates and parses LLM output against a JSON Schema, returning structured data to downstream nodes.
**Credentials:** none
**Resources / Operations:** No discrete operations — validates/parses LLM text into structured JSON.
**Key params & gotchas:**
- **Schema Type**: Two options — provide a JSON Schema directly, or use n8n's visual schema builder. Both result in the same runtime behavior.
- The parser injects format instructions into the prompt automatically — the LLM must follow JSON Schema output format.
- On parse failure, the node errors. Wrap with **Auto-fixing Output Parser** for resilience against occasional malformed responses.
- Pair with models that reliably support JSON mode (OpenAI, DeepSeek, Mistral, etc.) for best results.
**Source:** n8n-nodes-langchain.outputparserstructured/index.md  [doc-verified]
