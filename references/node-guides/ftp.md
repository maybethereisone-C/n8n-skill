# FTP — `n8n-nodes-base.ftp`
**Type** `n8n-nodes-base.ftp` · **core**

**What:** Accesses and transfers files on FTP or SFTP servers.

**Credentials:** FTP or SFTP credential.

**Resources / Operations:**
| Operation | Key params |
|-----------|-----------|
| Delete | Path; Folder option (+ Recursive for directories) |
| Download | Path, Put Output File in Field |
| List | Path, Recursive |
| Rename | Old Path, New Path; Create Directories option |
| Upload | Path; Binary File toggle (Input Binary Field or File Content) |

**Key params & gotchas:**
- For SFTP use an SFTP credential — the node selects the protocol based on credential type.
- Upload requires a binary file already in the workflow (e.g., from Read/Write Files or HTTP Request node).
- SFTP Download supports **concurrent reads** option for faster transfers — not supported by all servers.
- Rename with **Create Directories** will recursively create the destination path.

**Source:** n8n-nodes-base.ftp.md  [doc-verified]
