# Linear  (`n8n-nodes-base.linear`)

- typeVersion (max): **1.1**  | group: output  | trigger: no
- credentials: linearApi, linearOAuth2Api
- resources: comment, issue
- operations: addComment, addLink, create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiToken |  |  |
| `resource` | Resource | options | issue |  |  |
| `notice` | Make sure your credential has the "Admin" scope to create webhooks. | notice |  |  |  |
| `teamId` | Team Name or ID | options |  |  |  |
