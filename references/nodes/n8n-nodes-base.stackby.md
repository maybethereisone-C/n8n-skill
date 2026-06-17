# Stackby  (`n8n-nodes-base.stackby`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: stackbyApi
- operations: append, delete, list, read

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | append |  |  |
| `stackId` | Stack ID | string |  | true |  |
| `table` | Table | string |  | true |  |
| `id` | ID | string |  | true | op=read,op=delete |
| `returnAll` | Return All | boolean | true |  | op=list |
| `limit` | Limit | number | 1000 |  | op=list |
| `additionalFields` | Additional Fields | collection | {} |  | op=list |
| `columns` | Columns | string |  | true | op=append |
