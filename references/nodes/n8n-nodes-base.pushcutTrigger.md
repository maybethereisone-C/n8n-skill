# Pushcut Trigger  (`n8n-nodes-base.pushcutTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: pushcutApi
- resources: notification
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `actionName` | Action Name | string |  |  |  |
| `resource` | Resource | options | notification |  |  |
| `operation` | Operation | options | send |  | res=notification |
| `notificationName` | Notification Name or ID | options |  |  | res=notification,op=send |
| `additionalFields` | Additional Fields | collection | {} |  | res=notification,op=send |
