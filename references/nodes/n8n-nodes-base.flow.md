# Flow  (`n8n-nodes-base.flow`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: flowApi
- resources: list, task
- operations: create, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | task |  |  |
| `listIds` | Project ID | string |  | true | res=list,res=task |
| `taskIds` | Task ID | string |  | true | res=task,res=list |
