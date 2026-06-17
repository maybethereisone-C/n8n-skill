# AWS Comprehend — `n8n-nodes-base.awsComprehend`
**Type** `n8n-nodes-base.awsComprehend` · **action**
**What:** Run NLP analysis on text using AWS Comprehend — language detection and sentiment analysis.
**Credentials:** AWS credential (access key + secret, with Comprehend permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Text | Identify dominant language |
| Text | Analyse sentiment |

## Key params & gotchas
- Only two operations: language detection and sentiment. More advanced Comprehend features (entity recognition, key phrases, PII detection) are not exposed — use HTTP Request node for those.
- Sentiment returns `POSITIVE`, `NEGATIVE`, `NEUTRAL`, or `MIXED` plus confidence scores.
- Language detection returns an ISO 639-1 code (e.g. `en`, `fr`).
- Input text must be UTF-8; max 5,000 bytes per request for real-time analysis.
- IAM permissions: `comprehend:DetectDominantLanguage`, `comprehend:DetectSentiment`.

**Source:** n8n-nodes-base.awscomprehend.md  [doc-verified]
