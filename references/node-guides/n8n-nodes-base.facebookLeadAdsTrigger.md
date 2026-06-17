# Facebook Lead Ads Trigger — `n8n-nodes-base.facebookLeadAdsTrigger`
**Type** `n8n-nodes-base.facebookLeadAdsTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires when a new lead is submitted via Facebook Lead Ads.

**Credentials:** `facebookLeadAdsOAuth2Api` (OAuth2 with Lead Ads permissions).

**Resources / Operations:**
| Event |
|---|
| New lead |

**Key params & gotchas:**
- Webhook-based. Facebook only allows **one webhook per app** — the test URL and production URL cannot both be active simultaneously; whichever was registered last wins.
- To test without breaking production: **Unpublish** (deactivate) the workflow first, test with the test webhook URL, then **Publish** again.
- Only fires for leads submitted through Facebook's lead ads form — not for manually entered CRM data.
- Webhook must be registered via a Facebook App with lead_retrieval permission granted.

**Source:** n8n-nodes-base.facebookleadadstrigger.md  [doc-verified]
