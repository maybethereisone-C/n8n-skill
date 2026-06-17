# Salesforce — `n8n-nodes-base.salesforce`
**Type** `n8n-nodes-base.salesforce` · **action**
**What:** Full CRUD on Salesforce CRM objects — accounts, attachments, cases, contacts, custom objects, documents, flows, leads, opportunities, tasks, and users. Includes SOQL search.
**Credentials:** `salesforceOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Account | Add Note, Create, Upsert, Get, Get All, Get Metadata, Delete, Update |
| Attachment | Create, Delete, Get, Get All, Get Metadata, Update |
| Case | Add Comment, Create, Get, Get All, Get Metadata, Delete, Update |
| Contact | Add to Campaign, Add Note, Create, Upsert, Delete, Get, Get Metadata, Get All, Update |
| Custom Object | Create, Upsert, Get, Get All, Delete, Update |
| Document | Upload |
| Flow | Get All, Invoke |
| Lead | Add to Campaign, Add Note, Create, Upsert, Delete, Get, Get All, Get Metadata, Update |
| Opportunity | Add Note, Create, Upsert, Delete, Get, Get All, Get Metadata, Update |
| Search | Execute SOQL query |
| Task | Create, Delete, Get, Get All, Get Metadata, Update |
| User | Get, Get All |

## Key params & gotchas
- Supports use as an AI tool node.
- **Upsert** (Create or Update) merges on an External ID field — that field must exist on the Salesforce object and be marked as External ID.
- **Custom Fields**: use Additional Fields → Custom Fields to set/read non-standard fields; field API names (e.g., `My_Field__c`) are required.
- **SOQL Search** returns all results in a single response — no automatic pagination; large result sets may hit governor limits.
- **Document Upload** stores as a Salesforce File (ContentVersion) — not a classic Attachment.
- **Flow → Invoke** triggers an active Salesforce Flow by its API name; useful for complex business logic delegation.
- OAuth2 credentials require a Connected App in Salesforce with appropriate scopes (`api`, `refresh_token`).
- Sandbox vs Production: use different OAuth2 endpoints (`test.salesforce.com` vs `login.salesforce.com`).

**Source:** n8n-nodes-base.salesforce.md  [doc-verified]
