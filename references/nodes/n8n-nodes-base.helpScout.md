# Help Scout  (`n8n-nodes-base.helpScout`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: helpScoutOAuth2Api
- resources: conversation, customer, mailbox, thread
- operations: create, delete, get, getAll, properties, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | conversation |  |  |
| `events` | Events | multiOptions | [] | true |  |
