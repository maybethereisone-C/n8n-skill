# SurveyMonkey Trigger — `n8n-nodes-base.surveyMonkeyTrigger`
**Type** `n8n-nodes-base.surveyMonkeyTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a SurveyMonkey survey response is submitted or a survey is updated, via webhook.
**Credentials:** `surveyMonkeyOAuth2Api`.
**Resources / Operations:**
| Object | Events |
|---|---|
| Survey | Response Completed, Response Created, Response Disqualified, Response Updated |
| Collector | Response Completed, Response Created, Response Disqualified, Response Updated |

**Key params & gotchas:**
- Trigger type: **webhook** — SurveyMonkey pushes events to n8n's webhook URL.
- Response payloads include only metadata (respondent ID, survey ID, date); a follow-up SurveyMonkey node call is needed to fetch full response answers.
- Webhook subscriptions require an app with the `responses:read` scope at minimum.

**Source:** n8n-nodes-base.surveymonkeytrigger.md  [doc-verified]
