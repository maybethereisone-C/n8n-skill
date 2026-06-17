# Box Trigger  (`n8n-nodes-base.boxTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: boxOAuth2Api
- resources: file, folder
- operations: copy, create, delete, download, get, search, share, update, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Events | multiOptions | [] | true |  |
| `targetType` | Target Type | options |  |  |  |
| `targetId` | Target ID | string |  |  |  |
| `resource` | Resource | options | file |  |  |
