# MailerLite Trigger  (`n8n-nodes-base.mailerLiteTrigger`)

- typeVersion (max): **2**  | group: trigger  | trigger: yes
- credentials: mailerLiteApi
- resources: subscriber
- operations: create, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | subscriber |  |  |
| `event` | Event | options | [] | true |  |
| `events` | Events | multiOptions | [] | true |  |
