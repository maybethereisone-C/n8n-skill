# Microsoft Entra ID  (`n8n-nodes-base.microsoftEntra`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: microsoftEntraOAuth2Api
- resources: group, user
- operations: ={{ { "added": true } }}, ={{ { "deleted": true } }}, ={{ { "removed": true } }}, ={{ { "updated": true } }}, addGroup, create, delete, get, getAll, removeGroup, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | user |  |  |
