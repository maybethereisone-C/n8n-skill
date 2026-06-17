# Pushcut  (`n8n-nodes-base.pushcut`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: pushcutApi
- resources: notification
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | notification |  |  |
| `operation` | Operation | options | send |  | res=notification |
| `notificationName` | Notification Name or ID | options |  |  | res=notification,op=send |
| `additionalFields` | Additional Fields | collection | {} |  | res=notification,op=send |
| `actionName` | Action Name | string |  |  |  |
