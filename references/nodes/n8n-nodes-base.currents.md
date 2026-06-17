# Currents  (`n8n-nodes-base.currents`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: currentsApi
- resources: action, instance, project, run, signature, specFile, test, testResult
- operations: ={{ { "success": true } }}, cancel, cancelGithub, create, delete, disable, enable, find, generate, get, getAll, getInsights, reset, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | run |  |  |
| `noticeGroups` | Currents sends separate webhook events for each group in a run. If your run has multiple groups, you will receive separate events for each group. | notice |  |  |  |
| `events` | Events | multiOptions | [] | true |  |
