# Perplexity — `n8n-nodes-langchain.perplexity`
**Type** `n8n-nodes-langchain.perplexity` · **typeVersion** 1 · **action/ai**
**What:** Send prompts to Perplexity AI models to generate completions (includes built-in web search via Perplexity's sonar models).
**Credentials:** `perplexityApi` (API key from docs.perplexity.ai).

## Resources / Operations
| Resource | Operations |
|---|---|
| Text | Message a Model |

## Key params & gotchas
- Perplexity's `sonar` model family performs live web search before responding — responses include citations by default.
- Minimal operations surface; for advanced parameters (temperature, max_tokens, search recency filters) use HTTP Request to the Perplexity API directly.
- Note: a `n8n-nodes-base.perplexity` guide also exists in the references directory — that is a different/older listing; this node is under the langchain namespace.

**Source:** n8n-nodes-langchain.perplexity.md  [doc-verified]
