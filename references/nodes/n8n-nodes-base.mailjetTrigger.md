# Mailjet Trigger  (`n8n-nodes-base.mailjetTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: mailjetEmailApi, mailjetSmsApi
- resources: email, sms
- operations: send, sendTemplate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `event` | Event | options | open | true |  |
| `resource` | Resource | options | email |  |  |
