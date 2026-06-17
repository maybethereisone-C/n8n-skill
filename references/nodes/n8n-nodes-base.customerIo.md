# Customer.io  (`n8n-nodes-base.customerIo`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: customerIoApi
- resources: campaign, customer, event, segment
- operations: add, delete, get, getAll, getMetrics, remove, track, trackAnonymous, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | customer |  |  |
| `events` | Events | multiOptions | [] | true |  |
