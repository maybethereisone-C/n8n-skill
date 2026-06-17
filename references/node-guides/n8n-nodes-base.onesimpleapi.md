# One Simple API — `n8n-nodes-base.oneSimpleApi`
**Type** `n8n-nodes-base.oneSimpleApi` · **action**
**What:** Utility API providing currency conversion, image metadata, social profile lookups, URL expansion, QR code generation, email validation, webpage PDF/screenshot, and SEO info.
**Credentials:** `oneSimpleApi` (API key).

## Resources / Operations

| Resource | Operation |
|---|---|
| Information | Convert a value between currencies |
| Information | Retrieve image metadata from a URL |
| Social Profile | Get details about an Instagram profile |
| Social Profile | Get details about a Spotify Artist |
| Utility | Expand a shortened URL |
| Utility | Generate a QR Code |
| Utility | Validate an email address |
| Website | Generate a PDF from a webpage |
| Website | Get SEO information from website |
| Website | Create a screenshot from a webpage |

## Key params & gotchas

- Social Profile lookups depend on One Simple API's own upstream access to Instagram/Spotify — rate limits and access restrictions are imposed by the upstream service, not n8n.
- Website operations (PDF, screenshot, SEO) require a publicly reachable URL; localhost or intranet URLs will fail.
- QR Code generation returns binary/image data; pipe output to a Write Binary File node or similar to persist it.

**Source:** n8n-nodes-base.onesimpleapi.md  [doc-verified]
