# Peekalink — `n8n-nodes-base.peekalink`
**Type** `n8n-nodes-base.peekalink` · **action**
**What:** Check link preview availability and fetch Open Graph / metadata previews for URLs.
**Credentials:** `peekalinkApi`

## Resources / Operations
| Operation |
|-----------|
| Check whether preview for a given link is available |
| Return the preview for a link |

## Key params & gotchas
- Check availability first before fetching preview to avoid wasted API calls on unsupported URLs.
- Preview data includes title, description, images, and domain info; structure varies by target site.
- Rate limits apply based on Peekalink plan tier.

**Source:** n8n-nodes-base.peekalink.md  [doc-verified]
