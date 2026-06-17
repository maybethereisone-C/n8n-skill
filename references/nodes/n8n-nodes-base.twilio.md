# Twilio  (`n8n-nodes-base.twilio`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: twilioApi
- resources: call, sms
- operations: make, send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | sms |  |  |
| `operation` | Operation | options | send |  | res=sms |
| `operation` | Operation | options | make |  | res=call |
| `from` | From | string |  | true | res=sms,res=call,op=send,op=make |
| `to` | To | string |  | true | res=sms,res=call,op=send,op=make |
| `toWhatsapp` | To Whatsapp | boolean | false |  | res=sms,op=send |
| `message` | Message | string |  | true | res=sms,op=send |
| `twiml` | Use TwiML | boolean | false |  | res=call,op=make |
| `message` | Message | string |  | true | res=call,op=make |
| `options` | Options | collection | {} |  |  |
| `updates` | Trigger On | multiOptions | [] | true |  |
| `callTriggerNotice` | The 'New Call' event may take up to thirty minutes to be triggered | notice |  |  |  |
