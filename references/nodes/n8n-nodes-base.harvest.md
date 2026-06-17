# Harvest  (`n8n-nodes-base.harvest`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: harvestApi, harvestOAuth2Api
- resources: client, company, contact, estimate, expense, invoice, project, task, timeEntry, user
- operations: create, createByDuration, createByStartEnd, delete, deleteExternal, get, getAll, me, restartTime, stopTime, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | task |  |  |
| `accountId` | Account Name or ID | options |  | true |  |
