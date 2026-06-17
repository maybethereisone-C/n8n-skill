# Brevo Trigger  (`n8n-nodes-base.sendInBlueApi`)

- typeVersion (max): **1**  | group: trigger  | trigger: no
- credentials: sendInBlueApi
- resources: attribute, contact, email, sender
- operations: ={{ { "success": true } }}, create, delete, get, getAll, send, sendTemplate, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `type` | Resource | options | transactional | true |  |
| `events` | Trigger On | multiOptions | [] | true |  |
| `resource` | Resource | options | email |  |  |
