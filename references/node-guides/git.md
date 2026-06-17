# Git — `n8n-nodes-base.git`
**Type** `n8n-nodes-base.git` · **core**

**What:** Runs Git operations (clone, commit, push, pull, etc.) against a local repository on the n8n server.

**Credentials:** Git credential (for Clone/Push with auth) or none.

**Resources / Operations:**
| Operation | Notes |
|-----------|-------|
| Add | Stage files/folders (`git add`) |
| Add Config | Set/append a git config key |
| Clone | Clone a remote repo; optional auth |
| Commit | Commit staged files with a message |
| Fetch | Fetch from remote |
| List Config | Return current config |
| Log | Return commit history; Return All or Limit |
| Pull | Pull from remote |
| Push | Push to remote; optional Target Repository override |
| Push Tags | Push all tags |
| Status | Return repo status |
| Switch Branch | Checkout a branch |
| Tag | Create a tag |
| User Setup | Configure user identity |

**Key params & gotchas:**
- All operations require **Repository Path** — the local filesystem path on the n8n server.
- Paths in Add/Commit can be absolute or relative to Repository Path.
- Commit's **Paths to Add** option: leave blank to commit all staged files.
- Log's **File** option narrows history to a specific path.

**Source:** n8n-nodes-base.git.md  [doc-verified]
