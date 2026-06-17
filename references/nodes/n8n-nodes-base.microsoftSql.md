# Microsoft SQL  (`n8n-nodes-base.microsoftSql`)

- typeVersion (max): **1.1**  | group: input  | trigger: no
- credentials: —
- operations: delete, executeQuery, insert, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | insert |  |  |
| `query` | Query | string |  | true | op=executeQuery |
| `options` | Options | collection | {} |  | op=executeQuery |
| `table` | Table | string |  | true | op=insert |
| `columns` | Columns | string |  |  | op=insert |
| `table` | Table | string |  | true | op=update |
| `updateKey` | Update Key | string | id | true | op=update |
| `columns` | Columns | string |  |  | op=update |
| `table` | Table | string |  | true | op=delete |
| `deleteKey` | Delete Key | string | id | true | op=delete |
