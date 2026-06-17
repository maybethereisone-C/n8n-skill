# Segment — `n8n-nodes-base.segment`
**Type** `n8n-nodes-base.segment` · **action**
**What:** Send analytics data to Segment — group membership, user identification, and event/page tracking.
**Credentials:** `segmentApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Group | Add a user to a group |
| Identify | Create an identity (identify call) |
| Track | Track an action/event |
| Track | Track a page view |

## Key params & gotchas
- Uses the Segment **HTTP Tracking API** (write-only); does not query Segment data or profiles.
- **Identify**: sets traits on a `userId` — use before Track calls to enrich user profiles.
- **Group**: associates a `userId` with a `groupId`; call after Identify for proper linking.
- **Track**: requires `event` name and `userId` or `anonymousId`; additional properties go in the event properties object.
- Write key is the Segment Source write key (not API token) — one per Source.
- Calls are synchronous HTTP but Segment processes asynchronously; data may appear with a short delay in destinations.

**Source:** n8n-nodes-base.segment.md  [doc-verified]
