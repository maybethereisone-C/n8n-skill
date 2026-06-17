# WooCommerce Trigger  (`n8n-nodes-base.wooCommerceTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: wooCommerceApi
- resources: customer, order, product
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `event` | Event | options |  | true |  |
| `resource` | Resource | options | product |  |  |
