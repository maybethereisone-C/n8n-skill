# RSS Read — `n8n-nodes-base.rssFeedRead`
**Type** `n8n-nodes-base.rssFeedRead` · **core**

**What:** Fetches and parses an RSS feed URL, returning all items as JSON.

**Credentials:** none.

**Resources / Operations:** Single operation — read RSS feed.

**Key params & gotchas:**
- **URL**: the RSS feed URL.
- **Ignore SSL Issues** option bypasses TLS certificate validation.
- Processes only the **first input item** — when feeding multiple URLs, use the Loop Over Items node (batch size 1) to iterate.
- Companion trigger: `n8n-nodes-base.rssFeedReadTrigger` for polling new items.

**Source:** n8n-nodes-base.rssfeedread.md  [doc-verified]
