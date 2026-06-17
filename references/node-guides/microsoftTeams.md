# Microsoft Teams — `n8n-nodes-base.microsoftTeams`
**Type** `n8n-nodes-base.microsoftTeams` · **typeVersion** 2 · **action**
**What:** Automate Microsoft Teams: manage channels, post channel messages, send and read chat messages, and manage Planner tasks.
**Credentials:** Microsoft OAuth2 (`microsoftOAuth2Api`) — requires Teams and (for tasks) Planner scopes.
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Channel | Create, Delete, Get, Get Many, Update |
| Channel Message | Create, Get Many |
| Chat Message | Create, Get, Get Many, Send and Wait for Response |
| Task | Create, Delete, Get, Get Many, Update |

**Key params & gotchas:**
- **Chat Message → Send and Wait for Response** pauses the workflow until the recipient responds — useful for HITL approval flows.
- Channel messages post to a team channel (requires Team ID + Channel ID); Chat messages go to a 1:1 or group chat (requires Chat ID).
- Tasks are Microsoft Planner tasks; you need a Plan ID and Bucket ID to create one.
- Government cloud tenants must set the correct **Microsoft Graph API Base URL** in the credential.
- Can be used as an AI tool node and supports HITL tool patterns.

**Source:** n8n-nodes-base.microsoftteams.md  [doc-verified]
