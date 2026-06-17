# PostBin — `n8n-nodes-base.postbin`
**Type** `n8n-nodes-base.postbin` · **action**
**What:** Testing utility — create/delete webhook bins and inspect captured HTTP requests. Useful for debugging webhooks without a real endpoint.
**Credentials:** none

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Bin | Create, Get, Delete |
| Request | Get, Remove First, Send |

## Key params & gotchas
- Workflow: Create a bin → get the bin ID → use "Request → Send" to POST to it → use "Request → Get" to inspect what arrived.
- Bins are ephemeral (expire after ~20 minutes on toptal.com PostBin).
- "Remove First" pops the oldest request from the bin queue — destructive, cannot be undone.
- No credentials needed; bins are public — do not use for sensitive data testing.
- Bin ID comes from the PostBin URL: `https://www.toptal.com/developers/postbin/BINID`.

**Source:** n8n-nodes-base.postbin.md  [doc-verified]
