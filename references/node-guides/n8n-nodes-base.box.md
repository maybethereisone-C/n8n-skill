# Box — `n8n-nodes-base.box`
**Type** `n8n-nodes-base.box` · **action**
**What:** Manage files and folders in Box cloud storage — upload, download, copy, share, search.
**Credentials:** Box OAuth2 credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| File | Copy, Delete, Download, Get, Search, Share, Upload |
| Folder | Create, Delete, Get, Search, Share, Update |

## Key params & gotchas
- **File/Upload** requires binary input data; set **Binary Property** to the field holding the binary.
- **File/Download** outputs binary data — pipe to Write Binary File to persist.
- **Search** searches within a folder by name/content — not a full-text search across all Box content.
- **Share** creates a shared link on the file/folder; configure access level (open, company, collaborators).
- Box file IDs are numeric strings — use Get to retrieve them if you only know the path.
- OAuth2 requires app approval in Box Developer Console; service accounts work better for automation.

**Source:** n8n-nodes-base.box.md  [doc-verified]
