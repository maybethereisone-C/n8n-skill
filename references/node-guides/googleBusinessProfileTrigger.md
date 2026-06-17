# Google Business Profile Trigger — `n8n-nodes-base.googleBusinessProfileTrigger`
**Type** `n8n-nodes-base.googleBusinessProfileTrigger` · **typeVersion** 1 · **trigger**
**What:** Polls for new reviews on a Google Business Profile location and fires when a new review is posted.
**Credentials:** `googleBusinessProfileOAuth2Api`

## Events

| Event | Notes |
|---|---|
| Review Added | Fires when a new customer review appears on the selected location |

## Key params & gotchas
- `account` — required resource locator; select the Google Business Profile account.
- `location` — required resource locator; select the specific business location within the account.
- `event` — only `reviewAdded` supported (default).
- This is a **polling** trigger — no push webhook. Response latency equals the poll interval.
- Companion app node: `n8n-nodes-base.googleBusinessProfile` for managing posts and replying to reviews.

**Source:** n8n-nodes-base.googlebusinessprofiletrigger.md + schema  [doc-verified]
