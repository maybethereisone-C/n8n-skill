# MSG91  (`n8n-nodes-base.msg91`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: msg91Api
- resources: sms
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | sms |  |  |
| `operation` | Operation | options | send |  | res=sms |
| `from` | Sender ID | string |  | true | res=sms,op=send |
| `to` | To | string |  | true | res=sms,op=send |
| `message` | Message | string |  | true | res=sms,op=send |
