# KoboToolbox Trigger — `n8n-nodes-base.kobotoolboxTrigger`
**Type** `n8n-nodes-base.kobotoolboxTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a new form submission arrives in a specified KoboToolbox form; handles webhook lifecycle automatically.
**Credentials:** `kobotoolboxApi` (API token + server URL — use kf.kobotoolbox.org for cloud or your self-hosted URL).
**Resources / Operations:**
| Trigger | Notes |
|---|---|
| New submission | Webhook; n8n creates/deletes the hook on activate/deactivate |

**Key params & gotchas:**
- The node mirrors the **Get Submission** operation of the KoboToolbox action node, including the same **Reformat** options (flatten group names, format dates, etc.) — apply them here so downstream nodes get clean data.
- Self-hosted instances: set the correct base URL in the credential; the default points to the public cloud.
- Only **new** submissions fire the trigger; editing existing submissions does not re-fire.
- Large media attachments are not inlined — use the KoboToolbox node to fetch attachments separately if needed.

**Source:** n8n-nodes-base.kobotoolboxtrigger.md  [doc-verified]
