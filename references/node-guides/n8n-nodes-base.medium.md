# Medium — `n8n-nodes-base.medium`
**Type** `n8n-nodes-base.medium` · **typeVersion** 1 · **action**
**What:** Publish posts and retrieve publications on Medium.
**Credentials:** `mediumApi` (Integration Token — existing tokens only).

## Resources / Operations
| Resource | Operations |
|---|---|
| Post | Create |
| Publication | Get All |

## Key params & gotchas
- **DEPRECATED / Non-functional for new users**: Medium stopped supporting API key issuance. Existing API keys may still work but no new keys can be generated.
- **Post→Create** requires `title`, `contentFormat` (`html` or `markdown`), and `content`; optionally set `publishStatus` (`public`, `draft`, `unlisted`) and `tags` (array, max 5).
- **Publication→Get All** returns publications the authenticated user can publish to — use the publication ID for cross-posting.
- Do not build new automations on this node; use the Medium UI or an alternative blogging API.

**Source:** n8n-nodes-base.medium.md  [doc-verified]
