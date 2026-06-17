# MailerLite Trigger — `n8n-nodes-base.mailerliteTrigger`
**Type** `n8n-nodes-base.mailerliteTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a MailerLite subscriber or campaign event occurs via webhook.
**Credentials:** `mailerliteApi` (API key).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Subscriber Created | New subscriber added |
| Subscriber Updated | Profile fields changed |
| Subscriber Added to Group | Group membership added |
| Subscriber Removed from Group | Group membership removed |
| Subscriber Unsubscribe | Opt-out |
| Subscriber Bounced | Hard or soft bounce |
| Subscriber Complained | Spam complaint |
| Subscriber Automation Triggered | Automation workflow started |
| Subscriber Automation Completed | Automation workflow finished |
| Campaign Sent | Campaign delivery completed |

**Key params & gotchas:**
- n8n auto-registers the webhook on activation; webhook appears in MailerLite under **Integrations → Webhooks**.
- MailerLite's Classic and New versions have different APIs — ensure your credential targets the correct version.

**Source:** n8n-nodes-base.mailerlitetrigger.md  [doc-verified]
