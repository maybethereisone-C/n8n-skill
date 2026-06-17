# Wikipedia Tool — `@n8n/n8n-nodes-langchain.toolWikipedia`

**Type** `@n8n/n8n-nodes-langchain.toolWikipedia` · **typeVersion** 1 · **ai**

**What:** AI tool sub-node that lets an agent search and retrieve Wikipedia article content.

**Credentials:** None (uses Wikipedia's public API).

**Resources / Operations:** No configurable parameters — the agent passes a search query; the node returns Wikipedia content.

**Key params & gotchas:**
- No configuration needed beyond wiring to an AI Agent's Tools input.
- Returns article summaries/content; quality depends on Wikipedia coverage of the topic.
- Sub-node — connect to AI Agent's Tools input.

**Source:** n8n-nodes-langchain.toolwikipedia.md  [doc-verified]
