# Bannerbear — `n8n-nodes-base.bannerbear`
**Type** `n8n-nodes-base.bannerbear` · **action**
**What:** Generate images from Bannerbear templates and retrieve template definitions.
**Credentials:** Bannerbear API key credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Image | Create, Get |
| Template | Get, Get All |

## Key params & gotchas
- **Image/Create** is async — Bannerbear generates the image in the background. The response includes a status field; poll with Image/Get until status is `completed`.
- Template variables (modifications) are passed as an array of `{name, text}` or `{name, image_url}` objects matching the template's layer names.
- Template/Get returns layer definitions — use this to discover the exact layer names needed for modifications.
- Images are returned as URLs; use HTTP Request node to download the binary if needed.

**Source:** n8n-nodes-base.bannerbear.md  [doc-verified]
