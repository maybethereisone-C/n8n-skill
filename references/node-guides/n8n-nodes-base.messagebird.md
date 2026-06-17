# MessageBird — `n8n-nodes-base.messageBird`
**Type** `n8n-nodes-base.messageBird` · **typeVersion** 1 · **action**
**What:** Sends SMS text messages and retrieves the MessageBird account balance.
**Credentials:** `messageBirdApi` (API Key from MessageBird dashboard).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| SMS | Send |
| Balance | Get |

**Key params & gotchas:**
- SMS > Send requires `originator` (sender name or number, max 11 chars for alphanumeric), `recipients` (E.164 format array), and `body` (message text).
- Alphanumeric originator names are not supported in all countries (e.g. US requires a registered number); check MessageBird's country coverage docs.
- MessageBird rebranded to **Bird** in 2023; the API still works under the old domain but check credentials dashboard for any migration notices.
- Balance > Get is useful to confirm the account has credit before sending large SMS batches.
- No delivery receipt / status polling in this node — use MessageBird webhooks via the Webhook trigger node for DLR callbacks.

**Source:** n8n-nodes-base.messagebird.md  [doc-verified]
