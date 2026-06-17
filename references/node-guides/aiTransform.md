# AI Transform — `n8n-nodes-base.aiTransform`

**Type** `n8n-nodes-base.aiTransform` · **typeVersion** 1 · **core**

**What:** Generates a JavaScript transformation snippet from a plain-English prompt and applies it to input data — AI-assisted Code node.

**Credentials:** None (uses n8n's internal AI; requires Cloud plan).

**Resources / Operations:** Single operation — prompt → generated code → applied transformation.

**Key params & gotchas:**
- **Cloud only** — not available on self-hosted instances.
- **Instructions**: plain English, max 500 characters. Click **Generate code** to produce the snippet.
- **Transformation Code** is read-only in this node; to edit generated code manually, copy it into a Code node.
- Context-aware: the AI sees the upstream nodes and their data types when generating code — referencing field names from prior nodes in your prompt improves accuracy.
- Re-generating code overwrites the previous snippet without warning.

**Source:** n8n-nodes-base.aitransform.md  [doc-verified]
