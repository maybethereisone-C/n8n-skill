# Date & Time  (`n8n-nodes-base.dateTime`)

- typeVersion (max): **2**  | group: transform  | trigger: no
- credentials: —
- operations: add, addToDate, extractDate, formatDate, getCurrentDate, getTimeBetweenDates, roundDate, subtract, subtractFromDate

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `noticeDateTime` | More powerful date functionality is available in <a href='https://docs.n8n.io/code/cookbook/luxon/' target='_blank'>expressions</a>,</br> e.g. <code>{{ $now.plus(1, 'week') }}</code> | notice |  |  |  |
| `action` | Action | options | format |  |  |
| `value` | Value | string |  | true |  |
| `dataPropertyName` | Property Name | string | data | true |  |
| `custom` | Custom Format | boolean | false |  |  |
| `toFormat` | To Format | string |  |  |  |
| `options` | Options | collection | {} |  |  |
| `operation` | Operation | options | add | true |  |
| `duration` | Duration | number | 0 | true |  |
| `timeUnit` | Time Unit | options | days | true |  |
