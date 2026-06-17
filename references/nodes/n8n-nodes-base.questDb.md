# QuestDB  (`n8n-nodes-base.questDb`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: —
- operations: executeQuery, insert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | insert |  |  |
| `query` | Query | string |  | true | op=executeQuery |
| `schema` | Schema | hidden |  |  | op=insert |
| `table` | Table | string |  | true | op=insert |
| `columns` | Columns | string |  |  | op=insert |
| `returnFields` | Return Fields | string | * |  | op=insert |
| `additionalFields` | Additional Fields | collection | independently |  | op=executeQuery |
| `additionalFields` | Additional Fields | hidden | {} |  | op=insert |
