# Copper Trigger  (`n8n-nodes-base.copperTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: copperApi
- resources: company, customerSource, lead, opportunity, person, project, task, user
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options |  | true |  |
| `event` | Event | options |  | true |  |
