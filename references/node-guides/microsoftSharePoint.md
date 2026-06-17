# Microsoft SharePoint — `n8n-nodes-base.microsoftSharePoint`
**Type** `n8n-nodes-base.microsoftSharePoint` · **typeVersion** 1 · **action**
**What:** Manage SharePoint list items and files — download, upload, update files; CRUD on list items; read lists.
**Credentials:** Microsoft OAuth2 (`microsoftOAuth2Api`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| File | Download, Update, Upload |
| Item | Create, Create or Update (upsert), Delete, Get, Get Many, Update |
| List | Get, Get Many |

**Key params & gotchas:**
- "Create or Update" is a true upsert — provide the item's unique field to match on.
- List operations return list metadata, not list items; use **Item → Get Many** for item data.
- File operations target a specific SharePoint site's document library; you need the site URL and the library-relative path.

**Source:** n8n-nodes-base.microsoftsharepoint.md  [doc-verified]
