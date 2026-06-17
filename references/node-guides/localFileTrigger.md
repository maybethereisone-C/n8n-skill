# Local File Trigger — `n8n-nodes-base.localFileTrigger`
**Type** `n8n-nodes-base.localFileTrigger` · **trigger**

**What:** Starts a workflow when files or folders on the local filesystem change (add, modify, delete).

**Credentials:** none.

**Resources / Operations:** Trigger only.

**Key params & gotchas:**
- **Self-hosted n8n only** — not available on n8n Cloud.
- **Disabled by default** from n8n 2.0 due to security risks; must be explicitly enabled via node allow-list.
- **Trigger On**: Changes to a Specific File or Changes Involving a Specific Folder.
- Folder watch options: **Watch for** (file added/changed/deleted), **Include Linked Files/Folders**, **Ignore** (Anymatch glob syntax), **Max Folder Depth**.
- Ignore pattern tests the full path, not just the filename.

**Source:** n8n-nodes-base.localfiletrigger.md  [doc-verified]
