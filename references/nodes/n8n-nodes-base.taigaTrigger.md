# Taiga Trigger  (`n8n-nodes-base.taigaTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: taigaApi
- resources: epic, issue, task, userStory
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `projectId` | Project Name or ID | options |  | true |  |
| `resources` | Resources | multiOptions |  | true |  |
| `operations` | Operations | multiOptions |  | true |  |
| `resource` | Resource | options | issue |  |  |
