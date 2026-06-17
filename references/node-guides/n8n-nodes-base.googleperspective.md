# Google Perspective — `n8n-nodes-base.googlePerspective`
**Type** `n8n-nodes-base.googlePerspective` · **typeVersion** 1 · **action**
**What:** Scores text for toxicity and related attributes using the Perspective API.
**Credentials:** `googlePerspectiveApi` (API Key — requires Perspective API enabled and approved in GCP).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| (top-level) | Analyze Comment |

**Key params & gotchas:**
- Analyze Comment returns probability scores (0–1) for attributes like TOXICITY, SEVERE_TOXICITY, IDENTITY_ATTACK, INSULT, PROFANITY, THREAT — select which attributes to request.
- The Perspective API access must be **requested and approved** by Google; it is not auto-enabled even with the API key.
- Rate limit is 1 QPS by default for new accounts; request quota increase in GCP Console.
- Language support varies by attribute; TOXICITY supports the most languages. Submitting unsupported languages returns an error.
- Do not send PII in the comment text — the Perspective API sends data to Google servers.

**Source:** n8n-nodes-base.googleperspective.md  [doc-verified]
