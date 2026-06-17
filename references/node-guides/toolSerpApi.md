# SerpApi (Google Search) Tool — `@n8n/n8n-nodes-langchain.toolSerpApi`

**Type** `@n8n/n8n-nodes-langchain.toolSerpApi` · **typeVersion** 1 · **ai**

**What:** AI tool sub-node giving an agent Google Search results via SerpApi. **Deprecated** — use the community node "SerpApi Official" instead.

**Credentials:** SerpApi API key credential.

**Resources / Operations:**

| Option | Detail |
|--------|--------|
| Country | Google GL parameter (country code) |
| Device | desktop / mobile / tablet |
| Explicit Array | Force fresh fetch vs cached |
| Google Domain | e.g. google.com, google.co.uk |
| Language | Google HL parameter |

**Key params & gotchas:**
- **Deprecated** as of recent n8n releases; will be removed in a future version. Migrate to the verified SerpApi Official community node.
- Sub-node — connect to AI Agent's Tools input.

**Source:** n8n-nodes-langchain.toolserpapi.md  [doc-verified]
