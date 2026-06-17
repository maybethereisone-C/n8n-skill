# LinkedIn — `n8n-nodes-base.linkedin`
**Type** `n8n-nodes-base.linkedin` · **typeVersion** 1 · **action**
**What:** Create LinkedIn posts as a person or organization.
**Credentials:** `linkedInOAuth2Api` (OAuth2).

## Resources / Operations
| Resource | Operations |
|---|---|
| Post | Create |

## Key params & gotchas
- **Post As**: `Person` uses the authenticated user's profile; `Organization` requires the numeric organization ID (not URN prefix — enter `03262013` not `urn:li:company:03262013`).
- **Media Category**: required when including images (`IMAGE`) or article links (`ARTICLE`) — omit for text-only posts.
- LinkedIn's API restricts posting frequency and content; automated posts may be flagged by LinkedIn's spam detection.
- OAuth2 scopes needed: `w_member_social` for person posts; `w_organization_social` for org posts.
- LinkedIn does not expose read/delete post operations in this node — post management must be done in the LinkedIn UI.

**Source:** n8n-nodes-base.linkedin.md  [doc-verified]
