# Mailjet Trigger — `n8n-nodes-base.mailjetTrigger`
**Type** `n8n-nodes-base.mailjetTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Mailjet email event occurs (sent, opened, clicked, bounced, spam, etc.) via webhook.
**Credentials:** `mailjetEmailApi` (API key + secret).
**Resources / Operations:**
| Event category | Examples |
|---|---|
| Delivery | Sent, bounced, blocked, spam |
| Engagement | Opened, clicked, unsubscribed |

**Key params & gotchas:**
- Mailjet calls these "Event API" webhooks — they must be configured at the Mailjet account level pointing to the n8n webhook URL; n8n does **not** auto-register them.
- A single Mailjet Event API endpoint can receive multiple event types; use a Switch node on the `event` field to branch.
- Sandbox/test messages in Mailjet do not trigger events.

**Source:** n8n-nodes-base.mailjettrigger.md  [doc-verified]
