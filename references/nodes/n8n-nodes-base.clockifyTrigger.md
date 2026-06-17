# Clockify Trigger  (`n8n-nodes-base.clockifyTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: clockifyApi
- resources: client, project, tag, task, timeEntry, user, workspace
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `workspaceId` | Workspace Name or ID | options |  | true |  |
| `watchField` | Trigger | options |  | true |  |
| `resource` | Resource | options | project |  |  |
| `workspaceId` | Workspace Name or ID | options | [] | true | res=workspace |
