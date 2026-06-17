# TimescaleDB  (`n8n-nodes-base.timescaleDb`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: —
- operations: executeQuery, insert, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | insert |  |  |
| `query` | Query | string |  | true | op=executeQuery |
| `schema` | Schema | string | public | true | op=insert |
| `table` | Table | string |  | true | op=insert |
| `columns` | Columns | string |  |  | op=insert |
| `schema` | Schema | string | public | true | op=update |
| `table` | Table | string |  | true | op=update |
| `updateKey` | Update Key | string | id | true | op=update |
| `columns` | Columns | string |  |  | op=update |
| `returnFields` | Return Fields | string | * |  | op=insert,op=update |
| `additionalFields` | Additional Fields | collection | multiple |  |  |
