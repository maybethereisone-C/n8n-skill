# Google Calendar  (`n8n-nodes-base.googleCalendar`)

- typeVersion (max): **1.3**  | group: input  | trigger: no
- credentials: googleCalendarOAuth2Api
- resources: calendar, event
- operations: availability, create, delete, get, getAll, update

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | event |  |  |
| `useN8nTimeZone` | This node will use the time zone set in n8n’s settings, but you can override this in the workflow settings | notice |  |  |  |
| `calendarId` | Calendar | resourceLocator |  | true |  |
| `triggerOn` | Trigger On | options |  | true |  |
| `options` | Options | collection | {} |  |  |
