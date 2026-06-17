# Twilio — `n8n-nodes-base.twilio`
**Type** `n8n-nodes-base.twilio` · **typeVersion** 1 · **action**
**What:** Send SMS/MMS/WhatsApp messages and make TTS phone calls via Twilio.
**Credentials:** `twilioApi` (Account SID + Auth Token).
**Resources / Operations:**
| Resource | Operation |
|----------|-----------|
| SMS | Send SMS/MMS/WhatsApp message |
| Call | Make a phone call (text-to-speech) |

**Key params & gotchas:**
- WhatsApp messages require the `To` number prefixed with `whatsapp:` (e.g., `whatsapp:+1234567890`) and the `From` must be a WhatsApp-enabled Twilio number.
- MMS requires a `mediaUrl` parameter pointing to the media file.
- TTS calls use Twilio's TwiML under the hood; only plain text is supported (no SSML via this node).
- Can be used as an AI tool sub-node (supports `ai-tools` snippet).

**Minimal example:**
```json
{
  "resource": "sms",
  "operation": "send",
  "from": "+15551234567",
  "to": "+15559876543",
  "message": "Hello from n8n!"
}
```
**Source:** n8n-nodes-base.twilio.md  [doc-verified]
