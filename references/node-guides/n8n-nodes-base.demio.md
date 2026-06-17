# Demio — `n8n-nodes-base.demio`
**Type** `n8n-nodes-base.demio` · **action**
**What:** Fetch Demio webinar events and register attendees; retrieve event reports.
**Credentials:** demioApi (API key + API secret).

## Resources / Operations
| Resource | Operations |
|---|---|
| Event | Get, Get All, Register |
| Report | Get (event report) |

## Key params & gotchas
- **Register** requires the event ID and registrant email; optional fields include name and custom form answers.
- **Get event report** returns post-event attendance and registration stats — only available after the event ends.
- Event IDs are numeric; use "Get All" to discover them dynamically.

**Source:** n8n-nodes-base.demio.md  [doc-verified]
