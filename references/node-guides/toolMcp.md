# MCP Client Tool — `@n8n/n8n-nodes-langchain.toolMcp`

**Type** `@n8n/n8n-nodes-langchain.toolMcp` · **typeVersion** 1 · **ai**

**What:** MCP (Model Context Protocol) client sub-node that exposes an external MCP server's tools to an n8n AI Agent.

**Credentials:** Bearer, generic Header, Multiple Headers, or OAuth2 (via httpRequest credential). Select **None** for unauthenticated servers.

**Resources / Operations:**

| Parameter | Options |
|-----------|---------|
| Tools to Include | All / Selected / All Except |

**Key params & gotchas:**
- **SSE Endpoint**: the Server-Sent Events URL of the MCP server (e.g. `https://my-mcp-server/sse`).
- **Multiple Headers Auth**: use when the server needs >1 header (e.g., API key + username); add each as a Name/Value pair in the credential.
- **All Except** mode: agent gets every MCP tool minus the ones you blacklist — useful when a server exposes dozens of tools and you want to exclude a few.
- Companion node: **MCP Server Trigger** (`n8n-nodes-langchain.mcpTrigger`) exposes *n8n* tools to external agents (inverse direction).
- Sub-node — must connect to an AI Agent node's Tools input.

**Source:** n8n-nodes-langchain.toolmcp.md  [doc-verified]
