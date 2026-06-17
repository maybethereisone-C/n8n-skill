# SIGNL4  (`n8n-nodes-base.signl4`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: signl4Api
- resources: alert
- operations: resolve, send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | alert |  |  |
| `operation` | Operation | options | send |  | res=alert |
| `message` | Message | string |  |  | res=alert,op=send |
| `additionalFields` | Additional Fields | collection | single_ack | true | res=alert,op=send |
| `externalId` | External ID | string |  |  | res=alert,op=resolve |
