# MCP Client  (`@n8n/n8n-nodes-langchain.mcpClient`)

- typeVersion (max): **1.1**  | group: transform  | trigger: no
- credentials: —

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `endpointUrl` | MCP Endpoint URL | string |  | true |  |
| `authentication` | Authentication | options | none |  |  |
| `credentials` | Credentials | credentials |  |  |  |
| `tool` | Tool | resourceLocator |  | true |  |
| `inputMode` | Input Mode | options | manual |  |  |
| `parameters` | Parameters | resourceMapper |  | true |  |
| `jsonInput` | JSON | json | {\n  "my_field_1": "value",\n  "my_field_2": 1\n}\n |  |  |
| `options` | Options | collection | {} |  |  |
