# Email Trigger (IMAP) — `n8n-nodes-base.emailReadImap`
**Type** `n8n-nodes-base.emailReadImap` · **typeVersion** 2.1 · **trigger**
**What:** Polls an IMAP mailbox and fires when new emails arrive.
**Credentials:** IMAP (host, port, TLS, user/pass).
**Trigger-on:** New email in the configured mailbox.

**Key params & gotchas:**
- `mailbox` — default `INBOX`; change to `Sent`, `[Gmail]/All Mail`, etc. as needed.
- `postProcessAction` — `read` (mark as read) or `nothing` (leave unread). Leaving unread will re-trigger on the same email every poll cycle if the workflow re-activates.
- `downloadAttachments` — default `false`; enabling it increases processing time significantly; only set when attachments are required downstream.
- `format` — three options:
  - `simple` — parsed, human-friendly; **cannot** capture inline attachments.
  - `resolved` — full parse + attachments as binary data (preferred when attachments matter).
  - `RAW` — base64url-encoded raw MIME string in `raw` field; no `payload` field.
- `options.customEmailConfig` — accepts node-imap search criteria array (e.g., `["UNSEEN", ["SINCE", "May 1, 2024"]]`) for fine-grained filtering.
- `options.forceReconnect` — integer minutes; set to avoid stale IMAP connections on long-lived deployments.
- This node polls; it is **not** a webhook. Poll interval is controlled by n8n's trigger poll settings, not this node.
- Schema shows `typeVersion 2.1`; the node is listed as a trigger group but `trigger: no` in schema — it is nonetheless a trigger node in practice.

**Source:** `n8n-nodes-base.emailimap.md`  [doc-verified]
