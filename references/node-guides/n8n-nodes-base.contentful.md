# Contentful — `n8n-nodes-base.contentful`
**Type** `n8n-nodes-base.contentful` · **action**
**What:** Read-only access to Contentful CDA/CPA — fetch assets, content types, entries, locales, and spaces.
**Credentials:** contentfulApi (Delivery API token or Preview API token + Space ID).

## Resources / Operations
| Resource | Operations |
|---|---|
| Asset | Get, Get All |
| Content Type | Get |
| Entry | Get, Get All |
| Locale | Get All |
| Space | Get |

## Key params & gotchas
- This node is **read-only** (Contentful Delivery/Preview API); use HTTP Request for CMA write operations.
- Credentials must specify whether to use the Delivery API (published content) or Preview API (draft content).
- **Entry Get All** supports filtering by content type, locale, and query params; results may be paginated.
- `include` depth parameter controls how many levels of linked entries are resolved inline.

**Source:** n8n-nodes-base.contentful.md  [doc-verified]
