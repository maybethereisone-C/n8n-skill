# Pushbullet  (`n8n-nodes-base.pushbullet`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: pushbulletOAuth2Api
- resources: push
- operations: create, delete, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | push |  |  |
| `operation` | Operation | options | create |  | res=push |
| `type` | Type | options | note | true | res=push,op=create |
| `title` | Title | string |  | true | res=push,op=create |
| `body` | Body | string |  | true | res=push,op=create |
| `url` | URL | string |  | true | res=push,op=create |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=push,op=create |
| `target` | Target | options | default | true | res=push,op=create |
| `value` | Value | string |  | true | res=push,op=create |
| `pushId` | Push ID | string |  | true | res=push,op=delete |
| `returnAll` | Return All | boolean | false |  | res=push,op=getAll |
| `limit` | Limit | number | 100 |  | res=push,op=getAll |
| `filters` | Filters | collection | {} |  | res=push,op=getAll |
| `pushId` | Push ID | string |  | true | res=push,op=update |
| `dismissed` | Dismissed | boolean | false | true | res=push,op=update |
