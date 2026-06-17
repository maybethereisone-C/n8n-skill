# Microsoft Graph Security — `n8n-nodes-base.microsoftGraphSecurity`
**Type** `n8n-nodes-base.microsoftGraphSecurity` · **typeVersion** 1 · **action**
**What:** Read and update Microsoft Secure Score data and control profiles via the Microsoft Graph Security API.
**Credentials:** Microsoft OAuth2 (`microsoftOAuth2Api`) — requires `SecurityEvents.Read.All` / `SecurityEvents.ReadWrite.All` scopes.
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Secure Score | Get, Get All |
| Secure Score Control Profile | Get, Get All, Update |

**Key params & gotchas:**
- Government cloud tenants (US Gov, US Gov DOD, China) must set the correct **Microsoft Graph API Base URL** in the credential — the default points to commercial endpoints and will 401 on gov tenants.
- Secure Scores are computed daily; "Get All" returns a list of historical score snapshots, not a current single value.

**Source:** n8n-nodes-base.microsoftgraphsecurity.md  [doc-verified]
