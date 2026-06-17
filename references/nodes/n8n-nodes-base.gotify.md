# Gotify  (`n8n-nodes-base.gotify`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: gotifyApi
- resources: message
- operations: create, delete, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | message |  |  |
| `operation` | Operation | options | create |  | res=message |
| `message` | Message | string |  | true | res=message,op=create |
| `additionalFields` | Additional Fields | collection | {} |  | res=message,op=create |
| `options` | Options | collection | text/plain |  | res=message,op=create |
| `messageId` | Message ID | string |  | true | res=message,op=delete |
| `returnAll` | Return All | boolean | false |  | res=message,op=getAll |
| `limit` | Limit | number | 20 |  | res=message,op=getAll |
