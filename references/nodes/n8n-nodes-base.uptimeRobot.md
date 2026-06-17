# UptimeRobot  (`n8n-nodes-base.uptimeRobot`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: uptimeRobotApi
- resources: account, alertContact, maintenanceWindow, monitor, publicStatusPage
- operations: create, delete, get, getAll, reset, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | account |  |  |
| `operation` | Operation | options | get |  | res=account |
