# TheHive Trigger — `n8n-nodes-base.theHiveTrigger`
**Type** `n8n-nodes-base.theHiveTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on TheHive v3/v4 security incident management events (alerts, cases, tasks, observables, logs) via webhook.
**Credentials:** `theHiveApi` (API key + server URL).
**Resources / Operations:**
| Object | Events |
|---|---|
| Alert | Created / Deleted / Updated |
| Case | Created / Deleted / Updated |
| Log | Created / Deleted / Updated |
| Observable | Created / Deleted / Updated |
| Task | Created / Deleted / Updated |

**Key params & gotchas:**
- Trigger type: **webhook** — TheHive v3/v4 pushes events; requires manual `application.conf` edit + cURL activation.
- Use this node for TheHive **v3 or v4** only; for v5 use `n8n-nodes-base.theHive5Trigger`.
- Config uses `version: 0` in `application.conf` (vs `version: 1` for v5).
- The cURL activation command routes `AnyEvent` to all configured endpoints — there is no per-event filtering at the webhook level; filter in n8n using an IF/Switch node.

**Minimal example — application.conf entry:**
```
notification.webhook.endpoints = [
  {
    name: n8n-prod
    url: https://your-n8n.com/webhook/UUID
    version: 0
    wsConfig: {}
    includedTheHiveOrganisations: ["MyOrg"]
    excludedTheHiveOrganisations: []
  }
]
```

**Source:** n8n-nodes-base.thehivetrigger.md  [doc-verified]
