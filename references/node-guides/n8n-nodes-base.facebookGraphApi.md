# Facebook Graph API — `n8n-nodes-base.facebookGraphApi`
**Type** `n8n-nodes-base.facebookGraphApi` · **action**
**What:** Generic Facebook Graph API client — make GET, POST, DELETE requests to any Graph API node/edge.
**Credentials:** facebookGraphApi (access token — page, user, or app token depending on scope).

## Resources / Operations
| Resource | Operations |
|---|---|
| Default | GET, POST, DELETE |
| Video Uploads | GET, POST, DELETE |

## Key params & gotchas
- **Host URL:** `Default` routes to `graph.facebook.com`; `Video` routes to `graph-video.facebook.com` (required for video uploads only).
- **Node** field: the Graph API node path, e.g., `/<page-id>/feed` or `/me/photos`.
- **Edge** field: collections attached to the node (e.g., `photos`, `videos`); leave blank for the node itself.
- **Graph API Version** must be set explicitly (e.g., `v19.0`); using an outdated version may return deprecated fields.
- **Send Binary File** (POST only): enables multipart upload — set `Input Binary Field` to the binary data field name.
- **Ignore SSL Issues**: toggle to bypass SSL validation (not recommended for production).
- Access tokens expire; use long-lived page tokens or handle refresh in the workflow.

**Source:** n8n-nodes-base.facebookgraphapi.md  [doc-verified]
