# Eventbrite Trigger — `n8n-nodes-base.eventbriteTrigger`
**Type** `n8n-nodes-base.eventbriteTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on event management and ticketing events from Eventbrite via webhook.

**Credentials:** `eventbriteApi` (private token) or `eventbriteOAuth2Api`.

**Resources / Operations:**
| Trigger type | What fires it |
|---|---|
| Webhook | Eventbrite events selected during node config (attendee.updated, order.placed, event.published, etc.) |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with Eventbrite on activation.
- Event type selection is done within the n8n node; Eventbrite supports a range of webhook actions (attendee, order, event, organizer, ticket class, barcode events).
- Doc is thin on explicit event list — refer to Eventbrite webhook reference for full action catalog.

**Source:** n8n-nodes-base.eventbritetrigger.md  [doc-verified]
