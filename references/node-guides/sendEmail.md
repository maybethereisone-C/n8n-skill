# Send Email — `n8n-nodes-base.sendEmail`
**Type** `n8n-nodes-base.sendEmail` · **core**

**What:** Sends emails via SMTP, with optional human-in-the-loop approval/response flow.

**Credentials:** SMTP account credential.

**Resources / Operations:**
| Operation | Notes |
|-----------|-------|
| Send | Plain text, HTML, or both formats |
| Send and Wait for Response | Pauses workflow until recipient responds via Approval, Free Text, or Custom Form |

**Key params & gotchas:**
- **From/To Email** support display name format: `Name <email@domain.com>`; To accepts comma-separated list.
- **Email Format** (Send only): Text, HTML, or Both (recipient client chooses).
- **Attachments**: comma-separated binary property names; supports embedded images via `cid:` references.
- **Send and Wait → Response Type**: Approval (approve/decline buttons), Free Text (open form), Custom Form (structured form).
- **Limit Wait Time** on wait operations auto-resumes after a timeout interval or wall time.
- Does **not** support `In-Reply-To`/`References` headers — cannot thread emails. Workaround: use Gmail node's Reply operation.
- **Ignore SSL Issues** bypasses TLS validation for the SMTP connection.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.sendemail.md  [doc-verified]
