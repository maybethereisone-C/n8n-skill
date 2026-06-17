# Mailcheck — `n8n-nodes-base.mailcheck`
**Type** `n8n-nodes-base.mailcheck` · **typeVersion** 1 · **action**
**What:** Verify email addresses for deliverability, disposable domains, and typos using Mailcheck.
**Credentials:** `mailcheckApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Email | Check |

## Key params & gotchas
- **Email→Check** returns fields including `valid` (boolean), `disposable` (boolean), `did_you_mean` (typo suggestion), and `mx_found`.
- Use to gate list imports — filter out `disposable: true` or `valid: false` before adding to campaigns.
- Single email per operation; loop with Split In Batches for bulk verification.
- API credit consumption applies per check.

**Source:** n8n-nodes-base.mailcheck.md  [doc-verified]
