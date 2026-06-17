# Microsoft Outlook Trigger — `n8n-nodes-base.microsoftOutlookTrigger`
**Type** `n8n-nodes-base.microsoftOutlookTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a new email message is received in a Microsoft Outlook mailbox.
**Credentials:** `microsoftOutlookOAuth2Api` (OAuth2 — Microsoft account).
**Resources / Operations:**
| Event | Notes |
|---|---|
| Message Received | New email arrives in watched folder |

**Key params & gotchas:**
- **Government Cloud** tenants must set the correct **Microsoft Graph API Base URL** in the credential.
- Polling-based (Graph API delta); not instant — latency depends on poll interval.
- Configure **Folder** to watch Inbox, a specific folder, or a shared mailbox folder.
- Use **Filters** (sender, subject contains, etc.) to avoid processing every message.
- Marks messages as read by default after reading — disable with **Mark as Read = false** if you need to preserve unread state.

**Source:** n8n-nodes-base.microsoftoutlooktrigger.md  [doc-verified]
