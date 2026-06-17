# YouTube — `n8n-nodes-base.youtube`
**Type** `n8n-nodes-base.youtube` · **typeVersion** 1 · **action**
**What:** Manage YouTube channels, playlists, playlist items, videos, and video categories via the YouTube Data API.
**Credentials:** `youTubeOAuth2Api` (Google OAuth2; requires YouTube Data API v3 enabled in Google Cloud Console).

## Resources / Operations
| Resource | Operations |
|---|---|
| Channel | Get, Get All, Update, Upload Banner |
| Playlist | Create, Delete, Get, Get All, Update |
| Playlist Item | Add, Delete, Get, Get All |
| Video | Delete, Get, Get All, Rate, Update, Upload |
| Video Category | Get All |

## Key params & gotchas
- **Upload Video** requires binary data in the workflow — use HTTP Request or Read Binary File to get the video file first.
- **Upload Channel Banner** similarly expects binary data; banners must meet YouTube's minimum resolution (2048×1152 px).
- `Rate` operation accepts `like`, `dislike`, or `none` — not a numeric rating.
- Get All Videos without specifying a channel ID returns the authenticated user's own videos.
- This node supports use as an **AI tool** (can be called by AI Agent nodes).
- YouTube Data API has a quota system (10,000 units/day by default); uploads cost 1,600 units each.

**Source:** n8n-nodes-base.youtube.md  [doc-verified]
