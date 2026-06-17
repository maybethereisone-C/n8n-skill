# Netscaler ADC — `n8n-nodes-base.netscaleradc`
**Type** `n8n-nodes-base.netscaleradc` · **typeVersion** 1 · **action**
**What:** Manage SSL/TLS certificates and file objects on a Citrix Netscaler ADC appliance.
**Credentials:** `netscalerAdcApi`

## Resources / Operations

| Resource | Operation |
|---|---|
| Certificate | Create |
| Certificate | Install |
| File | Delete |
| File | Download |
| File | Upload |

## Key params & gotchas

- **Certificate → Create** generates a self-signed certificate on the ADC; **Install** binds an existing cert/key pair to an SSL virtual server — these are distinct actions, not a combined flow.
- File operations target the ADC's local file system (e.g., `/nsconfig/ssl/`); paths must match the appliance's directory structure exactly.
- No "Get" or "List" operation exists for either resource — retrieval of cert/file state must be done via the ADC API directly if needed.
- Credentials require direct network access to the ADC management interface; not reachable through cloud n8n instances without a tunnel or VPN.

**Source:** n8n-nodes-base.netscaleradc.md  [doc-verified]
