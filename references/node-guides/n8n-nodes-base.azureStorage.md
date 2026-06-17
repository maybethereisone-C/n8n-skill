# Azure Storage — `n8n-nodes-base.azureStorage`
**Type** `n8n-nodes-base.azureStorage` · **action**
**What:** Manage Azure Blob Storage containers and blobs — create, read, list, delete.
**Credentials:** Azure Storage credential (connection string or account name + key/SAS).

## Resources / Operations
| Resource | Operations |
|---|---|
| Blob | Create blob, Delete blob, Get blob, Get many blobs |
| Container | Create container, Delete container, Get container, Get many containers |

## Key params & gotchas
- **Blob/Create** creates a new blob or fully replaces an existing one — not an append operation.
- Blob binary content flows as n8n binary data; set the **Binary Property** param to the field holding the data.
- "Get many blobs" lists blobs within a specified container — requires container name.
- Container names must be lowercase, 3–63 chars, alphanumeric and hyphens only.
- No presigned URL generation — use HTTP Request node with Azure Storage REST API for that.

**Source:** n8n-nodes-base.azurestorage.md  [doc-verified]
