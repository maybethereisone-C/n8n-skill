# Brevo — `n8n-nodes-base.brevo`
**Type** `n8n-nodes-base.brevo` · **action**
**What:** Manage Brevo (formerly Sendinblue) contacts, attributes, senders, and send transactional emails.
**Credentials:** Brevo API key credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create, Create or Update, Delete, Get, Get All, Update |
| Contact Attribute | Create, Delete, Get All, Update |
| Email | Send, Send Template |
| Sender | Create, Delete, Get All |

## Key params & gotchas
- **Contact/Create or Update** upserts by email address — safe for idempotent sync workflows.
- **Contact Attribute** manages custom contact fields (not standard fields like email/name). Must create attributes before using them in contacts.
- **Email/Send Template** requires a template ID from Brevo's template library and `params` object for variable substitution.
- **Email/Send** sends transactional emails; sender must be a verified sender identity in Brevo.
- Contact lists are not directly managed here — use the HTTP Request node with Brevo API for list operations.

**Source:** n8n-nodes-base.brevo.md  [doc-verified]
