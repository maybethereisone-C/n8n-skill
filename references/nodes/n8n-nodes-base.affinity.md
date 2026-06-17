# Affinity  (`n8n-nodes-base.affinity`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: affinityApi
- resources: list, listEntry, organization, person
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | organization |  |  |
| `events` | Events | multiOptions | [] | true |  |
