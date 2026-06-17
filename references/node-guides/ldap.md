# LDAP — `n8n-nodes-base.ldap`
**Type** `n8n-nodes-base.ldap` · **core**

**What:** Interacts with LDAP/Active Directory servers to compare, create, delete, rename, search, and update directory entries.

**Credentials:** LDAP credential.

**Resources / Operations:**
| Operation | Key params |
|-----------|-----------|
| Compare | DN, Attribute ID, Value |
| Create | DN, Attribute ID/Value pairs |
| Delete | DN |
| Rename | DN, New DN |
| Search | Base DN, Search For, Attribute, Search Text (`*` wildcard); Return All / Limit |
| Update | DN, update mode (Add/Remove/Replace), Attribute ID/Value |

**Key params & gotchas:**
- **Search → Scopes**: Base Tree (subordinates only), Single Level (immediate children), Whole Subtree (full depth).
- **Search → Page Size** controls LDAP paging; set to 0 to disable.
- **Search → Attribute Names or IDs** limits returned attributes — useful to reduce payload size.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.ldap.md  [doc-verified]
