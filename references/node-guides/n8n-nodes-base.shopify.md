# Shopify — `n8n-nodes-base.shopify`
**Type** `n8n-nodes-base.shopify` · **action**
**What:** Manage Shopify store orders and products.
**Credentials:** `shopifyApi` (API key + password) or `shopifyOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Order | Create, Delete, Get, Get All, Update |
| Product | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- A companion trigger node (`n8n-nodes-base.shopifyTrigger`) handles webhook events (order created, product updated, etc.) — prefer it over polling for real-time flows.
- Order Create requires at minimum `line_items` with variant IDs; customer info is optional but needed for fulfillment.
- Product Create/Update supports variants, images, and metafields via Additional Fields.
- Shopify API enforces per-second and per-day rate limits — use with care in high-volume loops.
- Admin API credentials (API key + secret or access token from a private/custom app) are required; public OAuth2 apps need the merchant to install and grant scopes.
- Store subdomain must be the `.myshopify.com` handle, not a custom domain.

**Source:** n8n-nodes-base.shopify.md  [doc-verified]
