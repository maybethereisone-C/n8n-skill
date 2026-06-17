# Bitly — `n8n-nodes-base.bitly`
**Type** `n8n-nodes-base.bitly` · **action**
**What:** Create and manage Bitly shortened links.
**Credentials:** Bitly OAuth2 or API token credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Link | Create, Get, Update |

## Key params & gotchas
- **Link/Create** requires a long URL; optionally set custom title, tags, and domain (e.g. `bit.ly` or a custom branded domain).
- **Link/Get** takes a Bitlink ID (e.g. `bit.ly/3xyz`) and returns metadata including click stats.
- **Link/Update** can change the title, tags, and archived status — it cannot change the long URL destination (Bitly limitation on free plans).
- Custom domains require a paid Bitly plan and must be configured in Bitly before use.

**Source:** n8n-nodes-base.bitly.md  [doc-verified]
