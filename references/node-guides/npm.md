# npm — `n8n-nodes-base.npm`
**Type** `n8n-nodes-base.npm` · **typeVersion** 1 · **action**
**What:** Query the npm registry for package metadata, version lists, search results, and distribution tags.
**Credentials:** npm API token (`npmApi`) — required only for private registry or tag updates; public registry reads may work unauthenticated.
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Package | Get Package Metadata, Get Package Versions, Search for Packages |
| Distribution Tag | Get All Tags, Update a Tag |

**Key params & gotchas:**
- **Get Package Metadata** returns the full npm registry manifest (all versions, maintainers, readme, dist-tags, etc.).
- **Search for Packages** queries the npm search index — returns name, description, score, downloads.
- **Update a Tag** (e.g., pointing `latest` to a different version) requires a token with publish permission on the package.
- Targets the public npm registry by default; configure base URL in credentials for private registries (Verdaccio, Artifactory, etc.).

**Source:** n8n-nodes-base.npm.md  [doc-verified]
