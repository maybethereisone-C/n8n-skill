# SearXNG Tool — `@n8n/n8n-nodes-langchain.toolSearxng`

**Type** `@n8n/n8n-nodes-langchain.toolSearxng` · **typeVersion** 1 · **ai**

**What:** AI tool sub-node that lets an agent run web searches via a self-hosted SearXNG instance (privacy-respecting meta-search engine).

**Credentials:** SearXNG credential (base URL of your SearXNG instance).

**Resources / Operations:**

| Option | Default |
|--------|---------|
| Number of Results | 10 |
| Page Number | 1 |
| Language | en |
| Safe Search | None (options: None / Moderate / Strict) |

**Key params & gotchas:**
- Requires a **self-hosted** SearXNG instance reachable from the n8n host — no public SearXNG endpoint is provided.
- SearXNG must have JSON output enabled in its `settings.yml`: add `json` to `search.formats`. Without this the node will fail.
- Quality of results depends entirely on the health and configuration of your SearXNG instance.
- Sub-node — connect to AI Agent's Tools input.

**Source:** n8n-nodes-langchain.toolsearxng.md  [doc-verified]
