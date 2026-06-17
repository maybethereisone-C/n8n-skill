# Cortex — `n8n-nodes-base.cortex`
**Type** `n8n-nodes-base.cortex` · **action**
**What:** Run Cortex security analyzers and responders, and retrieve job results — for SOAR/threat-intel automation.
**Credentials:** cortexApi (API key + Cortex instance URL).

## Resources / Operations
| Resource | Operations |
|---|---|
| Analyzer | Execute Analyzer |
| Job | Get Job Details, Get Job Report |
| Responder | Execute Responder |

## Key params & gotchas
- **Execute Analyzer** requires an analyzer ID (e.g., `VirusTotal_GetReport_3_0`) and the observable value + type (ip, domain, file, etc.).
- Jobs run asynchronously; use **Get Job Details** to poll status (`Waiting`, `InProgress`, `Success`, `Failure`) before fetching the report.
- **Get Job Report** returns the full analyzer output JSON — may be large for file-hash reports.
- "Operation not supported" can indicate the analyzer/responder is not installed on the target Cortex instance.

**Source:** n8n-nodes-base.cortex.md  [doc-verified]
