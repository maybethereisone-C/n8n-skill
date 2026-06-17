# SeaTable  (`n8n-nodes-base.seaTable`)

- typeVersion (max): **2**  | group: output  | trigger: no
- credentials: seaTableApi
- resources: asset, base, link, row
- operations: add, collaborator, create, delete, get, getAll, getPublicURL, list, lock, metadata, remove, search, snapshot, unlock, update, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `tableName` | Table Name or ID | options |  | true |  |
| `event` | Event | options | rowCreated |  |  |
| `simple` | Simplify | boolean | true |  |  |
| `resource` | Resource | options | row |  |  |
| `viewName` | View Name | options |  |  |  |
| `assetColumn` | Signature Column | options |  | true |  |
| `options` | Options | collection | {} |  |  |
| `notice` | "Fetch Test Event" returns max. three items of the last hour. | notice |  |  |  |
