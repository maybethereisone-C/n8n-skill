# Microsoft Entra ID — `n8n-nodes-base.microsoftEntra`
**Type** `n8n-nodes-base.microsoftEntra` · **typeVersion** 1 · **action**
**What:** Manages Microsoft Entra ID (Azure AD) users and groups via Microsoft Graph API.
**Credentials:** `microsoftEntraOAuth2Api` (OAuth2 — requires Azure AD app with Graph API permissions).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Group | Create, Delete, Get, Get Many, Update |
| User | Create, Delete, Get, Get Many, Update, Add to Group, Remove from Group |

**Key params & gotchas:**
- **Government Cloud**: select the appropriate Microsoft Graph API Base URL in credentials (default is global; US Gov, US Gov DOD, and China have different endpoints).
- **Update group timing bug**: `allowExternalSenders` and `autoSubscribeNewMembers` cannot be set immediately after group creation — insert a Wait node (≥2 seconds) between Create Group and Update Group operations or the update fails.
- User > Create requires at minimum `displayName`, `mailNickname`, `userPrincipalName`, and `passwordProfile`; omitting any returns a 400.
- Group `objectId` (GUID) is needed for most operations — store it from Create or Get Many responses.
- Required Graph API permissions: `User.ReadWrite.All`, `Group.ReadWrite.All` (application permissions for service principal; delegated for user-context flows).
- Get Many supports `$filter` and `$search` via additional options for large directories.

**Source:** n8n-nodes-base.microsoftentra.md  [doc-verified]
