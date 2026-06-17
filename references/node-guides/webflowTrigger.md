# Webflow Trigger — `n8n-nodes-base.webflowTrigger`
**Type** `n8n-nodes-base.webflowTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Webflow site/CMS/e-commerce events via Webflow webhook.
**Credentials:** `webflowOAuth2Api` or `webflowApi` (site API token).
**Resources / Operations:**
| Event | Notes |
|---|---|
| form_submission | Webflow form submitted |
| site_publish | Site published |
| ecomm_new_order | New e-commerce order |
| ecomm_order_changed | Order status changed |
| ecomm_inventory_changed | Product inventory changed |
| memberships_user_account_added | New membership user |
| memberships_user_account_updated | Membership user updated |
| collection_item_created | CMS collection item created |
| collection_item_changed | CMS collection item changed |
| collection_item_deleted | CMS collection item deleted |
| collection_item_unpublished | CMS item unpublished |

**Key params & gotchas:**
- Trigger type: **webhook** — Webflow registers the webhook automatically when the workflow is activated.
- Scoped to a specific **Site** — select the site in the node parameters.
- Webflow's API v2 (2023+) uses OAuth 2.0; legacy API tokens are site-scoped.

**Source:** n8n-nodes-base.webflowtrigger.md  [doc-verified]
