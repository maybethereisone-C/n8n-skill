# Monday.com  (`n8n-nodes-base.mondayCom`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: mondayComApi, mondayComOAuth2Api
- resources: board, boardColumn, boardGroup, boardItem
- operations: addUpdate, archive, changeColumnValue, changeMultipleColumnValues, create, delete, get, getAll, getByColumnValue, move

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | board |  |  |
