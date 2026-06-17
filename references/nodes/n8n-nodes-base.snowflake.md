# Snowflake  (`n8n-nodes-base.snowflake`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: snowflakeOAuth2Api
- operations: executeQuery, insert, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | credentials |  |  |
| `operation` | Operation | options | insert |  |  |
| `query` | Query | string |  | true | op=executeQuery |
| `table` | Table | string |  | true | op=insert |
| `columns` | Columns | string |  |  | op=insert |
| `table` | Table | string |  | true | op=update |
| `updateKey` | Update Key | string | id | true | op=update |
| `columns` | Columns | string |  |  | op=update |
