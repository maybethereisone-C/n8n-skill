# Help Scout Trigger  (`n8n-nodes-base.helpScoutTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: helpScoutOAuth2Api
- resources: conversation, customer, mailbox, thread
- operations: create, delete, get, getAll, properties, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Events | multiOptions | [] | true |  |
| `resource` | Resource | options | conversation |  |  |
