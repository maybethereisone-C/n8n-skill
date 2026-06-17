# Spotify — `n8n-nodes-base.spotify`
**Type** `n8n-nodes-base.spotify` · **typeVersion** 1 · **action**
**What:** Interact with Spotify — browse albums/artists/tracks, control playback, and manage playlists.
**Credentials:** `spotifyOAuth2Api`
**Resources / Operations:**
| Resource | Operations |
|---|---|
| Album | Get, Get New Releases, Get Tracks, Search |
| Artist | Get, Get Albums, Get Related Artists, Get Top Tracks, Search |
| Library | Get Liked Tracks |
| My Data | Get Followed Artists |
| Player | Add to Queue, Get Current Track, Next, Pause, Previous, Get Recently Played, Resume, Set Volume, Start Playing |
| Playlist | Add Tracks, Create, Get, Get Tracks, Get User Playlists, Remove Tracks, Search |
| Track | Get, Get Audio Features, Search |

**Key params & gotchas:**
- Album/Artist/Track identifiers accept either Spotify URI (`spotify:track:xxx`) or bare ID.
- Player operations require an active Spotify device; calls fail if no device is playing.
- `Start Playing` can target a playlist, artist, or album — not individual tracks directly.
- OAuth2 scopes must cover the operations used (e.g. `user-modify-playback-state` for playback control).

**Source:** n8n-nodes-base.spotify.md  [doc-verified]
