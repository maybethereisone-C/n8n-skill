# Google Calendar Trigger — `n8n-nodes-base.googleCalendarTrigger`
**Type** `n8n-nodes-base.googleCalendarTrigger` · **typeVersion** 1.3 · **trigger**
**What:** Polls a Google Calendar and fires when calendar events are created, updated, started, ended, or cancelled.
**Credentials:** `googleCalendarOAuth2Api`

## Events

| Event | Notes |
|---|---|
| Event Cancelled | An event is cancelled/deleted |
| Event Created | A new event is added to the calendar |
| Event Ended | An event's end time passes |
| Event Started | An event's start time arrives |
| Event Updated | An existing event is modified |

## Key params & gotchas
- `calendarId` — required resource locator; select the calendar to watch.
- `triggerOn` — required options field; choose one of the five events above.
- `options` — additional collection (e.g., time zone override, how far ahead to look for started/ended events).
- This is a **polling** trigger — n8n polls the Calendar API on a schedule, not a push webhook. For Event Started/Ended, the node detects when an event's time window crosses the poll boundary.
- **Timezone note:** node uses n8n's global timezone by default; override in workflow settings if calendar is in a different zone.
- Companion app node: `n8n-nodes-base.googleCalendar`.

**Source:** n8n-nodes-base.googlecalendartrigger.md + schema  [doc-verified]
