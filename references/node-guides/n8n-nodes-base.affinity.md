# Affinity — `n8n-nodes-base.affinity`

**Type** `n8n-nodes-base.affinity` · **typeVersion** 1 · **action**

**What:** Create, read, update, and delete Lists, List Entries, Organizations, and Persons in Affinity CRM.

**Credentials:** `affinityApi` — API key obtained from Affinity Settings → API.

## Resources / Operations

| Resource | Operations |
|---|---|
| **List** | Get, Get All |
| **List Entry** | Create, Delete, Get, Get All |
| **Organization** | Create, Delete, Get, Get All, Update |
| **Person** | Create, Delete, Get, Get All, Update |

Notes:
- **List** is read-only from n8n's perspective (no create/delete/update of lists themselves).
- **List Entry** links an existing Organization or Person to a List — it is not a standalone record.

## Key params & gotchas

- **`resource`** defaults to `organization`; remember to switch it when targeting lists or persons — wrong resource with a valid ID silently returns the wrong entity type.
- **List Entry → Create** requires both a `listId` and the ID of the entity (organization or person) being added — omitting either causes a 400 from the Affinity API.
- **Get All** operations support a **Return All** toggle; leave it off and set a **Limit** for large workspaces to avoid rate-limit errors (Affinity enforces per-minute quotas on list endpoints).
- **Organization / Person → Update** only patches supplied fields; absent optional fields are left unchanged. Do not send `null` for fields you want to preserve.
- The `events` parameter shown in the schema (`multiOptions`, default `[]`) applies to webhook/trigger variants — it is irrelevant for this action node.
- Affinity field IDs (for custom fields) are numeric strings, not names. Retrieve them via **List → Get All** or the Affinity API reference before building Update payloads.

## Minimal example

```json
{
  "nodes": [
    {
      "name": "Add org to list",
      "type": "n8n-nodes-base.affinity",
      "typeVersion": 1,
      "parameters": {
        "resource": "listEntry",
        "operation": "create",
        "listId": "12345",
        "entityId": "67890"
      },
      "credentials": {
        "affinityApi": { "id": "1", "name": "Affinity account" }
      }
    }
  ]
}
```

**Source:** `n8n-nodes-base.affinity.md`  [doc-verified + schema]
