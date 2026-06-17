# SSH — `n8n-nodes-base.ssh`
**Type** `n8n-nodes-base.ssh` · **core**

**What:** Executes commands and transfers files on remote servers via SSH/SFTP.

**Credentials:** SSH credential (password or private key).

**Resources / Operations:**
| Operation | Key params |
|-----------|-----------|
| Execute Command | Command, Working Directory |
| Download File | Path (includes filename), File Property (output binary field name) |
| Upload File | Input Binary Field, Target Directory |

**Key params & gotchas:**
- Upload requires binary data already in workflow (from Read/Write Files or HTTP Request node).
- **Download → File Name** option overrides the filename derived from the remote path.
- **Upload → File Name** option overrides the binary data's filename for the remote file.
- Working Directory for Execute applies to the remote machine.

**Source:** n8n-nodes-base.ssh.md  [doc-verified]
