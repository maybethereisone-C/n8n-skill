# MySQL  (`n8n-nodes-base.mySql`)

- typeVersion (max): **2.5**  | group: input  | trigger: no
- credentials: —
- resources: database
- operations: deleteTable, executeQuery, insert, select, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | insert |  |  |
| `query` | Query | string |  | true | op=executeQuery |
| `table` | Table | resourceLocator |  | true | op=insert |
| `columns` | Columns | string |  |  | op=insert |
| `options` | Options | collection | LOW_PRIORITY |  | op=insert |
| `table` | Table | resourceLocator |  | true | op=update |
| `updateKey` | Update Key | string | id | true | op=update |
| `columns` | Columns | string |  |  | op=update |
| `resource` | Resource | hidden | database |  |  |
