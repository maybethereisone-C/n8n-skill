# MQTT Trigger — `n8n-nodes-base.mqttTrigger`
**Type** `n8n-nodes-base.mqttTrigger` · **typeVersion** 1 · **trigger**
**What:** Subscribes to an MQTT topic and fires the workflow for each message published to that topic.
**Credentials:** `mqtt` (broker host, port, protocol, optional username/password, TLS).
**Resources / Operations:**
| Trigger type | Notes |
|---|---|
| Topic subscription | Persistent MQTT subscriber; one execution per inbound message |

**Key params & gotchas:**
- **Topics** — supports MQTT wildcards: `+` (single level) and `#` (multi-level), e.g. `sensors/+/temperature` or `home/#`.
- **QoS** — set Quality of Service (0, 1, or 2); QoS 0 is fire-and-forget, QoS 2 guarantees exactly-once delivery.
- **Output** — choose whether to parse JSON payload automatically or pass raw string.
- The node maintains a persistent connection; if the workflow is deactivated the subscription is dropped.
- Retained messages are delivered immediately on subscribe — set `Clean Session = true` to avoid processing stale retained messages.

**Source:** n8n-nodes-base.mqtttrigger.md  [doc-verified]
