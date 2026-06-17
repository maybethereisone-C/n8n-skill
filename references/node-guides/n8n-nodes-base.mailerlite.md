# MailerLite — `n8n-nodes-base.mailerlite`
**Type** `n8n-nodes-base.mailerlite` · **typeVersion** 1 · **action**
**What:** Manage MailerLite email marketing subscribers.
**Credentials:** `mailerLiteApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Subscriber | Create, Get, Get All, Update |

## Key params & gotchas
- **Subscriber→Create** adds a subscriber by email; include `fields` (custom field key-value pairs) and `groups` (group IDs) as optional parameters.
- No **Delete** or **Unsubscribe** operation — status changes must be done via the MailerLite UI or direct API calls using the HTTP Request node.
- **Get All** supports filtering by type (`active`, `unsubscribed`, `bounced`, `junk`, `unconfirmed`).
- MailerLite uses numeric group IDs — look them up via the MailerLite dashboard URL or their API.
- Classic MailerLite and MailerLite New have different APIs; this node targets the classic API — check your account version.

**Source:** n8n-nodes-base.mailerlite.md  [doc-verified]
