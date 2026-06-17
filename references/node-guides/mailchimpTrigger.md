# Mailchimp Trigger — `n8n-nodes-base.mailchimpTrigger`
**Type** `n8n-nodes-base.mailchimpTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Mailchimp audience/list event occurs (subscribe, unsubscribe, profile update, campaign events, etc.) via webhook.
**Credentials:** `mailchimpApi` (API key) or `mailchimpOAuth2Api`.
**Resources / Operations:**
| Event category | Examples |
|---|---|
| Subscriber | Subscribe, unsubscribe, profile update, email change, cleaned |
| Campaign | Sent, opened, clicked |

**Key params & gotchas:**
- Requires selecting a **List/Audience** — the webhook is list-scoped, not account-scoped.
- Mailchimp webhooks only deliver HTTP POST with form-encoded body, not JSON — n8n handles the parse automatically.
- Test/preview sends in Mailchimp do **not** fire webhook events.
- Webhooks created by n8n appear in Mailchimp under **Audience → Settings → Webhooks**.

**Source:** n8n-nodes-base.mailchimptrigger.md  [doc-verified]
