# NASA  (`n8n-nodes-base.nasa`)

- typeVersion (max): **1**  | group: transform  | trigger: no
- credentials: nasaApi
- resources: asteroidNeoBrowse, asteroidNeoFeed, asteroidNeoLookup, astronomyPictureOfTheDay, donkiCoronalMassEjection, donkiGeomagneticStorm, donkiHighSpeedStream, donkiInterplanetaryShock, donkiMagnetopauseCrossing, donkiNotifications, donkiRadiationBeltEnhancement, donkiSolarEnergeticParticle, donkiSolarFlare, donkiWsaEnlilSimulation, earthAssets, earthImagery
- operations: get, getAll

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | astronomyPictureOfTheDay |  |  |
| `operation` | Operation | options | get |  | res=astronomyPictureOfTheDay |
| `operation` | Operation | options | get |  | res=asteroidNeoFeed |
| `operation` | Operation | options | get |  | res=asteroidNeoLookup |
| `operation` | Operation | options | getAll |  | res=asteroidNeoBrowse |
| `operation` | Operation | options | get |  | res=donkiCoronalMassEjection |
| `operation` | Operation | options | get |  | res=donkiGeomagneticStorm |
| `operation` | Operation | options | get |  | res=donkiInterplanetaryShock |
| `operation` | Operation | options | get |  | res=donkiSolarFlare |
| `operation` | Operation | options | get |  | res=donkiSolarEnergeticParticle |
| `operation` | Operation | options | get |  | res=donkiMagnetopauseCrossing |
| `operation` | Operation | options | get |  | res=donkiRadiationBeltEnhancement |
| `operation` | Operation | options | get |  | res=donkiHighSpeedStream |
| `operation` | Operation | options | get |  | res=donkiWsaEnlilSimulation |
| `operation` | Operation | options | get |  | res=donkiNotifications |
| `operation` | Operation | options | get |  | res=earthImagery |
| `operation` | Operation | options | get |  | res=earthAssets |
| `operation` | Operation | options | get |  | res=inSightMarsWeatherService |
| `operation` | Operation | options | get |  | res=imageAndVideoLibrary |
| `operation` | Operation | options | get |  | res=techTransfer |
| `operation` | Operation | options | get |  | res=twoLineElementSet |
| `asteroidId` | Asteroid ID | string |  | true | res=asteroidNeoLookup,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=asteroidNeoLookup,op=get |
| `download` | Download Image | boolean | true |  | res=astronomyPictureOfTheDay |
| `binaryPropertyName` | Put Output File in Field | string | data | true | res=astronomyPictureOfTheDay,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=astronomyPictureOfTheDay,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=asteroidNeoFeed,res=donkiCoronalMassEjection,res=donkiGeomagneticStorm,res=donkiSolarFlare,res=donkiSolarEnergeticParticle,res=donkiMagnetopauseCrossing |
| `additionalFields` | Additional Fields | collection | {} |  | res=donkiInterplanetaryShock,op=get |
| `lat` | Latitude | number |  |  | res=earthImagery,res=earthAssets,op=get |
| `lon` | Longitude | number |  |  | res=earthImagery,res=earthAssets,op=get |
| `binaryPropertyName` | Put Output File in Field | string | data | true | res=earthImagery,op=get |
| `additionalFields` | Additional Fields | collection | {} |  | res=earthImagery,res=earthAssets,op=get |
| `returnAll` | Return All | boolean | false |  | op=getAll |
| `limit` | Limit | number | 20 |  | op=getAll |
