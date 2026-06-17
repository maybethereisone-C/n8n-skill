# Hunter — `n8n-nodes-base.hunter`
**Type** `n8n-nodes-base.hunter` · **typeVersion** 1 · **action**
**What:** Find, generate, and verify professional email addresses using Hunter.io.
**Credentials:** `hunterApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| (flat) | Domain Search — get all emails found for a domain |
| (flat) | Email Finder — generate/retrieve the most likely email from domain + first + last name |
| (flat) | Email Verifier — verify deliverability of an email address |

## Key params & gotchas
- **Domain Search** returns emails with sources (web pages where found), confidence scores, and type (`personal`/`generic`).
- **Email Finder** returns the most likely email pattern for a person; confidence < 70 means uncertain — validate with Email Verifier before sending.
- **Email Verifier** checks SMTP, MX records, and disposable/role address flags; `result: deliverable` is the best-case status.
- All operations consume Hunter API credits; verify quotas before bulk processing.

**Source:** n8n-nodes-base.hunter.md  [doc-verified]
