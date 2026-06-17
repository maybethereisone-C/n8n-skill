# ActiveCampaign — `n8n-nodes-base.activeCampaign`

**Type** `n8n-nodes-base.activeCampaign` · **typeVersion** 1 · **action**

**What:** Create, read, update, and delete records across ActiveCampaign CRM — contacts, accounts, deals, lists, tags, connections, and e-commerce objects.

**Credentials:** `activeCampaignApi` — requires the account URL and API key from ActiveCampaign → Settings → Developer.

---

## Resources / Operations

| Resource | Operations |
|---|---|
| **Account** | Create · Delete · Get · Get All · Update |
| **Account Contact** | Create association · Delete association · Update association |
| **Contact** | Create · Delete · Get · Get All · Update |
| **Contact List** | Add to list · Remove from list |
| **Contact Tag** | Add tag · Remove tag |
| **Connection** | Create · Delete · Get · Get All · Update |
| **Deal** | Create · Delete · Get · Get All · Update · Create note · Update note |
| **E-commerce Order** | Create · Delete · Get · Get All · Update |
| **E-commerce Customer** | Create · Delete · Get · Get All · Update |
| **E-commerce Order Products** | Get All order products · Get ordered product · Get order's products |
| **List** | Get All |
| **Tag** | Create · Delete · Get · Get All · Update |

---

## Key params & gotchas

- **Contact vs Account Contact:** "Contact" manages standalone contact records; "Account Contact" manages the *association* between an existing contact and an existing account — you need both IDs. Don't confuse them.
- **Contact List operations require a list ID, not a list name.** Use List → Get All first to resolve names to IDs, or store IDs in a lookup table.
- **Contact Tag vs Tag resource:** "Contact Tag" adds/removes a tag on a specific contact. "Tag" manages the tag definition itself (create the tag before you can apply it). Tag must exist before applying.
- **Connection is required for e-commerce.** E-commerce Orders and Customers are scoped to a Connection (a store integration). Create the Connection first and store its `id`; every order/customer operation requires `connectionid`.
- **E-commerce Order Products are read-only.** There is no Create/Update/Delete for order products via this node — products are set at order-creation time through the order payload, not managed separately.
- **Deal notes are sub-operations of Deal,** not a separate resource. Set Resource → Deal, then pick "Create note" or "Update note".
- **Get All returns paginated results.** By default n8n fetches all pages automatically; if the account has thousands of records, this can be slow or hit rate limits. Use filters where available.
- **events / sources parameters** are multiOptions fields on the node (exposed in the schema) — these filter webhook-style triggers, not standard operation parameters. Leave empty unless you are filtering event streams.
- **Update operations use the record ID**, not email or name. Always fetch the record first or pass the ID explicitly from a prior step.

---

## Minimal example

Upsert-style pattern: look up a contact by email, then branch on whether it exists.

```json
[
  {
    "parameters": {
      "resource": "contact",
      "operation": "getAll",
      "filters": {
        "email": "={{ $json.email }}"
      }
    },
    "type": "n8n-nodes-base.activeCampaign",
    "typeVersion": 1,
    "credentials": {
      "activeCampaignApi": { "id": "1", "name": "AC prod" }
    }
  }
]
```

If the result is empty, route to Contact → Create; otherwise route to Contact → Update with `{{ $json[0].id }}`.

---

**Source:** `n8n-nodes-base.activecampaign.md`  [doc-verified] + schema cross-referenced
