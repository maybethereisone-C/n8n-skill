# MCP Client Tool  (`@n8n/n8n-nodes-langchain.mcpClientTool`)

- typeVersion (max): **1.3**  | group: output  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `sseEndpoint` | SSE Endpoint | string |  | true |  |
| `endpointUrl` | Endpoint | string |  | true |  |
| `authentication` | Authentication | options | none |  |  |
| `credentials` | Credentials | credentials |  |  |  |
| `include` | Tools to Include | options | all |  |  |
| `includeTools` | Tools to Include | multiOptions | [] |  |  |
| `excludeTools` | Tools to Exclude | multiOptions | [] |  |  |
| `options` | Options | collection | {} |  |  |
