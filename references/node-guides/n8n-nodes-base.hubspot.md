# HubSpot — `n8n-nodes-base.hubspot`
**Type** `n8n-nodes-base.hubspot` · **typeVersion** 2 · **action**
**What:** Full CRM operations across HubSpot contacts, companies, deals, engagements, tickets, forms, and contact lists.
**Credentials:** `hubspotApi` (API key) or `hubspotOAuth2Api` (OAuth2).

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create/Update (upsert), Delete, Get, Get All, Get Recently Created/Updated, Search |
| Contact List | Add to List, Remove from List |
| Company | Create, Delete, Get, Get All, Get Recently Created, Get Recently Modified, Search by Domain, Update |
| Deal | Create, Delete, Get, Get All, Get Recently Created, Get Recently Modified, Search, Update |
| Engagement | Create, Delete, Get, Get All |
| Form | Get All Fields, Submit Data |
| Ticket | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- **Contact→Create/Update** upserts by email — sending an existing email updates rather than creating a duplicate.
- **Company→Search by Domain** takes a domain string (not URL), e.g. `acme.com` not `https://acme.com`.
- **Deal→Search** uses HubSpot's filter groups syntax; build filters carefully — logical operators are AND within a group, OR between groups.
- **Engagement** covers calls, emails, meetings, notes, tasks in HubSpot v1 API — the `type` field is required.
- **Form→Submit Data** posts to a HubSpot form; the form must have the fields you're submitting or they'll be silently dropped.
- HubSpot v3 API is used for most resources; the Engagement resource still uses v1.

**Source:** n8n-nodes-base.hubspot.md  [doc-verified]
