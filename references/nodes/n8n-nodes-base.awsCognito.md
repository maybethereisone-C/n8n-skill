# AWS Cognito  (`n8n-nodes-base.awsCognito`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: —
- resources: group, user, userPool
- operations: ={{ { "addedToGroup": true } }}, ={{ { "deleted": true } }}, ={{ { "removedFromGroup": true } }}, ={{ { "updated": true } }}, addToGroup, create, delete, get, getAll, removeFromGroup, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | user |  |  |
