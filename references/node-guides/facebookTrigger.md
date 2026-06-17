# Facebook Trigger — `n8n-nodes-base.facebookTrigger`
**Type** `n8n-nodes-base.facebookTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires on Meta Graph API webhook events across Facebook objects (Pages, Users, Instagram, WhatsApp Business, Groups, Applications, etc.).
**Credentials:** `facebookGraphApi` / `facebookGraphApiOAuth2Api` / `facebookGraphAppApi` / `facebookGraphAppOAuth2Api`

## Objects / Events

| Object | Trigger fields (examples) |
|---|---|
| Ad Account | ad changes |
| Application | add_account, plugin_comment, ads_rules_engine, group_install |
| Certificate Transparency | new SSL certs / phishing attempts on subscribed domains |
| Group | feed activity, membership events |
| Instagram | media comments, @mentions, Story expiry |
| Link | rich-preview link updates |
| Page | feed, mention, leadgen, ratings, live_videos, videos |
| Permissions | grant / revoke |
| User | profile field updates |
| WhatsApp Business Account | message events (prefer WhatsApp Trigger node) |
| Workplace Security | security events |

## Key params & gotchas
- `object` — select the object type (required).
- `fields` — defaults to `*` (all fields). Remove `*` and pick specific fields to reduce noise.
- **Application** and **Page** objects: toggle **Include Values** in Options or the webhook payload will fail.
- **Page** object prerequisites: page admin must grant `manage_pages` to the app and have at least Moderator privileges; call `{page-id}/subscribed_apps?subscribed_fields=feed` via Graph API Explorer with an app token.
- **WhatsApp** events: n8n recommends the dedicated WhatsApp Trigger node — it exposes more events.
- `authType` — `accessToken` (default) or OAuth2; choose to match your credential type.

**Source:** n8n-nodes-base.facebooktrigger/index.md + sub-pages  [doc-verified]
