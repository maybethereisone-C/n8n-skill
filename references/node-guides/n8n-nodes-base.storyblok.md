# Storyblok — `n8n-nodes-base.storyblok`
**Type** `n8n-nodes-base.storyblok` · **typeVersion** 1 · **action**
**What:** Manage Storyblok CMS stories via both the public Content API and the Management API.
**Credentials:** `storyblokApi`
**Resources / Operations:**
| API | Resource | Operations |
|---|---|---|
| Content API | Story | Get, Get All |
| Management API | Story | Delete, Get, Get All, Publish, Unpublish |

**Key params & gotchas:**
- Content API is read-only (public preview token); Management API requires a personal access token with write scope.
- Publish/Unpublish only available through Management API — switching credential type changes available operations.
- Content API Get All returns published stories only by default.

**Source:** n8n-nodes-base.storyblok.md  [doc-verified]
