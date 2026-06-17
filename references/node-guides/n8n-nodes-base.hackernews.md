# Hacker News — `n8n-nodes-base.hackernews`
**Type** `n8n-nodes-base.hackernews` · **typeVersion** 1 · **action**
**What:** Fetch Hacker News articles, users, or the front-page item list; no authentication required.
**Credentials:** None.

## Resources / Operations
| Resource | Operations |
|---|---|
| All | Get All Items (front page / new / top / best / ask / show / job) |
| Article | Get a single article by ID |
| User | Get a user by username |

## Key params & gotchas
- "Get All Items" fetches from HN's live feed endpoints; use **Limit** to cap results.
- Article IDs are integers; the node returns the full item object including `kids` (comment IDs) but does not recursively fetch comments.
- No write operations — HN API is read-only.

**Source:** n8n-nodes-base.hackernews.md  [doc-verified]
