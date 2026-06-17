# Google Business Profile  (`n8n-nodes-base.googleBusinessProfile`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: googleBusinessProfileOAuth2Api
- resources: post, review
- operations: create, delete, get, getAll, reply, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | post |  |  |
| `event` | Event | options | reviewAdded | true |  |
| `account` | Account | resourceLocator |  | true |  |
| `location` | Location | resourceLocator |  | true |  |
