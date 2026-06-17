# PagerDuty — `n8n-nodes-base.pagerduty`
**Type** `n8n-nodes-base.pagerduty` · **action**
**What:** Create and manage PagerDuty incidents, notes, log entries, and users.
**Credentials:** `pagerDutyApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Incident | Create, Get, Get All, Update |
| Incident Note | Create, Get All |
| Log Entry | Get, Get All |
| User | Get |

## Key params & gotchas
- Incident **Create** requires a valid service ID and an escalation policy or assigned user — missing these causes 400 errors.
- Incident **Update** can change status (acknowledged / resolved); triggering a resolve here is the standard auto-remediation pattern.
- Log entries are immutable audit records; you can only read them.
- Uses API key auth (not OAuth); key must have write scope for incident mutations.

**Source:** n8n-nodes-base.pagerduty.md  [doc-verified]
