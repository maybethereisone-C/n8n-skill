# Microsoft OneDrive — `n8n-nodes-base.microsoftOneDrive`
**Type** `n8n-nodes-base.microsoftOneDrive` · **typeVersion** 1 · **action**
**What:** Create, read, update, delete, share, and search files and folders in Microsoft OneDrive / OneDrive for Business.
**Credentials:** Microsoft OAuth2 (`microsoftOAuth2Api`).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| File | Copy, Delete, Download, Get, Rename, Search, Share, Upload (≤4 MB) |
| Folder | Create, Delete, Get Children, Rename, Search, Share |

**Key params & gotchas:**
- Upload is limited to **4 MB**. For larger files use the Microsoft Graph resumable upload API via HTTP Request node.
- On Microsoft 365 tenants, OneDrive is backed by SharePoint. To get a folder ID, use **Folder → Search** first; the folder ID will not appear in the URL as expected.
- Government cloud tenants must set the correct **Microsoft Graph API Base URL** in the credential.
- "Get Children" retrieves items inside a folder (files + subfolders), not just immediate children metadata.
- Can be used as an AI tool node (usable by AI agents).

**Source:** n8n-nodes-base.microsoftonedrive.md  [doc-verified]
