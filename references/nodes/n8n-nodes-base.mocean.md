# Mocean  (`n8n-nodes-base.mocean`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: moceanApi
- resources: sms, voice
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | sms |  |  |
| `operation` | Operation | options | send |  | res=sms,res=voice |
| `from` | From | string |  | true | res=sms,res=voice,op=send |
| `to` | To | string |  | true | res=sms,res=voice,op=send |
| `language` | Language | options | en-US |  | res=voice,op=send |
| `message` | Message | string |  | true | res=sms,res=voice,op=send |
| `options` | Options | collection | {} |  | res=sms,op=send |
