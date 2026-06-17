# UptimeRobot — `n8n-nodes-base.uptimerobot`
**Type** `n8n-nodes-base.uptimerobot` · **typeVersion** 1 · **action**
**What:** Manage UptimeRobot monitors, alert contacts, maintenance windows, and public status pages via API.
**Credentials:** `uptimeRobotApi` (API key from UptimeRobot account settings — use the main API key, not the monitor-specific key).
**Resources / Operations:**
| Resource | Operations |
|----------|-----------|
| Account | Get details |
| Alert Contact | Create, Delete, Get, Get All, Update |
| Maintenance Window | Create, Delete, Get, Get All, Update |
| Monitor | Create, Delete, Get, Get All, Reset, Update |
| Public Status Page | Create, Delete, Get, Get All |

**Key params & gotchas:**
- Monitor types on create: HTTP(S)=1, Keyword=2, Ping=3, Port=4, Heartbeat=5.
- "Reset" clears the monitor's uptime/downtime log history, not its configuration.
- Public Status Page has no Update operation — delete and recreate to change settings.
- Free UptimeRobot accounts are limited to 50 monitors and 5-minute check intervals.

**Source:** n8n-nodes-base.uptimerobot.md  [doc-verified]
