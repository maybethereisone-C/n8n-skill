# ActiveCampaign Trigger — `n8n-nodes-base.activeCampaignTrigger`
**Type** `n8n-nodes-base.activeCampaignTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on ActiveCampaign webhook events (customer experience automation platform — email, marketing automation, CRM).

**Credentials:** `activeCampaignApi` (API URL + API key).

**Resources / Operations:**
| Event |
|---|
| New ActiveCampaign event (generic — covers any webhook event configured in ActiveCampaign) |

**Key params & gotchas:**
- Webhook-based. n8n auto-registers the webhook URL; configure in ActiveCampaign under **Settings > Developer > Event Tracking / Webhooks**.
- The single "New ActiveCampaign event" option means all event types funnel through one trigger — use an IF/Switch node downstream to branch on `$.event` type if you need to differentiate.
- Companion app node: `n8n-nodes-base.activeCampaign`.

**Source:** n8n-nodes-base.activecampaigntrigger.md  [doc-verified]
