# Disqus — `n8n-nodes-base.disqus`
**Type** `n8n-nodes-base.disqus` · **action**
**What:** Read Disqus forum metadata, categories, threads, and posts.
**Credentials:** disqusApi (API key — public key for read, secret key for moderation).

## Resources / Operations
| Resource | Operations |
|---|---|
| Forum | Get Details, Get Categories, Get Threads, Get Posts |

## Key params & gotchas
- **Read-only** operations only — this node does not create, update, or moderate content.
- All operations require the Disqus **shortname** (forum identifier), not the forum display name.
- Responses are paginated via cursor; use "Return All" cautiously on large forums.

**Source:** n8n-nodes-base.disqus.md  [doc-verified]
