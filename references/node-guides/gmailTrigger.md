# Gmail Trigger — `n8n-nodes-base.gmailTrigger`
**Type** `n8n-nodes-base.gmailTrigger` · **typeVersion** 2.2 · **trigger**
**What:** Polls Gmail for new messages matching filters and fires when new mail is detected.
**Credentials:** `googleApi` (OAuth2 recommended)

## Trigger type: polling

| Param | Notes |
|---|---|
| Event | `messageReceived` only |
| Poll Time | Mode + interval; see poll-mode-options.md |
| Max Emails per Poll | Default 10, max 50; excess queued for next poll |
| Simplify | Default true — returns IDs, labels, From/To/CC/BCC/Subject headers only |

## Filters

| Filter | Notes |
|---|---|
| Include Spam and Trash | Default off |
| Label Names or IDs | Restrict to messages with specific labels |
| Search | Gmail search syntax (e.g. `from:boss@example.com has:attachment`) |
| Read Status | Unread only (default), Read only, or both |
| Sender | Filter by sender email or partial name |

## Key params & gotchas
- This is a **poll** trigger, not a push webhook — delivery latency equals the poll interval (minimum 1 minute by default).
- `simple=false` returns the full raw Gmail API message envelope including raw headers and base64-encoded parts.
- Max 50 emails per poll; if inbox has more unprocessed mail, n8n queues and fetches on next cycle — high-volume inboxes may lag.
- OAuth2 (`googleApi`) is strongly preferred; Service Account auth may lack Gmail scope.
- `authentication` param: `oAuth2` (default) or `serviceAccount`.

**Source:** n8n-nodes-base.gmailtrigger/index.md + poll-mode-options.md + schema  [doc-verified]
