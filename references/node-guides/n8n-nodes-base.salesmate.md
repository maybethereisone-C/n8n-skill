# Salesmate — `n8n-nodes-base.salesmate`
**Type** `n8n-nodes-base.salesmate` · **action**
**What:** Manage Salesmate CRM activities, companies, and deals.
**Credentials:** `salesmateApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Activity | Create, Delete, Get, Get All (listed as "Get all companies" in doc — likely a doc typo), Update |
| Company | Create, Delete, Get, Get All, Update |
| Deal | Create, Delete, Get, Get All, Update |

## Key params & gotchas
- The doc lists "Get all companies" under Activity resource — this appears to be a documentation error; Activity Get All retrieves activities.
- Salesmate API key is found in the account settings; credentials also require the Salesmate subdomain.
- No upsert or search operations — use Get All with filters to find existing records before update.

**Source:** n8n-nodes-base.salesmate.md  [doc-verified]
