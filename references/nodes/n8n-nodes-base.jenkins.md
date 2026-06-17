# Jenkins  (`n8n-nodes-base.jenkins`)

- typeVersion (max): **1**  | group: output  | trigger: no
- credentials: jenkinsApi
- resources: build, instance, job
- operations: cancelQuietDown, copy, create, exit, getAll, quietDown, restart, safeExit, safeRestart, trigger, triggerParams

## Parameters

| name | displayName | type | default | req | gated by |
|---|---|---|---|---|---|
| `resource` | Resource | options | job |  |  |
| `operation` | Operation | options | trigger |  | res=job |
| `triggerParamsNotice` | Make sure the job is setup to support triggering with parameters. <a href="https://wiki.jenkins.io/display/JENKINS/Parameterized+Build" target="_blank">More info</a> | notice |  |  | res=job,op=triggerParams |
| `job` | Job Name or ID | options |  | true | res=job,op=trigger,op=triggerParams,op=copy |
| `param` | Parameters | fixedCollection | {} | true | res=job,op=triggerParams |
| `newJob` | New Job Name | string |  | true | res=job,op=copy,op=create |
| `xml` | XML | string |  | true | res=job,op=create |
| `createNotice` | To get the XML of an existing job, add ‘config.xml’ to the end of the job URL | notice |  |  | res=job,op=create |
| `operation` | Operation | options | safeRestart |  | res=instance |
| `reason` | Reason | string |  |  | res=instance,op=quietDown |
| `instanceNotice` | Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation. | notice |  |  | res=instance |
| `operation` | Operation | options | getAll |  | res=build |
| `job` | Job Name or ID | options |  | true | res=build,op=getAll |
| `returnAll` | Return All | boolean | false |  | res=build,op=getAll |
| `limit` | Limit | number | 50 |  | res=build,op=getAll |
