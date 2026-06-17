# Zammad  (`n8n-nodes-base.zammad`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: zammadBasicAuthApi, zammadTokenAuthApi
- resources: group, organization, ticket, user
- operations: create, delete, get, getAll, getSelf, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | tokenAuth |  |  |
| `resource` | Resource | options | user |  |  |
