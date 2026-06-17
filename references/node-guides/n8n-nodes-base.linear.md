# Linear — `n8n-nodes-base.linear`
**Type** `n8n-nodes-base.linear` · **typeVersion** 1 · **action**
**What:** Manage Linear issues and comments for engineering project tracking.
**Credentials:** `linearApi` (API key or OAuth2).

## Resources / Operations
| Resource | Operations |
|---|---|
| Comment | Add Comment (to an issue) |
| Issue | Add Link, Create, Delete, Get, Get Many, Update |

## Key params & gotchas
- **Issue→Create** requires a `teamId` — get team IDs from the Linear workspace settings or via the Linear API.
- **Issue→Add Link** attaches an external URL to an issue (e.g. PR link, Figma URL).
- **Issue→Get Many** supports filtering by team, assignee, state, label, and priority.
- Linear uses GraphQL; IDs are UUIDs — not human-readable names.
- For receiving events (issue created/updated), use the Linear Trigger node (`n8n-nodes-base.linearTrigger`).

**Source:** n8n-nodes-base.linear.md  [doc-verified]
