# WhatsApp Business Cloud  (`n8n-nodes-base.whatsApp`)

- typeVersion (max): **1.1**  | group: output  | trigger: no
- credentials: whatsAppTriggerApi
- resources: media, message
- operations: mediaDelete, mediaUpload, mediaUrlGet, send, sendTemplate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | message |  |  |
| `whatsAppNotice` | Due to Facebook API limitations, you can use just one WhatsApp trigger for each Facebook App | notice |  |  |  |
| `updates` | Trigger On | multiOptions | [] | true |  |
| `options` | Options | collection | {} |  |  |
