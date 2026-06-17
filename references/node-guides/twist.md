# Twist — `n8n-nodes-base.twist`
**Type** `n8n-nodes-base.twist` · **typeVersion** 1 · **action**
**What:** Manage channels, threads, comments, and direct messages in Twist (team communication app by Doist).
**Credentials:** `twistOAuth2Api` (OAuth2).
**Resources / Operations:**
| Resource | Operation |
|----------|-----------|
| Channel | Archive, Create (conversation), Delete, Get, Get All, Unarchive, Update |
| Comment | Create, Delete, Get, Get All, Update |
| Message Conversation | Create, Delete, Get, Get All, Update |
| Thread | Create, Delete, Get, Get All, Update |

**Key params & gotchas:**
- User ID is found in the URL after `/u/` — e.g., `https://twist.com/a/4qw45/people/u/475370` → User ID is `475370`.
- "Channel" in Twist maps to a workspace channel (not a DM); "Message Conversation" is a direct/group message thread.
- Creating a channel requires a workspace ID.

**Source:** n8n-nodes-base.twist.md  [doc-verified]
