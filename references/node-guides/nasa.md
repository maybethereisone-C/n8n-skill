# NASA — `n8n-nodes-base.nasa`
**Type** `n8n-nodes-base.nasa` · **typeVersion** 1 · **action**
**What:** Retrieve NASA open data: astronomy pictures, asteroid tracking (NeoWs), DONKI space weather events, and Earth imagery.
**Credentials:** NASA API key (`nasaApi`) — free key from api.nasa.gov; anonymous requests are heavily rate-limited.
**Resources / Operations:**
| Resource / Operation |
|---|
| Astronomy Picture of the Day — Get |
| Asteroid Neo-Feed — Get list by close-approach date range |
| Asteroid Neo-Lookup — Get by SPK-ID |
| Asteroid Neo-Browse — Browse full dataset |
| DONKI Coronal Mass Ejection — Get |
| DONKI Interplanetary Shock — Get |
| DONKI Solar Flare — Get |
| DONKI Solar Energetic Particle — Get |
| DONKI Magnetopause Crossing — Get |
| DONKI Radiation Belt Enhancement — Get |
| DONKI High Speed Stream — Get |
| DONKI WSA+EnlilSimulation — Get |
| DONKI Notifications — Get |
| Earth Imagery — Retrieve |
| Earth Assets — Retrieve |

**Key params & gotchas:**
- DONKI operations accept a date range (`startDate` / `endDate`); omitting dates returns recent data.
- Earth Imagery returns a satellite image (binary) for given lat/lon coordinates and date.
- Asteroid Neo-Feed requires `startDate` and `endDate` (max 7-day range per request).
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.nasa.md  [doc-verified]
