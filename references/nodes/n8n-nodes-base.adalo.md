# Adalo  (`n8n-nodes-base.adalo`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: adaloApi
- resources: collection
- operations: ={{ { "success": true } }}, create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | collection |  |  |
| `operation` | Operation | options | getAll |  |  |
| `collectionId` | Collection ID | string |  | true | res=collection |
