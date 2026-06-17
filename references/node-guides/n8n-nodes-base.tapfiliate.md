# Tapfiliate — `n8n-nodes-base.tapfiliate`
**Type** `n8n-nodes-base.tapfiliate` · **typeVersion** 1 · **action**
**What:** Manage affiliates, affiliate metadata, and program-affiliate relationships in Tapfiliate affiliate marketing.
**Credentials:** `tapfiliateApi`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Affiliate | Create, Delete, Get by ID, Get All |
| Affiliate Metadata | Add, Remove, Update |
| Program Affiliate | Add to Program, Approve, Disapprove, Get, Get All |

**Key params & gotchas:**
- Affiliate Metadata keys/values are free-form strings; updates replace the specific key, not the whole metadata object.
- Program Affiliate operations require both an affiliate ID and a program ID.
- Approve/Disapprove changes the affiliate's status within a specific program, not globally.

**Source:** n8n-nodes-base.tapfiliate.md  [doc-verified]
