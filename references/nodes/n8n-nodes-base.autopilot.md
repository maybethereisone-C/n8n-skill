# Autopilot  (`n8n-nodes-base.autopilot`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: autopilotApi
- resources: contact, contactJourney, contactList, list
- operations: add, create, delete, exist, get, getAll, remove, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | contact |  |  |
| `event` | Event | options |  | true |  |
