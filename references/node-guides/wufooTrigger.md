# Wufoo Trigger — `n8n-nodes-base.wufooTrigger`
**Type** `n8n-nodes-base.wufooTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Wufoo form receives a new submission, via Wufoo webhook (HandshakeKey-verified).
**Credentials:** `wufooApi` (API key + subdomain).
**Resources / Operations:**
| Event | Notes |
|---|---|
| New Form Entry | Fires on each new form submission |

**Key params & gotchas:**
- Trigger type: **webhook** — Wufoo pushes the form entry data to n8n's webhook URL.
- Select the specific **Form** to watch; n8n registers the webhook automatically on workflow activation.
- Wufoo sends a **HandshakeKey** in the POST body to verify the source — n8n validates this automatically using the API credentials.
- Wufoo's webhook payload uses field IDs (`Field1`, `Field2`, …) rather than labels — map field IDs to labels via the Wufoo API or the form builder's field manager.
- Wufoo does not support multiple webhooks per form; only one endpoint can be registered.

**Source:** n8n-nodes-base.wufootrigger.md  [doc-verified]
