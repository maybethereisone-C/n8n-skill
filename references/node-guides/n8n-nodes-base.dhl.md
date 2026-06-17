# DHL — `n8n-nodes-base.dhl`
**Type** `n8n-nodes-base.dhl` · **action**
**What:** Track DHL shipments by tracking number.
**Credentials:** dhlApi (API key from DHL Developer Portal).

## Resources / Operations
| Resource | Operations |
|---|---|
| Shipment | Get Tracking Details |

## Key params & gotchas
- Single operation node — pass the tracking number and optionally the service type (Express, Parcel, etc.).
- DHL tracking API may return multiple events per shipment; the response is an array of tracking events ordered newest-first.
- API key is obtained from developer.dhl.com; sandbox and production use different keys.
- Can be used as an AI tool node (useful for order-status chatbot workflows).

**Source:** n8n-nodes-base.dhl.md  [doc-verified]
