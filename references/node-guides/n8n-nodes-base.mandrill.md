# Mandrill — `n8n-nodes-base.mandrill`
**Type** `n8n-nodes-base.mandrill` · **typeVersion** 1 · **action**
**What:** Send transactional emails via Mailchimp's Mandrill (transactional email service) using templates or raw HTML.
**Credentials:** `mandrillApi` (API key — requires a paid Mailchimp account with Mandrill add-on).

## Resources / Operations
| Resource | Operations |
|---|---|
| Message | Send via Template, Send via HTML |

## Key params & gotchas
- **Send via Template** requires a Mandrill template slug (not display name) and `merge_vars` for Handlebars/Merge tag substitution.
- **Send via HTML** accepts raw `html` and `text` fields — useful for dynamic content that can't be pre-templated.
- Mandrill requires a **paid Mailchimp plan** — free Mailchimp accounts cannot use Mandrill.
- Mandrill API key is separate from Mailchimp API key — generate it in the Mailchimp account under Transactional.
- Attachments are base64-encoded in the request body — large attachments increase payload size significantly.

**Source:** n8n-nodes-base.mandrill.md  [doc-verified]
