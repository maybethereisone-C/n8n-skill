# Brandfetch — `n8n-nodes-base.brandfetch`
**Type** `n8n-nodes-base.brandfetch` · **action**
**What:** Look up brand assets and metadata (colors, fonts, logos, industry) by company domain.
**Credentials:** Brandfetch API key credential.

## Resources / Operations
- Return a company's colors
- Return a company's data (full brand profile)
- Return a company's fonts
- Return a company's industry
- Return a company's logo & icon

## Key params & gotchas
- Input is a **domain name** (e.g. `apple.com`) — not a company name. Use the company domain for accurate lookups.
- "Return company's data" is the superset — returns colors, fonts, logos, and industry in one call.
- Logo/icon URLs in the response point to CDN-hosted SVG/PNG assets.
- Rate limits apply on free tier; cache results to avoid repeat lookups on the same domain.

**Source:** n8n-nodes-base.brandfetch.md  [doc-verified]
