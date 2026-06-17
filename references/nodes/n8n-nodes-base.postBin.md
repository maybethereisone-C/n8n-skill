# PostBin  (`n8n-nodes-base.postBin`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: —
- resources: bin, request
- operations: ={{ { "requestId": $response.body } }}, create, delete, get, removeFirst, send

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | bin | true |  |
