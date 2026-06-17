# seven — `n8n-nodes-base.sms77`
**Type** `n8n-nodes-base.sms77` · **typeVersion** 1 · **action**
**What:** Send SMS messages and convert text to voice calls via the seven (sms77) platform.
**Credentials:** `sms77Api`
**Resources / Operations:**
| Resource | Operation |
|---|---|
| SMS | Send SMS |
| Voice Call | Convert text to voice and call a number |

**Key params & gotchas:**
- Voice Call converts TTS to a phone call — requires a valid E.164 phone number as destination.
- Node was formerly branded "sms77"; the display name changed to "seven" but the type ID remains `sms77`.

**Source:** n8n-nodes-base.sms77.md  [doc-verified]
