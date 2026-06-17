# Gumroad Trigger — `n8n-nodes-base.gumroadTrigger`
**Type** `n8n-nodes-base.gumroadTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Gumroad commerce events (sales, refunds, disputes, cancellations) via webhook.
**Credentials:** `gumroadApi` / `gumroadOAuth2Api`

## Events / Resources

| Resource (event) | Description |
|---|---|
| sale | New product sale |
| refund | Sale refunded |
| dispute | Dispute opened |
| dispute_won | Dispute resolved in seller's favour |
| cancellation | Subscription cancelled |

## Key params & gotchas
- `resource` — required options field; maps 1:1 to the Gumroad webhook event type.
- `authentication` — `accessToken` (default) or OAuth2.
- Gumroad sends one webhook per event type; create separate trigger nodes if you need to handle multiple events in parallel.

**Source:** n8n-nodes-base.gumroadtrigger.md + schema  [doc-verified]
