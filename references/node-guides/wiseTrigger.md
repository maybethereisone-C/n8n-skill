# Wise Trigger — `n8n-nodes-base.wiseTrigger`
**Type** `n8n-nodes-base.wiseTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Wise (formerly TransferWise) balance and transfer events via Wise webhook.
**Credentials:** `wiseApi` (API token — use a full-access token, not read-only, for webhook registration).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Balance credited | Balance account receives funds |
| Balance credited or debited | Any balance movement |
| Transfer active cases updated | Transfer's active case list changed |
| Transfer status updated | Transfer moves to a new status (e.g. processing → completed) |

**Key params & gotchas:**
- Trigger type: **webhook** — Wise pushes events to n8n's webhook URL.
- Wise webhooks require a **profile ID** (personal or business) to scope events.
- Transfer status events are the most common use case; statuses include `incoming_payment_waiting`, `processing`, `funds_converted`, `outgoing_payment_sent`, `cancelled`, `bounced_back`, `funds_refunded`.
- Wise sandbox environment uses a separate API token and base URL — test with sandbox credentials before going live.

**Source:** n8n-nodes-base.wisetrigger.md  [doc-verified]
