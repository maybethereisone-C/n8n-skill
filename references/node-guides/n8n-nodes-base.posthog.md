# PostHog — `n8n-nodes-base.posthog`
**Type** `n8n-nodes-base.posthog` · **action**
**What:** Send analytics events, create identities, manage aliases, and track page/screen views in PostHog.
**Credentials:** `postHogApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Alias | Create an alias |
| Event | Create an event |
| Identity | Create |
| Track | Track a page |
| Track | Track a screen |

## Key params & gotchas
- This node sends data **into** PostHog (ingestion); it does not query analytics results or feature flags.
- Alias links two distinct IDs (e.g., anonymous → identified user); call this after a user signs in.
- Identity (Identify) sets user properties on a `distinct_id`; use to set `name`, `email`, plan tier, etc.
- Event Create sends a custom event; requires `event` name and `distinct_id` at minimum.
- Track page/screen is for web/mobile instrumentation from server-side workflows.
- PostHog API key must be the **Project API Key** (public write key), not the personal API key.

**Source:** n8n-nodes-base.posthog.md  [doc-verified]
