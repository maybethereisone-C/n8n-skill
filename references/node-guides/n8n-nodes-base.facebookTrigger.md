# Facebook Trigger — `n8n-nodes-base.facebookTrigger`
**Type** `n8n-nodes-base.facebookTrigger` · **typeVersion** 1 · **trigger**

**What:** Fires on Facebook Graph API webhook events for various objects (Pages, Ad Accounts, Instagram accounts, etc.).

**Credentials:** `facebookAppApi` (App ID + App Secret).

**Resources / Operations:**
| Object | Field/event options |
|---|---|
| Ad Account | In Process Ad Objects · With Issues Ad Objects (wildcard `*` selects all) |
| (Other objects) | Configured per Facebook's Graph API Webhooks reference — Pages, User, Instagram Business, WhatsApp Business, etc. |

**Key params & gotchas:**
- Webhook-based using Facebook's Graph API Webhooks.
- Requires the **APP ID** in the node config (in addition to credential).
- **Ad Account object**: must enable **Include Values** in Options or the webhook subscription fails.
- **Ad Account wildcard `*`**: default selects all field updates; remove `*` to pick specific field names.
- Facebook verifies the webhook endpoint with a challenge request — n8n handles this automatically.
- One Facebook App can register multiple subscriptions but each webhook URL must be unique per object type.

**Source:** n8n-nodes-base.facebooktrigger/ad-account.md  [doc-verified]
