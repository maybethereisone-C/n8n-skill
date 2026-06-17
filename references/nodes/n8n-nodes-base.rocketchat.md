# RocketChat  (`n8n-nodes-base.rocketchat`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: rocketchatApi
- resources: chat
- operations: postMessage

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | chat |  |  |
| `operation` | Operation | options | postMessage |  | res=chat |
| `channel` | Channel | string |  | true | res=chat,op=postMessage |
| `text` | Text | string |  |  | res=chat,op=postMessage |
| `jsonParameters` | JSON Parameters | boolean | false |  | res=chat,op=postMessage |
| `options` | Options | collection | {} |  | res=chat,op=postMessage |
| `attachments` | Attachments | collection | #ff0000 |  | res=chat,op=postMessage |
| `attachmentsJson` | Attachments | json |  |  | res=chat,op=postMessage |
