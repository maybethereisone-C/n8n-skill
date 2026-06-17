# Moonshot Kimi — `n8n-nodes-langchain.moonshot`
**Type** `n8n-nodes-langchain.moonshot` · **typeVersion** 1 · **action/ai**
**What:** Send messages to Moonshot Kimi models with optional image attachments, or analyze images using vision models.
**Credentials:** `moonshotApi` (API key from platform.kimi.ai).

## Resources / Operations
| Resource | Operations |
|---|---|
| Text | Message a Model |
| Image | Analyze Image |

## Key params & gotchas
- **Thinking Mode** and **Web Search** are mutually exclusive — enabling both will cause an error.
- **Add Attachments** on Message a Model accepts binary image field names (comma-separated for multiple images).
- `simplify: true` (default) returns condensed response; `includeMergedResponse` adds a single merged output string of all text parts.
- `maxToolsIterations` defaults to 15 (one iteration may include multiple tool calls); set to 0 for unlimited.
- **Analyze Image**: binary field name(s) separated by commas for multiple images; default question is `What's in this image?`.
- Model selected via `resourceLocator` — supports list selection or manual ID entry.

**Source:** n8n-nodes-langchain.moonshot.md  [doc-verified]
