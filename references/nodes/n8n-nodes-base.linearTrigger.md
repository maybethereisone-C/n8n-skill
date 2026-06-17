# Linear Trigger  (`n8n-nodes-base.linearTrigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: linearApi, linearOAuth2Api
- resources: comment, issue
- operations: addComment, addLink, create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiToken |  |  |
| `notice` | Make sure your credential has the "Admin" scope to create webhooks. | notice |  |  |  |
| `teamId` | Team Name or ID | options |  |  |  |
| `resource` | Resource | options | issue |  |  |
