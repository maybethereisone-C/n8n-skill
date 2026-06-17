# PayPal Trigger — `n8n-nodes-base.paypalTrigger`
**Type** `n8n-nodes-base.paypalTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a PayPal payment or order event occurs via PayPal webhook.
**Credentials:** `payPalApi` (client ID + secret; choose sandbox or live environment).
**Resources / Operations:**
| Event category | Examples |
|---|---|
| Payment | Payment completed, reversed, denied |
| Checkout order | Order created, approved, completed |
| Billing plan / agreement | Subscription created, activated, cancelled |
| Disputes | Dispute opened, resolved |
| Invoices | Invoice created, paid, cancelled |

**Key params & gotchas:**
- n8n auto-registers the PayPal webhook on activation via the PayPal REST API.
- **Sandbox vs Live** — the credential environment must match your PayPal app setting; sandbox webhooks only receive sandbox events.
- PayPal signs webhook payloads (HMAC + certificate); n8n validates this automatically — do not strip headers.
- PayPal may retry unacknowledged webhooks; ensure your workflow completes within the timeout window.

**Source:** n8n-nodes-base.paypaltrigger.md  [doc-verified]
