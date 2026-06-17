# Philips Hue — `n8n-nodes-base.philipshue`
**Type** `n8n-nodes-base.philipshue` · **action**
**What:** Control Philips Hue smart lights — retrieve info, update state, or delete lights.
**Credentials:** `philipsHueOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Light | Delete |
| Light | Retrieve (single) |
| Light | Retrieve All |
| Light | Update |

## Key params & gotchas
- Uses OAuth2 via the Philips Hue Remote API — credentials must be authorized against your Hue bridge account, not a local bridge IP.
- "Delete" removes the light from the bridge; use Update (set `on: false`) to simply turn it off.
- Update accepts brightness (`bri`), hue, saturation, color temperature (`ct`), and on/off state.
- Hue bridge must be linked to a Philips Hue developer account for remote API access.

**Source:** n8n-nodes-base.philipshue.md  [doc-verified]
