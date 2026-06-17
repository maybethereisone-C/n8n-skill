# WooCommerce Trigger — `n8n-nodes-base.wooCommerceTrigger`
**Type** `n8n-nodes-base.wooCommerceTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on WooCommerce store events (orders, products, customers, coupons) via WooCommerce webhook.
**Credentials:** `wooCommerceApi` (consumer key + consumer secret + store URL).
**Resources / Operations:**
| Event | Notes |
|---|---|
| coupon.created / updated / deleted | Coupon lifecycle |
| customer.created / updated / deleted | Customer lifecycle |
| order.created / updated / deleted | Order lifecycle |
| product.created / updated / deleted | Product lifecycle |

**Key params & gotchas:**
- Trigger type: **webhook** — WooCommerce registers the webhook automatically when the workflow is activated.
- WooCommerce webhooks include the full object payload (order, product, customer, coupon) — no follow-up API call needed.
- `order.updated` fires on every order status transition (pending → processing → completed, etc.) — add an IF node on `status` to filter to specific transitions.
- WooCommerce signs webhook payloads with an HMAC-SHA256 signature in the `X-WC-Webhook-Signature` header; n8n validates this automatically.
- WooCommerce requires HTTPS for webhook delivery.

**Source:** n8n-nodes-base.woocommercetrigger.md  [doc-verified]
