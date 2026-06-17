# Box  (`n8n-nodes-base.box`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: boxOAuth2Api
- resources: file, folder
- operations: copy, create, delete, download, get, search, share, update, upload

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | file |  |  |
| `events` | Events | multiOptions | [] | true |  |
| `targetType` | Target Type | options |  |  |  |
| `targetId` | Target ID | string |  |  |  |
