# Google Business Profile Trigger  (`n8n-nodes-base.googleBusinessProfileTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: googleBusinessProfileOAuth2Api
- resources: post, review
- operations: create, delete, get, getAll, reply, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `event` | Event | options | reviewAdded | true |  |
| `account` | Account | resourceLocator |  | true |  |
| `location` | Location | resourceLocator |  | true |  |
| `resource` | Resource | options | post |  |  |
