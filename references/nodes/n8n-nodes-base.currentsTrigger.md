# Currents Trigger  (`n8n-nodes-base.currentsTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: currentsApi
- resources: action, instance, project, run, signature, specFile, test, testResult
- operations: ={{ { "success": true } }}, cancel, cancelGithub, create, delete, disable, enable, find, generate, get, getAll, getInsights, reset, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `noticeGroups` | Currents sends separate webhook events for each group in a run. If your run has multiple groups, you will receive separate events for each group. | notice |  |  |  |
| `events` | Events | multiOptions | [] | true |  |
| `resource` | Resource | options | run |  |  |
