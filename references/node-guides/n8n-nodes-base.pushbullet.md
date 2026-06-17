# Pushbullet — `n8n-nodes-base.pushbullet`
**Type** `n8n-nodes-base.pushbullet` · **action**
**What:** Create, update, delete, and retrieve push notifications across Pushbullet-connected devices.
**Credentials:** `pushbulletOAuth2Api`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Push | Create |
| Push | Delete |
| Push | Get All |
| Push | Update |

## Key params & gotchas
- Push types include `note`, `link`, `file` — specify type when creating.
- Pushes can be targeted to a device, a channel, or a contact (email); omitting target sends to all devices.
- OAuth2 credentials required; the Pushbullet Access Token (non-OAuth) is not supported here.
- Deleted pushes are soft-deleted and excluded from Get All by default.

**Source:** n8n-nodes-base.pushbullet.md  [doc-verified]
