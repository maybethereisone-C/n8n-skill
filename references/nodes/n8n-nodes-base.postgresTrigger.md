# Postgres Trigger  (`n8n-nodes-base.postgresTrigger`)

- typeVersion (max): **2.6**  | group: trigger  | trigger: yes
- credentials: —
- resources: database
- operations: deleteTable, executeQuery, insert, select, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `triggerMode` | Listen For | options | createTrigger |  |  |
| `schema` | Schema Name | resourceLocator |  | true |  |
| `tableName` | Table Name | resourceLocator |  | true |  |
| `channelName` | Channel Name | string |  | true |  |
| `firesOn` | Event to listen for | options | INSERT |  |  |
| `additionalFields` | Additional Fields | collection | {} |  |  |
| `options` | Options | collection | {} |  |  |
| `operation` | Operation | options | insert |  |  |
| `query` | Query | string |  | true | op=executeQuery |
| `schema` | Schema | string | public | true | op=insert |
| `table` | Table | string |  | true | op=insert |
| `columns` | Columns | string |  |  | op=insert |
| `schema` | Schema | string | public |  | op=update |
| `table` | Table | string |  | true | op=update |
| `updateKey` | Update Key | string | id | true | op=update |
| `columns` | Columns | string |  |  | op=update |
| `returnFields` | Return Fields | string | * |  | op=insert,op=update |
| `resource` | Resource | hidden | database |  |  |
