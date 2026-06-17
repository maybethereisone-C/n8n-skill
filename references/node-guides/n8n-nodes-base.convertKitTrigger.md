# ConvertKit Trigger — `n8n-nodes-base.convertKitTrigger`
**Type** `n8n-nodes-base.convertKitTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on subscriber and purchase events from ConvertKit (Kit) email marketing platform.

**Credentials:** `convertKitApi` (API secret).

**Resources / Operations:**
| Event |
|---|
| Form subscribe |
| Link click |
| Product purchase |
| Purchase created |
| Purchase complete |
| Sequence complete |
| Sequence subscribe |
| Subscriber activated |
| Subscriber unsubscribe |
| Tag add |
| Tag remove |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with ConvertKit on activation.
- "Purchase created" and "Purchase complete" are distinct — created fires immediately, complete fires after fulfillment.
- Companion app node: `n8n-nodes-base.convertKit`.

**Source:** n8n-nodes-base.convertkittrigger.md  [doc-verified]
