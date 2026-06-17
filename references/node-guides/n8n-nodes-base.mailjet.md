# Mailjet — `n8n-nodes-base.mailjet`
**Type** `n8n-nodes-base.mailjet` · **typeVersion** 1 · **action**
**What:** Send transactional emails and SMS via Mailjet.
**Credentials:** `mailjetApi` (API key + secret key) — SMS operations use a separate SMS token credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Email | Send Email, Send Email Template |
| SMS | Send SMS |

## Key params & gotchas
- **Email→Send Email Template** requires a Mailjet **Template ID** (integer) and a `Variables` object for template variable substitution.
- **SMS→Send SMS** requires a separate Mailjet SMS token (different from the email API key) — configure in Mailjet's SMS section.
- SMS sender must be pre-registered/approved in Mailjet; unregistered senders are rejected.
- For receiving Mailjet events (bounces, opens), use Mailjet webhooks via an n8n Webhook trigger node.
- A Mailjet Trigger node (`n8n-nodes-base.mailjetTrigger`) also exists for inbound event handling.

**Source:** n8n-nodes-base.mailjet.md  [doc-verified]
