# Autopilot Trigger — `n8n-nodes-base.autopilotTrigger`
**Type** `n8n-nodes-base.autopilotTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on contact lifecycle events from Autopilot (visual marketing automation / customer journey tool).

**Credentials:** `autopilotApi` (API key).

**Resources / Operations:**
| Event |
|---|
| Contact added |
| Contact added to a list |
| Contact entered to a segment |
| Contact left a segment |
| Contact removed from a list |
| Contact unsubscribed |
| Contact updated |

**Key params & gotchas:**
- Webhook-based. Configure the webhook URL in Autopilot under **Settings > Integrations > Webhooks**.
- Companion app node: `n8n-nodes-base.autopilot`.

**Source:** n8n-nodes-base.autopilottrigger.md  [doc-verified]
