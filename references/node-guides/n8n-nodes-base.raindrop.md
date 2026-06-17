# Raindrop — `n8n-nodes-base.raindrop`
**Type** `n8n-nodes-base.raindrop` · **action**
**What:** Manage Raindrop.io bookmarks, collections, tags, and user profile.
**Credentials:** `raindropOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Bookmark | Create, Delete, Get, Get All, Update |
| Collection | Create, Delete, Get, Get All, Update |
| Tag | Delete, Get All |
| User | Get |

## Key params & gotchas
- Bookmark Create requires a URL; title and collection assignment are optional but recommended.
- Collections are nested folders; parent collection ID is needed for sub-collection creation.
- Tag Delete removes the tag from ALL bookmarks in the account — not scoped to a single item.
- OAuth2 app must be created at https://app.raindrop.io/settings/integrations.
- Get All supports pagination; use Return All or set a Limit.

**Source:** n8n-nodes-base.raindrop.md  [doc-verified]
