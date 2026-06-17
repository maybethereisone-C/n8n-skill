# Stripe — `n8n-nodes-base.stripe`
**Type** `n8n-nodes-base.stripe` · **typeVersion** 1 · **action**
**What:** Manage Stripe payments, customers, charges, coupons, cards, sources, tokens, and usage-based meter events.
**Credentials:** `stripeApi`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Balance | Get |
| Charge | Create, Get, Get All, Update |
| Coupon | Create, Get All |
| Customer | Create, Delete, Get, Get All, Update |
| Customer Card | Add, Get, Remove |
| Meter Event | Create |
| Source | Create, Delete, Get |
| Token | Create |

**Key params & gotchas:**
- Meter Event is for Stripe usage-based billing (new metered billing API) — requires a meter ID.
- Charges use amount in smallest currency unit (cents for USD); forgetting this causes 100x errors.
- Customer Card requires a customer ID and a Stripe token (from Token→Create or frontend Stripe.js).
- Source is the legacy payment source object; prefer Payment Methods for new integrations.
- Companion trigger node (`n8n-nodes-base.stripeTrigger`) available for webhook events.

**Source:** n8n-nodes-base.stripe.md  [doc-verified]
