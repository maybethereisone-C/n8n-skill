# RSS Feed Trigger — `n8n-nodes-base.rssFeedReadTrigger`
**Type** `n8n-nodes-base.rssFeedReadTrigger` · **trigger**

**What:** Polls an RSS feed on a schedule and triggers the workflow when new items are published.

**Credentials:** none.

**Resources / Operations:** Trigger only — poll RSS feed.

**Key params & gotchas:**
- **Feed URL**: the RSS feed to poll.
- **Poll Times → Mode**: Every (interval), Custom (cron), Once (one-time). Mode selection adds/removes time fields.
- Only fires for items that are new since the last poll — deduplication is handled internally.
- Companion action node: `n8n-nodes-base.rssFeedRead` for one-shot fetches.

**Source:** n8n-nodes-base.rssfeedreadtrigger.md  [doc-verified]
