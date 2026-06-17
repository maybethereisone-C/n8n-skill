# Shopify  (`n8n-nodes-base.shopify`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: shopifyAccessTokenApi, shopifyApi, shopifyOAuth2Api
- resources: order, product
- operations: create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `apiVersion` | Shopify API Version: 2024-07 | notice |  |  |  |
| `authentication` | Authentication | options | apiKey |  |  |
| `resource` | Resource | options | order |  |  |
| `topic` | Trigger On | options |  |  |  |
