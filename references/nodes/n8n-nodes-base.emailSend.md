# Send Email  (`n8n-nodes-base.emailSend`)

- typeVersion (max): **2.1**  | group: output  | trigger: no
- credentials: —
- resources: email
- operations: send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `fromEmail` | From Email | string |  | true |  |
| `toEmail` | To Email | string |  | true |  |
| `ccEmail` | CC Email | string |  |  |  |
| `bccEmail` | BCC Email | string |  |  |  |
| `subject` | Subject | string |  |  |  |
| `text` | Text | string |  |  |  |
| `html` | HTML | string |  |  |  |
| `attachments` | Attachments | string |  |  |  |
| `options` | Options | collection | {} |  |  |
| `resource` | Resource | hidden | email |  |  |
| `operation` | Operation | options | send |  | res=email |
