# Stripe Trigger — `n8n-nodes-base.stripeTrigger`
**Type** `n8n-nodes-base.stripeTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Stripe events (payments, subscriptions, customers, etc.) via Stripe webhook.
**Credentials:** `stripeApi` (secret key) — webhook signing secret configured separately in Stripe Dashboard.
**Resources / Operations:**
Common Stripe event types (selected in the node):
| Category | Example events |
|---|---|
| Payment | payment_intent.succeeded, payment_intent.payment_failed |
| Charge | charge.succeeded, charge.refunded, charge.disputed |
| Customer | customer.created, customer.updated, customer.deleted |
| Subscription | customer.subscription.created, customer.subscription.deleted |
| Invoice | invoice.payment_succeeded, invoice.payment_failed |
| Checkout | checkout.session.completed |

**Key params & gotchas:**
- Trigger type: **webhook** — Stripe pushes events to n8n's endpoint.
- Stripe webhooks carry a `Stripe-Signature` header; n8n verifies this using the webhook signing secret from the Stripe Dashboard (set in credentials).
- Stripe retries failed webhook deliveries with exponential backoff for up to 72 hours — idempotency handling in downstream nodes is important.
- Test and live mode webhooks are separate in Stripe; ensure the correct secret key (test vs live) matches the webhook endpoint.

**Source:** n8n-nodes-base.stripetrigger.md  [doc-verified]
