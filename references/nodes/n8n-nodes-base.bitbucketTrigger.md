# Bitbucket Trigger  (`n8n-nodes-base.bitbucketTrigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: bitbucketAccessTokenApi, bitbucketApi
- resources: repository, workspace

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | password |  |  |
| `resource` | Resource | options | workspace | true |  |
| `workspace` | Workspace Name or ID | options |  | true | res=workspace,res=repository |
| `events` | Event Names or IDs | multiOptions | [] | true | res=workspace |
| `repository` | Repository Name or ID | options |  | true | res=repository |
| `events` | Event Names or IDs | multiOptions | [] | true | res=repository |
