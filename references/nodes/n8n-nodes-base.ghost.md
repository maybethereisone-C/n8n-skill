# Ghost  (`n8n-nodes-base.ghost`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: ghostAdminApi, ghostContentApi
- resources: post
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `source` | Source | options | contentApi |  |  |
| `resource` | Resource | options | post |  |  |
