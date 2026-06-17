# GetResponse  (`n8n-nodes-base.getResponse`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: getResponseApi, getResponseOAuth2Api
- resources: contact
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiKey |  |  |
| `resource` | Resource | options | contact |  |  |
| `events` | Events | multiOptions | [] | true |  |
| `listIds` | List Names or IDs | multiOptions | [] |  |  |
| `options` | Options | collection | {} |  |  |
