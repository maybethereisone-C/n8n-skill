# Twilio Trigger — `n8n-nodes-base.twilioTrigger`
**Type** `n8n-nodes-base.twilioTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when Twilio receives a new inbound SMS or a call completes, via Twilio webhook callback.
**Credentials:** `twilioApi` (Account SID + Auth Token).
**Resources / Operations:**
| Event | Notes |
|---|---|
| On New SMS | Fires when an inbound SMS is received on a Twilio number |
| On New Call | Fires when a completed call summary is available |

**Key params & gotchas:**
- Trigger type: **webhook** — set the n8n webhook URL as the messaging/voice webhook in the Twilio console for the phone number.
- **New Call delay**: Twilio can take up to **30 minutes** after a call ends to generate the summary and fire the webhook — do not use for real-time call handling.
- For SMS: the webhook fires immediately on receipt.
- Twilio signs requests with an `X-Twilio-Signature` header; n8n validates this automatically using the Auth Token.

**Source:** n8n-nodes-base.twiliotrigger.md  [doc-verified]
