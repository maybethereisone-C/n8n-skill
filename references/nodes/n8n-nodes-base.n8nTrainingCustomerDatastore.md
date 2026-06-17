# Customer Datastore (n8n training)  (`n8n-nodes-base.n8nTrainingCustomerDatastore`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —
- operations: getAllPeople, getOnePerson

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | getOnePerson |  |  |
| `returnAll` | Return All | boolean | false |  | op=getAllPeople |
| `limit` | Limit | number | 5 |  | op=getAllPeople |
