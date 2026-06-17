# Clockify  (`n8n-nodes-base.clockify`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: clockifyApi
- resources: client, project, tag, task, timeEntry, user, workspace
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | project |  |  |
| `workspaceId` | Workspace Name or ID | options | [] | true | res=workspace |
| `workspaceId` | Workspace Name or ID | options |  | true |  |
| `watchField` | Trigger | options |  | true |  |
