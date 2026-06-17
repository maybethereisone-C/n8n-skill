# Mailjet  (`n8n-nodes-base.mailjet`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: mailjetEmailApi, mailjetSmsApi
- resources: email, sms
- operations: send, sendTemplate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | email |  |  |
| `event` | Event | options | open | true |  |
