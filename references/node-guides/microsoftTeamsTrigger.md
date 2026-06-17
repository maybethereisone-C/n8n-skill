# Microsoft Teams Trigger — `n8n-nodes-base.microsoftTeamsTrigger`
**Type** `n8n-nodes-base.microsoftTeamsTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when Teams activity occurs — new channels, messages, chats, or team members.
**Credentials:** `microsoftTeamsOAuth2Api` (OAuth2 — Microsoft account; requires Teams API permissions).
**Resources / Operations:**
| Event | Notes |
|---|---|
| New Channel | A channel is created in a team |
| New Channel Message | A message posted to a channel |
| New Chat | A new 1:1 or group chat started |
| New Chat Message | A message sent in a chat |
| New Team Member | A user joins a team |

**Key params & gotchas:**
- **Government Cloud** tenants must set the correct **Microsoft Graph API Base URL** in the credential.
- Polling-based (Graph API); not instant — relies on n8n poll schedule.
- For **New Channel Message** and **New Chat Message**, specify the Team/Channel or Chat ID to narrow the scope; omitting watches all accessible conversations.
- The app registration in Azure AD must have the correct Graph API delegated or application permissions (`ChannelMessage.Read.All`, `Chat.Read`, etc.).

**Source:** n8n-nodes-base.microsoftteamstrigger.md  [doc-verified]
