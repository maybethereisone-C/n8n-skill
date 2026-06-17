# MessageBird  (`n8n-nodes-base.messageBird`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: messageBirdApi
- resources: balance, sms
- operations: get, send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | sms |  |  |
| `operation` | Operation | options | send |  | res=sms |
| `operation` | Operation | options | get |  | res=balance |
| `originator` | From | string |  | true | res=sms,op=send |
| `recipients` | To | string |  | true | res=sms,op=send |
| `message` | Message | string |  | true | res=sms,op=send |
| `additionalFields` | Additional Fields | collection | {} |  | res=sms,op=send |
