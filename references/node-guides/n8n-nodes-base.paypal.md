# PayPal — `n8n-nodes-base.paypal`
**Type** `n8n-nodes-base.paypal` · **action**
**What:** Create batch payouts and manage payout items via the PayPal Payouts API.
**Credentials:** `payPalApi` (Client ID + Secret; supports sandbox vs live toggle)

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Payout | Create a batch payout, Show batch payout details |
| Payout Item | Cancel an unclaimed payout item, Show payout item details |

## Key params & gotchas
- Batch payout creation is async — the response returns a `batch_header.payout_batch_id`; poll "Show batch payout details" to get final status.
- Only **unclaimed** items can be cancelled; claimed/completed items cannot be reversed through this node.
- Sandbox and production use different credentials; test in sandbox before switching.
- PayPal Payouts requires explicit feature enablement on the PayPal business account.

**Source:** n8n-nodes-base.paypal.md  [doc-verified]
