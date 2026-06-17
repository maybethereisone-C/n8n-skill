# Google Cloud Realtime Database  (`n8n-nodes-base.googleFirebaseRealtimeDatabase`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: googleFirebaseRealtimeDatabaseOAuth2Api
- operations: create, delete, get, push, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `projectId` | Project Name or ID | options |  | true |  |
| `operation` | Operation | options | create | true |  |
| `path` | Object Path | string |  | true | op=get |
| `attributes` | Columns / Attributes | string |  | true | op=create,op=push,op=update |
