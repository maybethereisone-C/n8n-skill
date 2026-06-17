# Nextcloud — `n8n-nodes-base.nextcloud`
**Type** `n8n-nodes-base.nextcloud` · **typeVersion** 1 · **action**
**What:** Manage files, folders, and users in a self-hosted or cloud Nextcloud instance — including upload, download, share, move, copy, and user provisioning.
**Credentials:** `nextcloudApi`

## Resources / Operations

| Resource | Operation |
|---|---|
| File | Copy |
| File | Delete |
| File | Download |
| File | Move |
| File | Share |
| File | Upload |
| Folder | Copy |
| Folder | Create |
| Folder | Delete |
| Folder | List Contents |
| Folder | Move |
| Folder | Share |
| User | Invite |
| User | Delete |
| User | Get |
| User | Get Many |
| User | Update |

## Key params & gotchas

- Paths are WebDAV paths (e.g., `/remote.php/dav/files/<username>/MyFolder/`); omitting the leading slash causes 404 errors.
- **File → Download** returns binary data; wire the output to a Write Binary File node or use the binary data directly in downstream nodes.
- **File/Folder → Share** returns a share link; the share type (public link, user share, group share) must be specified as a parameter.
- **User → Invite** creates a new Nextcloud account and sends an invitation email — requires admin-level credentials.
- The node supports AI tool use (can be used as a tool in AI agent workflows).

**Source:** n8n-nodes-base.nextcloud.md  [doc-verified]
