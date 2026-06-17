# Dropbox — `n8n-nodes-base.dropbox`
**Type** `n8n-nodes-base.dropbox` · **action**
**What:** Upload, download, move, copy, and delete Dropbox files and folders; search file contents.
**Credentials:** dropboxApi (app key/secret + access token) or dropboxOAuth2Api.

## Resources / Operations
| Resource | Operations |
|---|---|
| File | Copy, Delete, Download, Move, Upload |
| Folder | Copy, Create, Delete, List Contents, Move |
| Search | Query |

## Key params & gotchas
- Paths must start with `/` (e.g., `/MyFolder/file.txt`); relative paths are not accepted.
- **Upload** streams binary data from a previous node's binary field; set `Input Binary Field` to match the field name (default `data`).
- **Download** returns binary data — wire to a Write Binary File or subsequent processing node.
- **Move/Copy** require both source and destination paths; destination parent folder must already exist.
- Can be used as an AI tool node.
- "Operation not supported" error may appear for Dropbox Business-only features.

**Source:** n8n-nodes-base.dropbox.md  [doc-verified]
