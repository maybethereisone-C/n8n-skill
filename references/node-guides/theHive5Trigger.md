# TheHive 5 Trigger — `n8n-nodes-base.theHive5Trigger`
**Type** `n8n-nodes-base.theHive5Trigger` · **typeVersion** 1 · **trigger**
**What:** Fires on TheHive v5 security incident management events (alerts, cases, tasks, observables, etc.) via webhook.
**Credentials:** `theHive5Api` (API key + server URL).
**Resources / Operations:**
| Object | Events |
|---|---|
| Alert | Created / Deleted / Updated |
| Case | Created / Deleted / Updated |
| Comment | Created / Deleted / Updated |
| Observable | Created / Deleted / Updated |
| Page | Created / Deleted / Updated |
| Task | Created / Deleted / Updated |
| Task Log | Created / Deleted / Updated |

**Key params & gotchas:**
- Trigger type: **webhook** — TheHive v5 pushes events to n8n; requires manual webhook config in TheHive's `application.conf`.
- Use **TheHive 5 Trigger** for API v5 only; use **TheHive Trigger** for v3/v4.
- Webhook setup requires editing `application.conf` to add endpoint entries and then running a cURL command to enable notifications via the org API.
- Config uses `version: 1` (vs `version: 0` for TheHive v3/v4).
- The cURL activation command uses `AnyEvent` trigger — all registered events route through all configured webhook endpoints.

**Minimal example — application.conf entry:**
```
notification.webhook.endpoints = [
  {
    name: n8n-prod
    url: https://your-n8n.com/webhook/UUID
    version: 1
    wsConfig: {}
    includedTheHiveOrganisations: ["MyOrg"]
    excludedTheHiveOrganisations: []
  }
]
```

**Source:** n8n-nodes-base.thehive5trigger.md  [doc-verified]
