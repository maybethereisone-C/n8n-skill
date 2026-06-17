# Text Classifier — `n8n-nodes-langchain.textClassifier`
**Type** `n8n-nodes-langchain.textClassifier` · **ai**
**What:** Routes input items into named categories using an LLM; each category becomes a separate output branch.
**Credentials:** None (LLM sub-node provides credentials).

**Key params & gotchas:**
- **Input Prompt**: Expression for the text to classify (default: `text` field; chat trigger: `{{ $json.chatInput }}`).
- **Categories**: List of name + description pairs. Description is critical — use it to disambiguate similar categories.
- **Allow Multiple Classes To Be True** (option): Off = single label per item; On = multi-label.
- **When No Clear Match** (option): `Discard Item` (default, silently drops) or `Output on Extra, 'Other' Branch` — prefer the Other branch in production to avoid silent data loss.
- **System Prompt Template** (option): Uses `{categories}` placeholder.
- **Enable Auto-Fixing** (option): Re-sends parse failures to the LLM; adds latency but reduces hard errors on ambiguous input.
- Model temperature near 0 recommended for repeatable routing.

**Source:** n8n-nodes-langchain.text-classifier.md  [doc-verified]
