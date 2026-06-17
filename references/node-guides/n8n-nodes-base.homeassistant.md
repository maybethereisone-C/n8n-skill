# Home Assistant — `n8n-nodes-base.homeassistant`
**Type** `n8n-nodes-base.homeassistant` · **typeVersion** 1 · **action**
**What:** Interact with a self-hosted Home Assistant instance — control states, call services, manage events, retrieve logs, render templates, and get camera snapshots.
**Credentials:** `homeAssistantApi` (base URL + Long-Lived Access Token).

## Resources / Operations
| Resource | Operations |
|---|---|
| Camera Proxy | Get Screenshot |
| Config | Get Configuration, Check Configuration |
| Event | Create Event, Get All Events |
| Log | Get Log (entity), Get All Logs |
| Service | Call Service (domain), Get All Services |
| State | Upsert (create or update), Get (entity), Get All |
| Template | Create (render a Jinja2 template) |

## Key params & gotchas
- **Service→Call Service** requires `domain` (e.g. `light`) and `service` (e.g. `turn_on`) plus a JSON body of service data — entity IDs go inside the body, not as a separate param.
- **State→Upsert** creates a virtual state if the entity doesn't exist; real device states can't be set this way — use Service→Call Service instead.
- **Template→Create** sends a Jinja2 template string and returns the rendered output — useful for computing values inside HA's templating engine.
- The credential base URL must point to the HA instance (e.g. `http://homeassistant.local:8123`); n8n must have network access to it.
- **Camera Proxy→Get Screenshot** returns binary image data — connect to a Write Binary File or similar node downstream.

**Source:** n8n-nodes-base.homeassistant.md  [doc-verified]
