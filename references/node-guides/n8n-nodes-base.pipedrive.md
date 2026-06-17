# Pipedrive — `n8n-nodes-base.pipedrive`
**Type** `n8n-nodes-base.pipedrive` · **action**
**What:** Full CRUD for Pipedrive CRM — activities, deals, leads, notes, organizations, persons, products, and files.
**Credentials:** `pipedriveApi` or `pipedriveOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Activity | Create, Delete, Get, Get All, Update |
| Deal | Create, Delete, Duplicate, Get, Get All, Search, Update |
| Deal Activity | Get All |
| Deal Product | Add, Get All, Remove, Update |
| File | Create, Delete, Download, Get |
| Lead | Create, Delete, Get, Get All, Update |
| Note | Create, Delete, Get, Get All, Update |
| Organization | Create, Delete, Get, Get All, Search, Update |
| Person | Create, Delete, Get, Get All, Search, Update |
| Product | Get All |

## Key params & gotchas
- Supports use as an AI tool node (tool-compatible).
- Search operations use Pipedrive's search API and may return partial matches — always check the `result_score` field.
- Deal Duplicate copies field values but not linked activities/notes.
- Deal Product requires a valid Product ID from Pipedrive catalog.
- File Create uploads a binary attachment from a previous node's binary data output.
- Custom fields are accessible via their API key (e.g., `abc123_field`) in Additional Fields.
- API key auth is simpler; OAuth2 required for user-level scoped access.

**Source:** n8n-nodes-base.pipedrive.md  [doc-verified]
