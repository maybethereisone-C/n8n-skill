# Chargebee Trigger — `n8n-nodes-base.chargebeeTrigger`
**Type** `n8n-nodes-base.chargebeeTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on subscription and billing events from Chargebee (subscription billing platform for SaaS/eCommerce).

**Credentials:** `chargebeeApi` (site name + API key).

**Resources / Operations:**
| Trigger type | What fires it |
|---|---|
| Webhook | Any event type configured in the Chargebee webhook (subscription created/cancelled/renewed, invoice generated, payment succeeded/failed, etc.) |

**Key params & gotchas:**
- Webhook-based. Manual setup required: in Chargebee go to **Settings > Configure Chargebee > Webhooks > Add Webhook**, paste the n8n webhook URL.
- Event type selection happens in Chargebee's webhook config — n8n receives all subscribed event types at this single trigger.
- Chargebee webhook payload includes `event_type` field for downstream branching.

**Source:** n8n-nodes-base.chargebeetrigger.md  [doc-verified]
