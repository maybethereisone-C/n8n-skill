# Clearbit — `n8n-nodes-base.clearbit`
**Type** `n8n-nodes-base.clearbit` · **action**
**What:** Enrich companies and persons by domain or email using the Clearbit API.
**Credentials:** clearbitApi (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Company | Auto-complete (name→logo+domain), Lookup (by domain or email) |
| Person | Lookup (by email) |

## Key params & gotchas
- **Company Lookup** accepts either a domain or an email; Clearbit resolves the company from the email domain.
- **Person Lookup** is email-based — it also returns the matched company data in the same response.
- Clearbit returns `null` for unknown records rather than an error; downstream nodes must handle empty payloads.
- Rate limits vary by plan; bulk enrichment workflows should add a Wait node between items.

**Source:** n8n-nodes-base.clearbit.md  [doc-verified]
