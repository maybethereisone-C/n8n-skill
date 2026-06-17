# Yourls — `n8n-nodes-base.yourls`
**Type** `n8n-nodes-base.yourls` · **typeVersion** 1 · **action**
**What:** Shorten, expand, and get stats for URLs using a self-hosted Yourls instance.
**Credentials:** `yourlsApi` (Yourls instance URL + username + password, or signature token).

## Resources / Operations
| Resource | Operations |
|---|---|
| URL | Expand, Shorten, Get Stats (one short URL) |

## Key params & gotchas
- Requires a self-hosted Yourls installation; there is no cloud Yourls service.
- **Shorten** can accept an optional custom keyword (slug); if the keyword is already taken, the API returns an error rather than the existing URL.
- **Get Stats** returns click counts and metadata for a single short URL, not global site stats.

**Source:** n8n-nodes-base.yourls.md  [doc-verified]
