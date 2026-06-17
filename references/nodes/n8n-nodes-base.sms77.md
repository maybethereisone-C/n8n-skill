# seven  (`n8n-nodes-base.sms77`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: sms77Api
- resources: sms, voice
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | sms |  |  |
| `operation` | Operation | options | send |  | res=sms |
| `operation` | Operation | options | send |  | res=voice |
| `from` | From | string |  |  | res=sms,op=send |
| `to` | To | string |  | true | res=sms,res=voice,op=send |
| `message` | Message | string |  | true | res=sms,res=voice,op=send |
| `options` | Options | collection | {} |  | res=sms,op=send |
| `options` | Options | collection | {} |  | res=voice,op=send |
