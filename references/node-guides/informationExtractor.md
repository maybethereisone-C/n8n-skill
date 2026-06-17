# Information Extractor — `@n8n/n8n-nodes-langchain.informationExtractor`
**Type** `@n8n/n8n-nodes-langchain.informationExtractor` · **typeVersion** 1 · **ai (root/cluster)**
**What:** Extract structured data from free-form text using an LLM with a defined output schema; outputs JSON matching the schema.
**Credentials:** None directly — requires a connected Chat Model sub-node.
**Resources / Operations:** Single operation — extract structured fields from input text.

**Key params & gotchas:**
- **Text**: expression referencing input field, e.g. `{{ $json.chatInput }}` or `{{ $json.text }}`.
- **Schema Type** (choose one):
  - `From Attribute Descriptions` — list field name + description; LLM infers values.
  - `Generate From JSON Example` — paste example JSON; all fields become mandatory.
  - `Define using JSON Schema` — raw JSON Schema; most flexible, supports optional fields.
- System Prompt Template can be overridden; n8n auto-appends format instructions — don't duplicate them.
- Use `Generate From JSON Example` for rapid prototyping; switch to `Define using JSON Schema` for production to control required vs optional fields.
- Outputs one item per input item with a `output` key containing the extracted JSON.

**Minimal example (wiring):**
```
[Trigger] → [Information Extractor]
                └── [OpenAI Chat Model]  (sub-node)
```

**Source:** n8n-nodes-langchain.information-extractor.md  [doc-verified]
