# MCP Server Trigger — `@n8n/n8n-nodes-langchain.mcpTrigger`

**Type** `@n8n/n8n-nodes-langchain.mcpTrigger` · **typeVersion** 1 · **trigger · ai**

**What:** Makes n8n act as an MCP server — exposes n8n tool nodes and workflows to external MCP clients (e.g. Claude Desktop, other AI agents).

**Credentials:** Optional: Bearer Auth or Header Auth.

**Resources / Operations:** Single trigger — responds to MCP client tool-list and tool-call requests.

**Key params & gotchas:**

- **Unlike normal triggers** — does not pass output to a next node. Instead, it only connects to and executes Tool nodes (e.g. Custom n8n Workflow Tool, HTTP Request Tool, etc.).
- **Test vs Production URLs** — same pattern as Webhook: Test URL requires "Listen for Test Event"; Production URL requires workflow to be published.
- **Transport** — supports SSE (Server-Sent Events) and streamable HTTP. Does NOT support stdio transport. Claude Desktop requires the `mcp-remote` proxy to bridge SSE→stdio.
- **Path** — auto-generated UUID path by default; customizable for stable endpoint URLs.
- **Queue mode / multiple webhook replicas** — SSE/streamable HTTP are stateful; if you run multiple webhook replicas, all `/mcp*` traffic MUST be routed to a single dedicated replica. Multi-replica without sticky routing causes broken connections.
- **Reverse proxy (nginx)** — must disable proxy buffering for the MCP endpoint; also disable gzip and chunked transfer encoding, and clear the `Connection` header. Example:
  ```nginx
  location /mcp/ {
      proxy_http_version        1.1;
      proxy_buffering           off;
      gzip                      off;
      chunked_transfer_encoding off;
      proxy_set_header          Connection '';
  }
  ```
- **Claude Desktop integration** — use `mcp-remote` via `npx` as the command, passing the MCP URL and `Authorization: Bearer` header via env var.
- Expose n8n workflows as MCP tools by attaching the Custom n8n Workflow Tool node.

**Source:** n8n-nodes-langchain.mcptrigger.md  [doc-verified]
