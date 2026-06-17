# OpenWeatherMap  (`n8n-nodes-base.openWeatherMap`)

- typeVersion (max): **1**  | group: input  | trigger: no
- credentials: openWeatherMapApi
- operations: 5DayForecast, currentWeather

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `operation` | Operation | options | currentWeather |  |  |
| `format` | Format | options | metric |  |  |
| `locationSelection` | Location Selection | options | cityName |  |  |
| `cityName` | City | string |  | true |  |
| `cityId` | City ID | number | 160001123 | true |  |
| `latitude` | Latitude | string |  | true |  |
| `longitude` | Longitude | string |  | true |  |
| `zipCode` | Zip Code | string |  | true |  |
| `language` | Language | string |  |  |  |
