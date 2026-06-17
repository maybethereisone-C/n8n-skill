# Facebook Lead Ads Trigger  (`n8n-nodes-base.facebookLeadAdsTrigger`)

- typeVersion (max): **1**  | group: trigger  | trigger: yes
- credentials: facebookLeadAdsOAuth2Api

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `facebookLeadAdsNotice` | Due to Facebook API limitations, you can use just one Facebook Lead Ads trigger for each Facebook App | notice |  |  |  |
| `event` | Event | options | newLead | true |  |
| `page` | Page | resourceLocator |  | true |  |
| `form` | Form | resourceLocator |  | true |  |
| `options` | Options | collection | {} |  |  |
