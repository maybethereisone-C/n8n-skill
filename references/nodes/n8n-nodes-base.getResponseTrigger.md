# GetResponse Trigger  (`n8n-nodes-base.getResponseTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: getResponseApi, getResponseOAuth2Api
- resources: contact
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiKey |  |  |
| `events` | Events | multiOptions | [] | true |  |
| `listIds` | List Names or IDs | multiOptions | [] |  |  |
| `options` | Options | collection | {} |  |  |
| `resource` | Resource | options | contact |  |  |
