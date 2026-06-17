# Google Cloud Natural Language — `n8n-nodes-base.googleCloudNaturalLanguage`
**Type** `n8n-nodes-base.googleCloudNaturalLanguage` · **typeVersion** 1 · **action**
**What:** Runs sentiment analysis on text using the Google Cloud Natural Language API.
**Credentials:** `googleApi` (service account) or `googleCloudNaturalLanguageOAuth2Api` (OAuth2).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Document | Analyze Sentiment |

**Key params & gotchas:**
- Only **Analyze Sentiment** is exposed; entity analysis, syntax, classification, and moderation are not available through this node — use the HTTP Request node for those endpoints.
- Returns `documentSentiment` (score -1..1, magnitude 0..∞) and per-sentence scores.
- Input can be plain text or HTML; set `type` accordingly.
- Quotas default to 800 requests/minute per project; burst above that returns 429s.
- The Cloud Natural Language API must be enabled in the GCP project.

**Source:** n8n-nodes-base.googlecloudnaturallanguage.md  [doc-verified]
