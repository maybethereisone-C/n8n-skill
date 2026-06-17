# LangChain Code — `n8n-nodes-langchain.code`
**Type** `n8n-nodes-langchain.code` · **core/ai**
**What:** Escape hatch for any LangChain JS functionality not covered by built-in nodes; configurable as app node, root node, or sub-node by wiring inputs/outputs.
**Credentials:** None (manage inside user code).

**Key params & gotchas:**
- **Self-hosted only** — not available on n8n Cloud.
- **Mode**: `Execute` (needs main in + main out, works like the Code node) vs. `Supply Data` (sub-node mode, non-main output).
- Node type is determined entirely by the connector combination:

  | Role | Inputs | Outputs | Code mode |
  |------|--------|---------|-----------|
  | App node | Main | Main | Execute |
  | Root node | Main + ≥1 other | Main | Execute |
  | Sub-node | — | Non-main | Supply Data |
  | Sub-node with sub-nodes | Non-main | Non-main | Supply Data |

- Python is **not** supported; JS only.
- Built-in and external modules are disabled by default; self-hosted admins must enable via `NODE_FUNCTION_ALLOW_BUILTIN` / `NODE_FUNCTION_ALLOW_EXTERNAL`.
- n8n injects helper methods (`this.getInputData()`, `this.helpers.*`, etc.) — see built-in methods section in docs.

**Source:** n8n-nodes-langchain.code.md  [doc-verified]
