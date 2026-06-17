# Brevo  (`n8n-nodes-base.sendInBlue`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: sendInBlueApi
- resources: attribute, contact, email, sender
- operations: ={{ { "success": true } }}, create, delete, get, getAll, send, sendTemplate, update, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | email |  |  |
| `type` | Resource | options | transactional | true |  |
| `events` | Trigger On | multiOptions | [] | true |  |
