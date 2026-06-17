# ConvertKit — `n8n-nodes-base.convertkit`
**Type** `n8n-nodes-base.convertkit` · **action**
**What:** Manage ConvertKit email marketing — custom fields, forms, sequences, tags, and subscriber management.
**Credentials:** convertKitApi (API key + API secret).

## Resources / Operations
| Resource | Operations |
|---|---|
| Custom Field | Create, Delete, Get All, Update |
| Form | Add Subscriber, Get All, List Subscriptions |
| Sequence | Add Subscriber, Get All, Get Subscriptions |
| Tag | Create, Get All |
| Tag Subscriber | Add Tag, List Subscriptions, Delete Tag |

## Key params & gotchas
- Subscribers are identified by email address across all resources.
- **Form / Sequence Add Subscriber** also accepts custom field values; use the `Fields` collection to pass them.
- Tag IDs are numeric; use "Get All" tags first to look up IDs by name.
- ConvertKit has no "Delete Subscriber" via this node — use the HTTP Request node + CK API directly.

**Source:** n8n-nodes-base.convertkit.md  [doc-verified]
