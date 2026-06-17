# WordPress — `n8n-nodes-base.wordpress`
**Type** `n8n-nodes-base.wordpress` · **typeVersion** 1 · **action**
**What:** Create, read, and update posts, pages, and users on a WordPress site via its REST API.
**Credentials:** `wordpressApi` (site URL + username + application password).

## Resources / Operations
| Resource | Operations |
|---|---|
| Post | Create, Get, Get All, Update |
| Pages | Create, Get, Get All, Update |
| User | Create, Get, Get All, Update |

## Key params & gotchas
- Uses WordPress **Application Passwords** (not the main login password). Enable under Users → Profile → Application Passwords (requires WordPress 5.6+).
- No Delete operation for posts/pages — set status to `trash` via Update instead.
- Get All supports `search`, `status`, and `per_page` filters; defaults to published posts only.
- This node supports use as an **AI tool** (can be called by AI Agent nodes).

**Source:** n8n-nodes-base.wordpress.md  [doc-verified]
