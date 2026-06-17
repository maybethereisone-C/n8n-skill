# Agile CRM — `n8n-nodes-base.agileCrm`

**Type** `n8n-nodes-base.agileCrm` · **typeVersion** 1 · **action**

**What:** Create, read, update, and delete contacts, companies, and deals in Agile CRM.

**Credentials:** `agileCrmApi` — requires your Agile CRM subdomain, email, and REST API key.

## Resources / Operations

| Resource | Operations |
|----------|-----------|
| **Company** | Create · Delete · Get · Get All · Update |
| **Contact** | Create · Delete · Get · Get All · Update |
| **Deal** | Create · Delete · Get · Get All · Update |

All three resources expose the same five CRUD operations. The default resource is **Contact**.

## Key Params & Gotchas

- **`resource`** (default: `contact`) — must be set first; it gates which operation fields appear downstream.
- **Update operations use property-bag patching** — you pass a list of named properties to change; fields not listed are left untouched. Don't pass the full object.
- **Get All** returns paginated results; use the **Return All** toggle or set **Limit** explicitly. Without a limit, large accounts can produce very large response arrays that blow memory on subsequent nodes.
- **Company vs Contact linkage** is not handled by this node directly — if you need to associate a contact to a company after creation you must make a separate request (e.g., via HTTP Request or a subsequent Agile CRM node operation).
- The credential subdomain must be just the prefix (e.g., `mycompany`), not the full URL — using the full URL is a common auth failure.
- Agile CRM's REST API enforces rate limits per account tier; parallel branches hitting the same resource can trip 429 errors. Add a **Wait** node between bursts if needed.

## Minimal Example

```json
{
  "type": "n8n-nodes-base.agileCrm",
  "typeVersion": 1,
  "parameters": {
    "resource": "contact",
    "operation": "create"
  },
  "credentials": {
    "agileCrmApi": {
      "id": "<credential-id>",
      "name": "Agile CRM account"
    }
  }
}
```

**Source:** `n8n-nodes-base.agilecrm.md`  [doc-verified]
