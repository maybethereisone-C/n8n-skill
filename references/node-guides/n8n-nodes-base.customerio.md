# Customer.io — `n8n-nodes-base.customerIo`
**Type** `n8n-nodes-base.customerIo` · **action**
**What:** Manage Customer.io customers, track events, get campaign data, and manage segments.
**Credentials:** customerIoApi (site ID + API key — Track API) or customerIoTestApi.

## Resources / Operations
| Resource | Operations |
|---|---|
| Customer | Create/Update, Delete |
| Event | Track (identified), Track anonymous |
| Campaign | Get, Get All, Get Metrics |
| Segment | Add Customer, Remove Customer |

## Key params & gotchas
- **Customer Create/Update** is an upsert by `id` — if the customer exists it updates, otherwise creates. Always pass a stable unique `id`.
- **Track anonymous event** does not attach to a known customer; use for pre-signup funnel events.
- Campaign **Get Metrics** returns aggregated delivery/click/conversion stats — useful for reporting workflows.
- "Operation not supported" error applies to features not available on your Customer.io plan.

**Source:** n8n-nodes-base.customerio.md  [doc-verified]
