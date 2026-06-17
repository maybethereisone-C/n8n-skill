# Copper  (`n8n-nodes-base.copper`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: copperApi
- resources: company, customerSource, lead, opportunity, person, project, task, user
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | company |  |  |
| `event` | Event | options |  | true |  |
