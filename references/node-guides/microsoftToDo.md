# Microsoft To Do — `n8n-nodes-base.microsoftToDo`
**Type** `n8n-nodes-base.microsoftToDo` · **typeVersion** 1 · **action**
**What:** Manage Microsoft To Do task lists, tasks, and linked web resources via the Microsoft Graph Tasks API.
**Credentials:** Microsoft OAuth2 (`microsoftOAuth2Api`) — requires `Tasks.ReadWrite` scope.
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Linked Resource | Create, Delete, Get, Get All, Update |
| List | Create, Delete, Get, Get All, Update |
| Task | Create, Delete, Get, Get All, Update |

**Key params & gotchas:**
- A **Linked Resource** ties a task to an external URL (e.g., a Jira ticket). You need the task ID and list ID to create one.
- Government cloud tenants must set the correct **Microsoft Graph API Base URL** in the credential.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.microsofttodo.md  [doc-verified]
