# Reddit — `n8n-nodes-base.reddit`
**Type** `n8n-nodes-base.reddit` · **action**
**What:** Interact with Reddit — submit, search, and manage posts and comments; browse subreddit info and user profiles.
**Credentials:** `redditOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Post | Submit, Delete, Get, Get All, Search |
| Post Comment | Create top-level comment, Get All, Remove, Reply to comment |
| Profile | Get |
| Subreddit | Get info, Search subreddits |
| User | Get |

## Key params & gotchas
- Supports use as an AI tool node.
- Post Submit requires specifying subreddit and post type (`link` or `self`/text); link posts need a URL, self posts need body text.
- Search scopes to a specific subreddit or all of Reddit — set `restrict_sr` accordingly.
- Comment Remove only works for comments on posts the authenticated account moderates.
- OAuth2 credentials require a Reddit app (script/web type) with `read` + `submit` + `edit` scopes as needed.
- Reddit API enforces rate limits and may throttle new accounts; karma/account age restrictions apply to posting in some subreddits.
- "Get All posts from subreddit" returns posts sorted by hot/new/top — sort order is configurable.

**Source:** n8n-nodes-base.reddit.md  [doc-verified]
