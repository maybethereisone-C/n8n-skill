# Information Extractor — `n8n-nodes-langchain.informationExtractor`
**Type** `n8n-nodes-langchain.informationExtractor` · **ai**
**What:** Extracts structured data from free-form text using an LLM and a user-defined output schema.
**Credentials:** None (LLM sub-node provides credentials).

**Key params & gotchas:**
- **Text**: Expression pointing to input text (e.g. `{{ $json.chatInput }}`).
- **Schema Type** — three options:
  - `From Attribute Descriptions`: Define field names + descriptions; easiest to maintain.
  - `Generate From JSON Example`: Paste a sample JSON object; n8n infers types. Every field becomes mandatory — cannot mark fields optional this way.
  - `Define using JSON Schema`: Full control; must be valid JSON Schema.
- **System Prompt Template** (option): Override the extraction prompt. n8n always appends format-specification instructions automatically — do not re-include them.
- Model temperature should be low (0–0.2) for deterministic extraction.

**Source:** n8n-nodes-langchain.information-extractor.md  [doc-verified]
