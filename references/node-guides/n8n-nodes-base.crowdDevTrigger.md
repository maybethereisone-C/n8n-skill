# crowd.dev Trigger — `n8n-nodes-base.crowdDevTrigger`
**Type** `n8n-nodes-base.crowdDevTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on community activity events from crowd.dev (developer community analytics platform).

**Credentials:** `crowdDevApi` (API key + tenant ID).

**Resources / Operations:**
| Event |
|---|
| New Activity |
| New Member |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with crowd.dev on activation.
- "New Activity" covers any cross-channel activity (GitHub stars, Discord messages, Slack posts, etc.) tracked by crowd.dev.
- Companion app node: `n8n-nodes-base.crowdDev`.

**Source:** n8n-nodes-base.crowddevtrigger.md  [doc-verified]
