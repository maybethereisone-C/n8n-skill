# Google Business Profile — `n8n-nodes-base.googleBusinessProfile`
**Type** `n8n-nodes-base.googleBusinessProfile` · **typeVersion** 1 · **action**
**What:** Creates, reads, updates, deletes Google Business Profile posts and reviews/replies.
**Credentials:** `googleBusinessProfileOAuth2Api` (OAuth2 — requires Business Profile API enabled in GCP).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Post | Create, Delete, Get, Get Many, Update |
| Review | Delete Reply, Get, Get Many, Reply |

**Key params & gotchas:**
- Requires the **Google My Business API** (now "Business Profile API") to be enabled; it must be requested from Google — not auto-enabled.
- Posts require a `locationName` (format: `accounts/{accountId}/locations/{locationId}`); use the API or GBP dashboard to find location IDs.
- Review > Reply replaces an existing reply; calling Reply on a review that already has a reply overwrites it silently.
- Post types (STANDARD, EVENT, OFFER) have different required fields; EVENT needs start/end time, OFFER needs coupon code or terms.
- A companion trigger exists: `n8n-nodes-base.googleBusinessProfileTrigger`.

**Source:** n8n-nodes-base.googlebusinessprofile.md  [doc-verified]
