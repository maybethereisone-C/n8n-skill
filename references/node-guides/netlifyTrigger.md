# Netlify Trigger — `n8n-nodes-base.netlifyTrigger`
**Type** `n8n-nodes-base.netlifyTrigger` · **typeVersion** 1 · **trigger**
**What:** Fires when a Netlify site event occurs (deploy started, succeeded, failed, etc.) via webhook.
**Credentials:** `netlifyApi` (personal access token).
**Resources / Operations:**
| Event category | Examples |
|---|---|
| Deploy | Deploy started, succeeded, failed, locked, unlocked |
| Form | Form submission received |

**Key params & gotchas:**
- n8n auto-registers the Netlify webhook on activation via the Netlify API.
- Specify the **Site ID** (or site name) to scope events to a particular site; omitting may not be supported — always set a site.
- Deploy events include `deploy_url`, `branch`, `commit_ref`, and build log URL fields.
- Form submission events only fire for Netlify's built-in form handling, not third-party forms embedded on the site.

**Source:** n8n-nodes-base.netlifytrigger.md  [doc-verified]
