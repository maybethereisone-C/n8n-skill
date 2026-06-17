# Baserow  (`n8n-nodes-base.baserow`)

- typeVersion (max): **1.1**  | group: output  | trigger: no
- credentials: baserowApi, baserowTokenApi
- resources: row
- operations: batchCreate, batchDelete, batchUpdate, create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | usernamePassword |  |  |
| `resource` | Resource | options | row |  |  |
| `operation` | Operation | options | getAll |  | res=row |
