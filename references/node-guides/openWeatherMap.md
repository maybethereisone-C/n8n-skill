# OpenWeatherMap — `n8n-nodes-base.openWeatherMap`
**Type** `n8n-nodes-base.openWeatherMap` · **typeVersion** 1 · **action**
**What:** Retrieve current weather conditions or a 5-day / 3-hour forecast for a city or coordinates.
**Credentials:** OpenWeatherMap API key (`openWeatherMapApi`).
**Resources / Operations:**
| Operation |
|---|
| Get current weather data |
| Get weather data for next 5 days (3-hour intervals) |

**Key params & gotchas:**
- Location can be specified by city name, city ID, lat/lon, or ZIP code — check which format the API accepts per endpoint.
- Free tier is limited to current weather and 5-day forecast; One Call API (hourly/historical) requires a paid plan.
- Units can be set to `metric`, `imperial`, or `standard` (Kelvin).
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.openweathermap.md  [doc-verified]
