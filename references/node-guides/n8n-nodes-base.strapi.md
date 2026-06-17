# Strapi — `n8n-nodes-base.strapi`
**Type** `n8n-nodes-base.strapi` · **typeVersion** 1 · **action**
**What:** Create, read, update, and delete entries in Strapi headless CMS content types.
**Credentials:** `strapiApi`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Entry | Create, Delete, Get, Get Many, Update |

**Key params & gotchas:**
- Requires specifying the **Content Type** (plural API ID, e.g. `articles`); mismatched slug returns 404.
- Supports Strapi v3 and v4 — credential setup selects the API version; URL structure differs between versions.
- Pagination for Get Many uses `limit`/`start` (v3) or `pagination[page]`/`pagination[pageSize]` (v4) via additional fields.

**Source:** n8n-nodes-base.strapi.md  [doc-verified]
