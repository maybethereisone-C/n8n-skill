# Emelia Trigger — `n8n-nodes-base.emeliaTrigger`
**Type** `n8n-nodes-base.emeliaTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on cold email campaign events from Emelia (cold-mailing tool).

**Credentials:** `emeliApi` (API key).

**Resources / Operations:**
| Event |
|---|
| Email Bounced |
| Email Opened |
| Email Replied |
| Email Sent |
| Link Clicked |
| Unsubscribed Contact |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with Emelia on activation.
- Companion app node: `n8n-nodes-base.emelia`.

**Source:** n8n-nodes-base.emeliatrigger.md  [doc-verified]
