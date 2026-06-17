# Customer.io Trigger — `n8n-nodes-base.customerIoTrigger`
**Type** `n8n-nodes-base.customerIoTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on messaging and customer lifecycle events from Customer.io (behavioral email/push/SMS platform).

**Credentials:** `customerIoApi` (reporting API key — different from the tracking API key).

**Resources / Operations:**
| Resource | Events |
|---|---|
| Customer | Subscribed · Unsubscribed |
| Email | Bounced · Clicked · Converted · Delivered · Drafted · Failed · Opened · Sent · Spammed |
| Push | Attempted · Bounced · Clicked · Delivered · Drafted · Failed · Opened · Sent |
| Slack | Attempted · Clicked · Drafted · Failed · Sent |
| SMS | Attempted · Bounced · Clicked · Delivered · Drafted · Failed · Sent |

**Key params & gotchas:**
- Webhook-based. Configure the webhook in Customer.io under **Integrations > Reporting Webhooks**.
- Use the **Reporting API key** (not the Tracking API key) for credentials.
- Companion app node: `n8n-nodes-base.customerIo`.

**Source:** n8n-nodes-base.customeriotrigger.md  [doc-verified]
