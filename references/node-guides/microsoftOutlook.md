# Microsoft Outlook — `n8n-nodes-base.microsoftOutlook`
**Type** `n8n-nodes-base.microsoftOutlook` · **typeVersion** 2 · **action**
**What:** Full Outlook mailbox automation: send/receive messages, manage drafts, calendars, contacts, folders, events, and attachments via Microsoft Graph.
**Credentials:** Microsoft OAuth2 (`microsoftOAuth2Api`) — scopes depend on resources used (Mail, Calendars, Contacts).
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Calendar | Create, Delete, Get, Get Many, Update |
| Contact | Create, Delete, Get, Get Many, Update |
| Draft | Create, Delete, Get, Send, Update |
| Event | Create, Delete, Get, Get Many, Update |
| Folder | Create, Delete, Get, Get Many, Update |
| Folder Message | Get Many |
| Message | Delete, Get, Get Many, Move, Reply, Send, Send and Wait for Response, Update |
| Message Attachment | Add, Download, Get, Get Many |

**Key params & gotchas:**
- **Send and Wait for Response** pauses the workflow until the recipient clicks an approve/reject link — useful for human-in-the-loop (HITL) approvals.
- Government cloud tenants must configure the **Microsoft Graph API Base URL** in the credential.
- Moving a message requires a destination folder ID, not a display name.
- Can be used as an AI tool node and supports HITL tool patterns.

**Source:** n8n-nodes-base.microsoftoutlook.md  [doc-verified]
