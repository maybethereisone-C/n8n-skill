# Customer.io Trigger  (`n8n-nodes-base.customerIoTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: customerIoApi
- resources: campaign, customer, event, segment
- operations: add, delete, get, getAll, getMetrics, remove, track, trackAnonymous, upsert

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `events` | Events | multiOptions | [] | true |  |
| `resource` | Resource | options | customer |  |  |
