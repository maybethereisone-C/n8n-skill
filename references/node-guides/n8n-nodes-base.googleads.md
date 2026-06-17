# Google Ads — `n8n-nodes-base.googleAds`
**Type** `n8n-nodes-base.googleAds` · **typeVersion** 1 · **action**
**What:** Read-only access to Google Ads campaigns (get one or list all).
**Credentials:** `googleAdsOAuth2Api` — requires OAuth2 with Google Ads scope and a Developer Token.

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Campaign | Get, Get All |

**Key params & gotchas:**
- Google Ads API requires a **Developer Token** in addition to OAuth2 — apply for one in the Google Ads UI under Tools > API Center; test accounts get a test-account token that only works against test accounts.
- `Customer ID` (10-digit, no dashes) is required; for MCC (manager) accounts you must specify the child customer ID, not the manager account ID.
- Only Campaign read operations are supported; this node cannot create or modify ads/campaigns.

**Source:** n8n-nodes-base.googleads.md  [doc-verified]
