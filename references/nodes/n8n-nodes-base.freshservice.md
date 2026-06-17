# Freshservice  (`n8n-nodes-base.freshservice`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: freshserviceApi
- resources: agent, agentGroup, agentRole, announcement, asset, assetType, change, department, location, problem, product, release, requester, requesterGroup, software, ticket
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | agent |  |  |
