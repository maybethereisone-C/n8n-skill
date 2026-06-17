# Microsoft OneDrive Trigger — `n8n-nodes-base.microsoftOneDriveTrigger`
**Type** `n8n-nodes-base.microsoftOneDriveTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when files or folders are created or updated in Microsoft OneDrive.
**Credentials:** `microsoftOneDriveOAuth2Api` (OAuth2 — Microsoft account).
**Resources / Operations:**
| Event | Notes |
|---|---|
| On File Created | New file added to watched location |
| On File Updated | Existing file modified |
| On Folder Created | New folder created |
| On Folder Updated | Folder metadata or contents changed |

**Key params & gotchas:**
- **Government Cloud** tenants (US Gov, DOD, China) must set the correct **Microsoft Graph API Base URL** in the credential — the default points to the commercial endpoint.
- Polling-based under the hood (Graph API delta queries) — not true real-time; interval depends on n8n's poll schedule.
- Specify a **Drive ID** and **Folder ID** to scope the watch; leaving blank watches the entire personal OneDrive.

**Source:** n8n-nodes-base.microsoftonedrivetrigger.md  [doc-verified]
