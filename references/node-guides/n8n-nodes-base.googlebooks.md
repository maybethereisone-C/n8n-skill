# Google Books — `n8n-nodes-base.googleBooks`
**Type** `n8n-nodes-base.googleBooks` · **typeVersion** 1 · **action**
**What:** Manages Google Books bookshelves and volumes for a user account.
**Credentials:** `googleBooksOAuth2Api` or `googleApi` (service account).

**Resources / Operations:**

| Resource | Operations |
|---|---|
| Bookshelf | Get (by shelf ID), Get All (public shelves for user) |
| Bookshelf Volume | Add, Clear All, Get All, Move, Remove |
| Volume | Get (by volume ID), Get All (search by query) |

**Key params & gotchas:**
- Bookshelf operations target a specific user's shelves; the authenticated user's shelves are accessible, other users' shelves are public-only.
- Volume > Get All performs a text search (same as Google Books search); pass a query string, not a category filter.
- Bookshelf Volume > Move requires a `volumePosition` (0-based index); incorrect positions are silently clamped.

**Source:** n8n-nodes-base.googlebooks.md  [doc-verified]
