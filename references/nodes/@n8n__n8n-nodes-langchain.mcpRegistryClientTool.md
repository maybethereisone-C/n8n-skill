# MCP Registry Client (internal)  (`@n8n/n8n-nodes-langchain.mcpRegistryClientTool`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: mcpOAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `endpointUrl` | Endpoint URL | hidden |  |  |  |
| `serverTransport` | Server Transport | hidden | httpStreamable |  |  |
| `include` | Tools to Include | options | all |  |  |
| `includeTools` | Tools to Include | multiOptions | [] |  |  |
| `excludeTools` | Tools to Exclude | multiOptions | [] |  |  |
| `options` | Options | collection | {} |  |  |
