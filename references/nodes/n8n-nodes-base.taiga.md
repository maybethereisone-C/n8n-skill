# Taiga  (`n8n-nodes-base.taiga`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: taigaApi
- resources: epic, issue, task, userStory
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | issue |  |  |
| `projectId` | Project Name or ID | options |  | true |  |
| `resources` | Resources | multiOptions |  | true |  |
| `operations` | Operations | multiOptions |  | true |  |
