# APITemplate.io — `n8n-nodes-base.apiTemplateIo`
**Type** `n8n-nodes-base.apiTemplateIo` · **action**
**What:** Generate images and PDFs from pre-built templates in APITemplate.io.
**Credentials:** APITemplate.io API key credential.

## Resources / Operations
| Resource | Operations |
|---|---|
| Account | Get |
| Image | Create |
| PDF | Create |

## Key params & gotchas
- **Template ID** is required for Image/Create and PDF/Create — find it in your APITemplate.io dashboard.
- Template variables are passed as key-value pairs matching the template's defined fields.
- Created images/PDFs are returned as download URLs, not binary — use an HTTP Request node to fetch the binary if needed.
- Account/Get is useful to verify API key validity and check remaining credits.

**Source:** n8n-nodes-base.apitemplateio.md  [doc-verified]
