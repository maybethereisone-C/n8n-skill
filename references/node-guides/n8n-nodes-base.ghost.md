# Ghost — `n8n-nodes-base.ghost`
**Type** `n8n-nodes-base.ghost` · **action**
**What:** Manage Ghost CMS posts via Admin API (full CRUD) or read public posts via Content API.
**Credentials:** ghostAdminApi (Admin API key + URL) or ghostContentApi (Content API key + URL).

## Resources / Operations
| API | Resource | Operations |
|---|---|---|
| Admin API | Post | Create, Delete, Get, Get All, Update |
| Content API | Post | Get, Get All |

## Key params & gotchas
- **Admin API** uses a JWT-signed API key (format `id:secret`) — do not confuse with the Content API key.
- **Post Create** defaults to `draft` status; set `status: published` and `published_at` to publish immediately.
- **Content API** is read-only and returns only published posts; no authentication beyond the key is needed.
- Ghost uses Lexical (or Mobiledoc) as internal content format; `html` field is rendered output, `lexical` is the editable format. When creating posts via API, pass `html` (Ghost converts it) or the raw `lexical` JSON.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.ghost.md  [doc-verified]
