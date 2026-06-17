# Affinity Trigger  (`n8n-nodes-base.affinityTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: affinityApi
- resources: list, listEntry, organization, person
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Events | multiOptions | [] | true |  |
| `resource` | Resource | options | organization |  |  |
