# Strava — `n8n-nodes-base.strava`
**Type** `n8n-nodes-base.strava` · **typeVersion** 1 · **action**
**What:** Create and manage Strava activities and retrieve activity metadata (comments, kudos, laps, zones).
**Credentials:** `stravaOAuth2Api`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Activity | Create, Get, Get All, Get All Comments, Get All Kudos, Get All Laps, Get All Zones, Update |

**Key params & gotchas:**
- Create Activity requires `name`, `type` (e.g. `Run`), `startDate` (ISO 8601), and `elapsedTime` (seconds).
- Get All uses pagination — default returns 30 activities; set `perPage` and `page` via additional fields.
- OAuth2 scopes must include `activity:read_all` for private activities; `activity:write` for create/update.
- Companion trigger node (`n8n-nodes-base.stravaTrigger`) available for webhook-based activity events.

**Source:** n8n-nodes-base.strava.md  [doc-verified]
