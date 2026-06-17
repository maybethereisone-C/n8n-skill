# Azure Cosmos DB  (`n8n-nodes-base.azureCosmosDb`)

- typeVersion (max): **2**  | group: transform  | trigger: no
- credentials: microsoftAzureCosmosDbSharedKeyApi
- resources: container, item
- operations: ={{ { "deleted": true } }}, create, delete, get, getAll, query, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | container |  |  |
