# Form.io Trigger  (`n8n-nodes-base.formIoTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: formIoApi

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `projectId` | Project Name or ID | options |  | true |  |
| `formId` | Form Name or ID | options |  | true |  |
| `events` | Trigger Events | multiOptions | [] | true |  |
| `simple` | Simplify | boolean | true |  |  |
