# Onfleet  (`n8n-nodes-base.onfleet`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: onfleetApi
- resources: admin, container, destination, hub, organization, recipient, task, team, webhook, worker
- operations: addTask, autoDispatch, clone, complete, create, delete, get, getAll, getDelegatee, getSchedule, getTimeEstimates, setSchedule, update, updateTask

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | task |  |  |
