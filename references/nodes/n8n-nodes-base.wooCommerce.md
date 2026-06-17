# WooCommerce  (`n8n-nodes-base.wooCommerce`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: wooCommerceApi
- resources: customer, order, product
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | product |  |  |
| `event` | Event | options |  | true |  |
