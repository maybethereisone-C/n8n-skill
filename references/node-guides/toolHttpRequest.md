# HTTP Request Tool (Legacy) — `@n8n/n8n-nodes-langchain.toolHttpRequest`

**Type** `@n8n/n8n-nodes-langchain.toolHttpRequest` · **typeVersion** 1 · **ai**

**What:** Legacy standalone HTTP Request tool sub-node for AI agents; lets an agent call any URL/API. New workflows should use the standard HTTP Request node wired as a tool instead.

**Credentials:** Same as HTTP Request node — Generic Auth, Header Auth, OAuth1/2, Basic Auth, Bearer, etc. (httpRequest credential type).

**Resources / Operations:**

| Category | Detail |
|----------|--------|
| Single operation | Make HTTP request (GET/POST/PUT/PATCH/DELETE) to any URL on behalf of an agent |

**Key params & gotchas:**
- Identify version: if the node has **Add option** when opened, you have the *new* version (HTTP Request node as tool), not this legacy one.
- Legacy version does **not** expose `$fromAI()` field overrides; use the new version for AI-driven parameter control.
- Sub-node — must connect to an AI Agent node's Tools input, not to the main workflow chain.

**Source:** n8n-nodes-langchain.toolhttprequest.md  [doc-verified]
