# Brevo Trigger — `n8n-nodes-base.brevoTrigger`
**Type** `n8n-nodes-base.brevoTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on email delivery and engagement events from Brevo (formerly Sendinblue — email marketing platform).

**Credentials:** `brevoApi` (API key).

**Resources / Operations:**
| Event |
|---|
| Email blocked |
| Email clicked |
| Email deferred |
| Email delivered |
| Email hard bounce |
| Email invalid |
| Email marked spam |
| Email opened |
| Email sent |
| Email soft bounce |
| Email unique open |
| Email unsubscribed |

**Key params & gotchas:**
- Webhook-based. n8n registers the webhook with Brevo automatically on activation.
- "Email unique open" fires only on the first open per recipient; "Email opened" fires on every open.
- Companion app node: `n8n-nodes-base.brevo`.

**Source:** n8n-nodes-base.brevotrigger.md  [doc-verified]
