# Vonage  (`n8n-nodes-base.vonage`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: vonageApi
- resources: sms
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | sms |  |  |
| `operation` | Operation | options | send |  | res=sms |
| `from` | From | string |  |  | res=sms,op=send |
| `to` | To | string |  |  | res=sms,op=send |
| `type` | Type | options | text |  | res=sms,op=send |
| `binaryPropertyName` | Input Binary Field | string | data | true | res=sms,op=send |
| `body` | Body | string |  |  | res=sms,op=send |
| `udh` | UDH | string |  |  | res=sms,op=send |
| `title` | Title | string |  |  | res=sms,op=send |
| `url` | URL | string |  |  | res=sms,op=send |
| `validity` | Validity (in minutes) | number | 0 |  | res=sms,op=send |
| `message` | Message | string |  |  | res=sms,op=send |
| `vcard` | VCard | string |  |  | res=sms,op=send |
| `vcal` | VCal | string |  |  | res=sms,op=send |
| `additionalFields` | Additional Fields | collection | {} |  | res=sms,op=send |
