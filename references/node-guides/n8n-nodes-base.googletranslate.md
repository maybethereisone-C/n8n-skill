# Google Translate — `n8n-nodes-base.googleTranslate`
**Type** `n8n-nodes-base.googleTranslate` · **typeVersion** 2 · **action**
**What:** Translates text between languages using the Google Cloud Translation API.
**Credentials:** `googleTranslateOAuth2Api` (OAuth2) or `googleApi` (service account + API key).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Language | Translate |

**Key params & gotchas:**
- Target language is required (BCP-47 code, e.g. `th`, `en`, `fr`); source language is optional — omit to auto-detect.
- Uses Cloud Translation Basic (v2) by default; Advanced (v3) with glossaries/batch is not exposed.
- Input text length limit is 30,000 characters per request; split longer texts before translating.
- HTML is supported; pass `format: html` to preserve tags. Plain text mode strips tags.
- API must be enabled in the GCP project and billing must be active.

**Source:** n8n-nodes-base.googletranslate.md  [doc-verified]
