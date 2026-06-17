# WooCommerce — `n8n-nodes-base.woocommerce`
**Type** `n8n-nodes-base.woocommerce` · **typeVersion** 1 · **action**
**What:** Create, read, update, and delete customers, orders, and products in a WooCommerce store.
**Credentials:** `wooCommerceApi` (store URL + consumer key + consumer secret).

## Resources / Operations
| Resource | Operations |
|---|---|
| Customer | Create, Delete, Get, Get All, Update |
| Order | Create, Delete, Get, Get All, Update |
| Product | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- Credentials use WooCommerce REST API keys (not WordPress login). Generate them under WooCommerce → Settings → Advanced → REST API.
- SSL is required by the WooCommerce API; self-signed certificates will fail unless the n8n instance is configured to skip SSL verification.
- Get All operations support filtering by status (e.g., `pending`, `completed`) and pagination via `per_page`/`page`.
- This node supports use as an **AI tool** (can be called by AI Agent nodes).

**Source:** n8n-nodes-base.woocommerce.md  [doc-verified]
