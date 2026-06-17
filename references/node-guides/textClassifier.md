# Text Classifier — `@n8n/n8n-nodes-langchain.textClassifier`
**Type** `@n8n/n8n-nodes-langchain.textClassifier` · **typeVersion** 1 · **ai (root/cluster)**
**What:** Classify incoming text items into named categories using an LLM; routes items to per-category output branches.
**Credentials:** None directly — requires a connected Chat Model sub-node.
**Resources / Operations:** Single operation — classify text and route to category output pins.

**Key params & gotchas:**
- **Input Prompt**: expression for the text to classify (defaults to `{{ $json.text }}`).
- **Categories**: each category has a name and a description — descriptions are critical for ambiguous categories; the LLM uses them to decide.
- **Allow Multiple Classes To Be True**: off = exactly one category output per item; on = item can appear on multiple output branches.
- **When No Clear Match**: `Discard Item` (default) silently drops unmatched items; `Output on Extra 'Other' Branch` preserves them on a separate branch — prefer the latter in production to avoid silent data loss.
- **Enable Auto-Fixing**: retries schema parsing errors by re-prompting the LLM — adds latency and cost.
- Each category becomes a named output pin on the node; wire each to a different downstream path.

**Minimal example (wiring):**
```
[Trigger] → [Text Classifier] → [Branch: "support"]   → ...
                              → [Branch: "billing"]    → ...
                              → [Branch: "Other"]      → ...
             └── [OpenAI Chat Model]
```

**Source:** n8n-nodes-langchain.text-classifier.md  [doc-verified]
