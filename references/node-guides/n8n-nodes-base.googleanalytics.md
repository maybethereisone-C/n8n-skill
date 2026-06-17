# Google Analytics — `n8n-nodes-base.googleAnalytics`
**Type** `n8n-nodes-base.googleAnalytics` · **typeVersion** 2 · **action**
**What:** Pulls GA4 reports and searches user activity data from Google Analytics.
**Credentials:** `googleAnalyticsOAuth2Api` (OAuth2) or service account via `googleApi`.

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Report | Get |
| User Activity | Search |

**Key params & gotchas:**
- This node targets **GA4** (Google Analytics 4) properties. For Universal Analytics (UA) properties use the older v1 node or migrate to GA4 — UA was sunset July 2024.
- Report > Get requires a Property ID (format: `properties/XXXXXXXXX`), date ranges, and at least one dimension or metric.
- User Activity > Search requires a `clientId` or `userId` and only returns data from the last 90 days.
- Sampling can occur on large queries; use shorter date ranges or filter down to reduce sampling.

**Source:** n8n-nodes-base.googleanalytics.md  [doc-verified]
