# Medium  (`n8n-nodes-base.medium`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: mediumApi, mediumOAuth2Api
- resources: post, publication
- operations: create, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | accessToken |  |  |
| `resource` | Resource | options | post |  |  |
| `operation` | Operation | options | create |  | res=post |
| `publication` | Publication | boolean | false |  | res=post,op=create |
| `publicationId` | Publication Name or ID | options |  |  | res=post,op=create |
| `title` | Title | string |  | true | res=post,op=create |
| `contentFormat` | Content Format | options |  | true | res=post,op=create |
| `content` | Content | string |  | true | res=post,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=post,op=create |
| `operation` | Operation | options | publication |  | res=publication |
| `returnAll` | Return All | boolean | false |  | res=publication,op=getAll |
| `limit` | Limit | number | 100 |  | res=publication,op=getAll |
