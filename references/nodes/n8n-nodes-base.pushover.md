# Pushover  (`n8n-nodes-base.pushover`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: pushoverApi
- resources: message
- operations: push

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | message |  |  |
| `operation` | Operation | options | push |  | res=message |
| `userKey` | User Key | string |  | true | res=message,op=push |
| `message` | Message | string |  | true | res=message,op=push |
| `priority` | Priority | options |  |  | res=message,op=push |
| `retry` | Retry (Seconds) | number | 30 | true | res=message,op=push |
| `expire` | Expire (Seconds) | number | 30 | true | res=message,op=push |
| `additionalFields` | Additional Fields | collection | {} |  | res=message,op=push |
