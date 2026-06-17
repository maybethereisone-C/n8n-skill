# Spotify  (`n8n-nodes-base.spotify`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: spotifyOAuth2Api
- resources: album, artist, library, myData, player, playlist, track
- operations: add, addSongToQueue, create, currentlyPlaying, delete, get, getAlbums, getAudioFeatures, getFollowingArtists, getLikedTracks, getNewReleases, getRelatedArtists, getTopTracks, getTracks, getUserPlaylists, nextSong, pause, previousSong, recentlyPlayed, resume, search, startMusic, volume

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | player |  |  |
| `operation` | Operation | options | addSongToQueue |  | res=player |
| `id` | Resource ID | string |  | true | res=player,op=startMusic |
| `id` | Track ID | string |  | true | res=player,op=addSongToQueue |
| `operation` | Operation | options | track |  | res=track |
| `id` | Track ID | string |  | true | res=track,op=search |
| `query` | Search Keyword | string |  | true | res=track,op=search |
| `operation` | Operation | options | getLikedTracks |  | res=library |
| `operation` | Operation | options | getFollowingArtists |  | res=myData |
| `returnAll` | Return All | boolean | false | true | res=album,res=artist,res=library,res=myData,res=playlist,res=track |
| `limit` | Limit | number | 50 | true | res=album,res=artist,res=library,res=playlist,res=track,op=getTracks |
| `limit` | Limit | number | 50 | true | res=myData,res=player,op=getFollowingArtists,op=recentlyPlayed |
| `volumePercent` | Volume | number | 50 | true | res=player,op=volume |
| `filters` | Filters | collection | US |  | res=album,op=getNewReleases |
| `filters` | Filters | collection | {} |  | res=playlist,res=artist,res=track,res=album,op=search |
