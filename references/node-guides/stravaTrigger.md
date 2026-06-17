# Strava Trigger — `n8n-nodes-base.stravaTrigger`
**Type** `n8n-nodes-base.stravaTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Strava athlete or activity events via Strava webhook subscription.
**Credentials:** `stravaOAuth2Api`.
**Resources / Operations:**
| Object | Events |
|---|---|
| [All] | [All] / Created / Deleted / Updated |
| Activity | [All] / Created / Deleted / Updated |
| Athlete | [All] / Created / Deleted / Updated |

**Key params & gotchas:**
- Trigger type: **webhook** — Strava pushes events to n8n's webhook URL.
- Strava's webhook subscription API allows only one subscription per application (client ID); registering a new webhook may overwrite an existing one.
- "Athlete" events fire when the athlete updates their profile settings, privacy settings, or deauthorizes the app.

**Source:** n8n-nodes-base.stravatrigger.md  [doc-verified]
