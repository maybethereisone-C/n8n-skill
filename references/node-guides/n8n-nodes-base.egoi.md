# E-goi — `n8n-nodes-base.eGoi`
**Type** `n8n-nodes-base.eGoi` · **action**
**What:** Manage E-goi email marketing contacts (members) within a list.
**Credentials:** egoiApi (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Contact | Create Member, Get Member, Get All Members, Update Member |

## Key params & gotchas
- All operations require a **List ID** — select the target E-goi list from the dropdown.
- "Member" in E-goi terminology = contact/subscriber.
- **Get All Members** supports filters but paginates; use with care on large lists.

**Source:** n8n-nodes-base.egoi.md  [doc-verified]
