# Autopilot Trigger  (`n8n-nodes-base.autopilotTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: autopilotApi
- resources: contact, contactJourney, contactList, list
- operations: add, create, delete, exist, get, getAll, remove, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `event` | Event | options |  | true |  |
| `resource` | Resource | options | contact |  |  |
