# Netlify — `n8n-nodes-base.netlify`
**Type** `n8n-nodes-base.netlify` · **typeVersion** 1 · **action**
**What:** Manage Netlify deployments and sites — cancel, create, or retrieve deploys and delete or list sites.
**Credentials:** `netlifyApi`

## Resources / Operations

| Resource | Operation |
|---|---|
| Deploy | Cancel a deployment |
| Deploy | Create a new deployment |
| Deploy | Get a deployment |
| Deploy | Get all deployments |
| Site | Delete a site |
| Site | Get a site |
| Site | Returns all sites |

## Key params & gotchas

- `siteId` is required for all Deploy operations; loaded as a dynamic options list from your Netlify account — the field label shows "Site Name or ID".
- `simple` (Simplify) is `true` by default; disabling it returns the raw Netlify API response with the full deployment object including all build metadata.
- **Cancel** is irreversible for in-progress deploys — no confirmation step exists in the node.
- There is no "Update site" operation; site configuration changes must go through the Netlify API directly or a separate HTTP Request node.

**Source:** n8n-nodes-base.netlify.md  [doc-verified]
