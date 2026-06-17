# DeepL — `n8n-nodes-base.deepL`
**Type** `n8n-nodes-base.deepL` · **action**
**What:** Translate text between languages using the DeepL API.
**Credentials:** deeplApi (API key — Free or Pro).

## Resources / Operations
| Resource | Operations |
|---|---|
| Language | Translate |

## Key params & gotchas
- Free API keys use `api-free.deepl.com`; Pro keys use `api.deepl.com`. The credential config must match — mismatched base URLs cause 403 errors.
- `target_lang` is required; `source_lang` is optional (auto-detected if omitted).
- Language codes use DeepL format (e.g., `EN-US`, `PT-BR`) — not BCP-47 `en-US`.
- Can be used as an AI tool node; useful as a translation step in LLM pipelines.
- "Operation not supported" error applies to formality settings not available for all target languages.

**Source:** n8n-nodes-base.deepl.md  [doc-verified]
