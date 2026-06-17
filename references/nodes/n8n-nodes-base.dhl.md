# DHL  (`n8n-nodes-base.dhl`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: dhlApi
- resources: shipment
- operations: get

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | hidden | shipment |  |  |
| `operation` | Operation | options | get |  | res=shipment |
| `trackingNumber` | Tracking Number | string |  | true |  |
| `options` | Options | collection | {} |  |  |
