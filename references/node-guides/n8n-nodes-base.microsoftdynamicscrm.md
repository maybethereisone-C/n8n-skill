# Microsoft Dynamics CRM — `n8n-nodes-base.microsoftDynamicsCrm`
**Type** `n8n-nodes-base.microsoftDynamicsCrm` · **typeVersion** 1 · **action**
**What:** CRUD operations on Microsoft Dynamics CRM accounts.
**Credentials:** `microsoftDynamicsOAuth2Api` (OAuth2 — Azure AD app registration required).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Account | Create, Delete, Get, Get All, Update |

**Key params & gotchas:**
- Only **Account** entities are supported; for Contacts, Leads, Opportunities — use the HTTP Request node against the Dynamics Web API (`/api/data/v9.x/`).
- Requires the Dynamics 365 environment URL (e.g. `https://yourorg.crm.dynamics.com`) — set in credentials.
- Azure AD app registration needs `Dynamics CRM > user_impersonation` API permission.
- Get All supports OData-style filters; pass them in additional options as `$filter` strings.
- Field names in Dynamics use logical names (snake_case with prefix, e.g. `name`, `accountnumber`) not display names.

**Source:** n8n-nodes-base.microsoftdynamicscrm.md  [doc-verified]
