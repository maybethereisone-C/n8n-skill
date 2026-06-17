# AWS SES — `n8n-nodes-base.awsSes`
**Type** `n8n-nodes-base.awsSes` · **action**
**What:** Send emails and manage email templates and custom verification emails via AWS Simple Email Service.
**Credentials:** AWS credential (access key + secret, with SES permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Custom Verification Email | Create template, Delete template, Get template, Get All templates, Add identity, Update template |
| Email | Send, Send Template |
| Template | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- **Sandbox vs Production:** In SES sandbox mode, both sender and recipient must be verified identities. Request production access to send to arbitrary addresses.
- **Email/Send Template** requires a template name and substitution data (JSON key-value pairs matching template variables).
- Custom Verification Email templates have their own API separate from standard SES templates.
- "Add an email address to the list of identities" = send a verification email to that address, not add to a list.
- IAM permissions: `ses:SendEmail`, `ses:SendTemplatedEmail`, `ses:CreateTemplate`, `ses:GetTemplate`, `ses:ListTemplates`, `ses:DeleteTemplate`, `ses:UpdateTemplate`.

**Source:** n8n-nodes-base.awsses.md  [doc-verified]
