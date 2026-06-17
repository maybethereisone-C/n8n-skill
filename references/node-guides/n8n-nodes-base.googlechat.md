# Google Chat — `n8n-nodes-base.googleChat`
**Type** `n8n-nodes-base.googleChat` · **typeVersion** 1 · **action**
**What:** Sends, reads, and manages messages in Google Chat spaces; lists memberships and spaces.
**Credentials:** `googleChatOAuth2Api` (OAuth2) or service account (for bot/app scenarios).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Member | Get, Get All (in a space) |
| Message | Create, Delete, Get, Send and Wait for Response, Update |
| Space | Get, Get All |

**Key params & gotchas:**
- **Send and Wait for Response**: human-in-the-loop operation — sends a message and pauses the workflow until a user replies via a form button; requires the Chat app to be installed in the space.
- Service accounts must be added to a space before they can post; OAuth2 acts as the authenticated user.
- Space names use the format `spaces/{spaceId}` — retrieve via Space > Get All.
- Message names use `spaces/{spaceId}/messages/{messageId}` for Get/Delete/Update.
- Bot/app credentials cannot use OAuth2 flow; use a service account JSON key for fully automated (non-user) bots.

**Source:** n8n-nodes-base.googlechat.md  [doc-verified]
