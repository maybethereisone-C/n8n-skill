# Google Slides — `n8n-nodes-base.googleSlides`
**Type** `n8n-nodes-base.googleSlides` · **typeVersion** 2 · **action**
**What:** Creates presentations, reads slides/pages, retrieves thumbnails, and does bulk text replacement.
**Credentials:** `googleSlidesOAuth2Api` (OAuth2) or `googleApi` (service account).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Page | Get, Get Thumbnail |
| Presentation | Create, Get, Get Slides (list all slides), Replace Text |

**Key params & gotchas:**
- **Replace Text** does a global find-and-replace across the presentation — useful for mail-merge-style doc generation from a template. It is case-sensitive by default.
- **Get Thumbnail** returns a URL (not binary) to a PNG image; the URL is temporary and expires — download it immediately with HTTP Request if you need to store it.
- Presentation ID is the string in the URL: `slides.google.com/presentation/d/<ID>/edit`.
- Creating from a template: use Google Drive > Copy file first, then Replace Text to swap placeholders.
- Service accounts need the presentation shared with them; they cannot access user-private files.

**Source:** n8n-nodes-base.googleslides.md  [doc-verified]
