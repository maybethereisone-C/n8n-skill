# Magento 2 — `n8n-nodes-base.magento2`
**Type** `n8n-nodes-base.magento2` · **typeVersion** 1 · **action**
**What:** Manage Magento 2 e-commerce customers, invoices, orders, and products.
**Credentials:** `magento2Api` (base URL + access token or username/password).

## Resources / Operations
| Resource | Operations |
|---|---|
| Customer | Create, Delete, Get, Get All, Update |
| Invoice | Create (from order) |
| Order | Cancel, Get, Get All, Ship |
| Product | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- **Invoice→Create** generates an invoice from an existing order ID — not a standalone invoice; the order must be in a billable state.
- **Order→Ship** marks an order as shipped; optionally pass tracking number and carrier info.
- **Order→Cancel** only works if the order is in a cancellable state (`pending`, `pending_payment`) — attempting to cancel a shipped order errors.
- **Product** requires a valid `attribute_set_id` on create — look up valid IDs from Magento admin or the Magento API.
- Magento's REST API uses bearer tokens; generate an admin token via Magento admin → System → Integrations.
- **Get All** on orders/products supports SearchCriteria filters — use the **Filters** option for field/value/condition triples.

**Source:** n8n-nodes-base.magento2.md  [doc-verified]
