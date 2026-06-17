# MQTT — `n8n-nodes-base.mqtt`
**Type** `n8n-nodes-base.mqtt` · **typeVersion** 1 · **action**
**What:** Publish a message to an MQTT topic (action node — for subscribing/receiving use the MQTT Trigger).
**Credentials:** MQTT broker connection (`mqtt`) — host, port, protocol (mqtt/mqtts/ws/wss), optional username/password and TLS config.
**Resources / Operations:**
| Operation |
|---|
| Send message to a topic |

**Key params & gotchas:**
- Set the **Topic**, **QoS** level (0/1/2), and whether to **Retain** the message on the broker.
- Optionally send the incoming n8n item data as the message payload (toggle "Send Input Data").
- For receiving MQTT messages use the companion **MQTT Trigger** node (`n8n-nodes-base.mqttTrigger`).
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.mqtt.md  [doc-verified]
