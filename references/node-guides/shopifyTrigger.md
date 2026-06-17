# Shopify Trigger — `n8n-nodes-base.shopifyTrigger`
**Type** `n8n-nodes-base.shopifyTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Shopify store events (orders, products, customers, etc.) via webhook.
**Credentials:** `shopifyApi` (API key + password + store name) or OAuth.
**Resources / Operations:**
| Event category | Notes |
|---|---|
| orders/create, orders/updated, orders/paid, orders/cancelled, orders/fulfilled | Order lifecycle |
| products/create, products/update, products/delete | Catalog changes |
| customers/create, customers/update, customers/delete | Customer events |
| checkouts/create, checkouts/update, checkouts/delete | Checkout events |
| app/uninstalled | App lifecycle |

**Key params & gotchas:**
- Trigger type: **webhook** — Shopify pushes to n8n's webhook URL; no polling.
- Each n8n webhook URL (test vs. production) registers as a separate Shopify webhook. Switching between test and production modes requires re-registering the webhook in Shopify.
- Shopify webhooks have a 5-second delivery timeout; if n8n doesn't respond in time, Shopify will retry.
- Shopify enforces a limit on the number of webhooks per topic per shop.

**Source:** n8n-nodes-base.shopifytrigger.md  [doc-verified]
