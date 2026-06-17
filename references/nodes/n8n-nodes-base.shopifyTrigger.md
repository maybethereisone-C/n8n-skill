# Shopify Trigger  (`n8n-nodes-base.shopifyTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: shopifyAccessTokenApi, shopifyApi, shopifyOAuth2Api
- resources: order, product
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `authentication` | Authentication | options | apiKey |  |  |
| `topic` | Trigger On | options |  |  |  |
| `apiVersion` | Shopify API Version: 2024-07 | notice |  |  |  |
| `resource` | Resource | options | order |  |  |
