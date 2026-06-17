# Humantic AI — `n8n-nodes-base.humanticai`
**Type** `n8n-nodes-base.humanticai` · **typeVersion** 1 · **action**
**What:** Create, retrieve, and update personality profiles using Humantic AI's buyer intelligence API.
**Credentials:** `humanticAiApi` (API key).

## Resources / Operations
| Resource | Operations |
|---|---|
| Profile | Create, Retrieve, Update |

## Key params & gotchas
- **Create** builds a profile from a LinkedIn URL or user ID — LinkedIn URL is the primary input.
- **Retrieve** returns DISC/Big Five personality scores and communication style recommendations for sales outreach.
- **Update** enriches an existing profile with additional data (e.g. email, resume text).
- Profiles are identified by a `userId` returned on Create — store it for subsequent Retrieve/Update calls.
- API rate limits apply per account tier; batch creation via n8n loops may hit limits quickly.

**Source:** n8n-nodes-base.humanticai.md  [doc-verified]
