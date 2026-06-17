# Beeminder — `n8n-nodes-base.beeminder`
**Type** `n8n-nodes-base.beeminder` · **action**
**What:** Log data points to Beeminder goals for commitment-contract tracking.
**Credentials:** Beeminder API key credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Data Point | Create, Delete, Get All, Update |

## Key params & gotchas
- **Goal slug** is required — the short name in the goal URL (`https://www.beeminder.com/<user>/<slug>`).
- Data Point/Create requires a numeric `value` and optionally a `timestamp` (Unix epoch) and `comment`.
- If no timestamp is provided, Beeminder uses the current time.
- Data points are immutable in spirit — deleting/updating bypasses Beeminder's derailment detection, so use with care.
- Get All returns all data points for a goal; no server-side date filtering — filter downstream.

**Source:** n8n-nodes-base.beeminder.md  [doc-verified]
