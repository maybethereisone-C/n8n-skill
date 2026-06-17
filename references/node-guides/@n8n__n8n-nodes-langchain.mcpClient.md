# MCP Client — `@n8n/n8n-nodes-langchain.mcpClient`

**Type** `@n8n/n8n-nodes-langchain.mcpClient` · **typeVersion** 1.1 · **ai · core**

**What:** Calls tools exposed by an external MCP (Model Context Protocol) server as a regular workflow step — not as an AI Agent tool.

**Credentials:** Bearer Auth, Header Auth, Multiple Headers, or OAuth2 (via HTTP Request credential types); or None.

**Resources / Operations:** Single action — execute a selected MCP tool.

**Key params & gotchas:**

- **Distinction from MCP Client Tool node** — this node is for use in regular workflow steps. To give MCP tools to an AI Agent, use `n8n-nodes-langchain.toolMcp` (MCP Client Tool sub-node) instead.
- **Server Transport** — the protocol the MCP server uses (SSE, streamable HTTP, etc.).
- **MCP Endpoint URL** — the full URL of the MCP server (e.g. `https://mcp.notion.com/mcp`).
- **Tool** — fetched dynamically from the server at configuration time; select from the available tool list.
- **Input Mode:**
  - `Manual` — fill each tool parameter individually in the UI.
  - `JSON` — pass a single JSON object; required for tools with nested or dynamic parameters.
- **Convert to Binary** (option) — when OFF, images/audio return as base64 strings; when ON, they are converted to binary data items.
- **Timeout** (option) — milliseconds to wait for the tool call to complete.
- **Multiple Headers Auth** — use when the MCP server needs more than one header (e.g. API key + tenant ID); set as Name/Value pairs in the credential.

**Source:** n8n-nodes-langchain.mcpClient.md  [doc-verified]
