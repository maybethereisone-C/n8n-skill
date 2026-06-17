# Bitbucket Trigger — `n8n-nodes-base.bitbucketTrigger`
**Type** `n8n-nodes-base.bitbucketTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on Bitbucket repository or workspace events via webhook (code pushes, PRs, issues, etc.).

**Credentials:** `bitbucketOAuth2Api` or `bitbucketApi` (username + app password).

**Resources / Operations:**
| Trigger type | What fires it |
|---|---|
| Webhook | Events selected when configuring the Bitbucket webhook (push, pull request, issue, etc.) |

**Key params & gotchas:**
- Webhook-based. Configure the webhook in the Bitbucket repository under **Repository Settings > Webhooks**, pointing to n8n's webhook URL.
- Event selection happens in Bitbucket, not in n8n — choose which Bitbucket event types to subscribe to there.
- Doc has no explicit event list; event payload schema follows Bitbucket's webhook reference.

**Source:** n8n-nodes-base.bitbuckettrigger.md  [doc-verified]
