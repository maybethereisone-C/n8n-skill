# Drift  (`n8n-nodes-base.drift`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: driftApi, driftOAuth2Api
- resources: contact
- operations: create, delete, get, getCustomAttributes, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | contact |  |  |
