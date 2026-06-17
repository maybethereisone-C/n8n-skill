# Cal Trigger — `n8n-nodes-base.calTrigger`
**Type** `n8n-nodes-base.calTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on booking lifecycle events from Cal.com (open-source scheduling).

**Credentials:** `calApi` (API key from Cal.com account settings).

**Resources / Operations:**
| Event |
|---|
| Booking cancelled |
| Booking created |
| Booking rescheduled |
| Meeting ended |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with Cal.com on activation.
- "Meeting ended" fires after the event's scheduled end time, not when participants leave.

**Source:** n8n-nodes-base.caltrigger.md  [doc-verified]
