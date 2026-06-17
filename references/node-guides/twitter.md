# X (Formerly Twitter) — `n8n-nodes-base.twitter`
**Type** `n8n-nodes-base.twitter` · **typeVersion** 2 · **action**
**What:** Create/delete/search/like/retweet tweets, send DMs, look up users, and manage list members on X (Twitter).
**Credentials:** `twitterOAuth2Api` (OAuth2 — requires X Developer App with appropriate scopes).
**Resources / Operations:**
| Resource | Operation |
|----------|-----------|
| Direct Message | Create |
| Tweet | Create or reply, Delete, Search, Like, Retweet |
| User | Get |
| List | Add member |

**Key params & gotchas:**
- Search uses X API v2 query syntax; free-tier X Developer accounts have very limited search access.
- Tweet creation supports `reply_to_tweet_id` for threading.
- Can be used as an AI tool sub-node.
- OAuth2 scopes needed differ by operation: `tweet.write` for posting, `dm.write` for DMs, `users.read` for user lookup.

**Source:** n8n-nodes-base.twitter.md  [doc-verified]
