# Mailchimp — `n8n-nodes-base.mailchimp`
**Type** `n8n-nodes-base.mailchimp` · **typeVersion** 1 · **action**
**What:** Manage Mailchimp email campaigns, audience members, list groups, and member tags.
**Credentials:** `mailchimpApi` (API key) or `mailchimpOAuth2Api` (OAuth2).

## Resources / Operations
| Resource | Operations |
|---|---|
| Campaign | Delete, Get, Get All, Replicate, Resend to Non-Openers, Send |
| List Group | Get All (groups within an audience) |
| Member | Create, Delete, Get, Get All, Update |
| Member Tag | Add Tags, Remove Tags |

## Key params & gotchas
- **Campaign→Send** dispatches the campaign immediately — ensure content and recipient list are finalized; this cannot be undone.
- **Campaign→Resend to Non-Openers** creates a new campaign variant targeting contacts who didn't open the original — the original campaign must be sent first.
- **Member→Create** requires an `email_address` and `status` (`subscribed`, `unsubscribed`, `pending`, `cleaned`); use `pending` to trigger double opt-in.
- **Member Tag** operations require tag names (strings), not IDs.
- **List Group** Get All requires an `audienceId` (list ID) and `interestCategoryId` (group category ID).
- Mailchimp API key encodes the data center (e.g. `us14`) — the node extracts this automatically.

**Source:** n8n-nodes-base.mailchimp.md  [doc-verified]
