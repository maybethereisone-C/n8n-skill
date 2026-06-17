# Read/Write Files from Disk — `n8n-nodes-base.readWriteFile`
**Type** `n8n-nodes-base.readWriteFile` · **core**

**What:** Reads files from (or writes files to) the filesystem of the machine running n8n.

**Credentials:** none.

**Resources / Operations:**
| Operation | Key params |
|-----------|-----------|
| Read File(s) From Disk | File(s) Selector (glob patterns supported: `*`, `**`, `?`, `[]`) |
| Write File to Disk | File Path and Name, Input Binary Field |

**Key params & gotchas:**
- **Read options**: File Extension, File Name, MIME Type, Put Output File in Field (all override metadata in node output).
- **Write option**: Append (add to existing file vs. overwrite).
- **n8n Cloud**: only `/home/node/` is accessible; filesystem is ephemeral — files do not persist across restarts. Use S3/Drive/FTP for persistence.
- **Self-hosted**: defaults to `~/.n8n-files` from n8n 2.0 (`N8N_RESTRICT_FILE_ACCESS_TO` controls allowed paths). Docker paths refer to container filesystem — mount host dirs as volumes.
- Use absolute paths to avoid ambiguity.
- In Docker, paths are container-internal; mount host directories as volumes to access host files.

**Source:** n8n-nodes-base.readwritefile.md  [doc-verified]
