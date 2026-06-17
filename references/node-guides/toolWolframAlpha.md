# Wolfram|Alpha Tool — `@n8n/n8n-nodes-langchain.toolWolframAlpha`

**Type** `@n8n/n8n-nodes-langchain.toolWolframAlpha` · **typeVersion** 1 · **ai**

**What:** AI tool sub-node connecting an agent to Wolfram|Alpha's computational intelligence engine for math, science, unit conversions, and factual queries.

**Credentials:** Wolfram|Alpha API key credential.

**Resources / Operations:** No configurable parameters — agent passes a natural-language or symbolic query; node returns Wolfram|Alpha's computed result.

**Key params & gotchas:**
- Requires a Wolfram|Alpha developer API key (free tier available at developer.wolframalpha.com).
- Best for quantitative queries (calculations, conversions, equations, data lookup) rather than open-ended text.
- Sub-node — connect to AI Agent's Tools input.

**Source:** n8n-nodes-langchain.toolwolframalpha.md  [doc-verified]
