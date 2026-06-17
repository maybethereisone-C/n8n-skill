# Table Name or ID  (`n8n-nodes-base.seaTableApi`)

- typeVersion (max): **1**  | group: -  | trigger: no
- credentials: seaTableApi
- resources: row
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `tableName` | Table Name or ID | options |  | true |  |
| `event` | Event | options | rowCreated |  |  |
| `simple` | Simplify | boolean | true |  |  |
| `resource` | Resource | options | row |  |  |
