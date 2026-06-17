# SendGrid — `n8n-nodes-base.sendgrid`
**Type** `n8n-nodes-base.sendgrid` · **action**
**What:** Send transactional emails and manage SendGrid marketing contacts and lists.
**Credentials:** `sendGridApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Contact | Create/Update, Delete, Get by ID, Get All |
| List | Create, Delete, Get, Get All, Update |
| Mail | Send an email |

## Key params & gotchas
- Supports use as an AI tool node.
- **Mail → Send**: supports `to`, `from`, `subject`, `text`/`html` body, `cc`, `bcc`, attachments, and dynamic template IDs. `from` address must be a verified sender in SendGrid.
- **Contact Create/Update** upserts by email; custom fields require additional setup in SendGrid and use their field IDs.
- **Contact Delete** requires contact IDs (not emails) — use Get All to look up IDs first.
- SendGrid enforces sender verification; unverified `from` addresses return 403.
- Dynamic templates use Handlebars syntax; pass `templateId` and `dynamicTemplateData` via Additional Fields.
- API key needs appropriate scopes: `Mail Send`, `Marketing` for contact/list operations.

**Source:** n8n-nodes-base.sendgrid.md  [doc-verified]
