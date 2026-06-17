# WhatsApp Trigger  (`n8n-nodes-base.whatsAppTrigger`)

- typeVersion (max): **1.1**  | group: trigger  | trigger: yes
- credentials: whatsAppTriggerApi
- resources: media, message
- operations: mediaDelete, mediaUpload, mediaUrlGet, send, sendTemplate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `whatsAppNotice` | Due to Facebook API limitations, you can use just one WhatsApp trigger for each Facebook App | notice |  |  |  |
| `updates` | Trigger On | multiOptions | [] | true |  |
| `options` | Options | collection | {} |  |  |
| `resource` | Resource | options | message |  |  |
