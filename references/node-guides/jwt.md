# JWT — `n8n-nodes-base.jwt`
**Type** `n8n-nodes-base.jwt` · **core**

**What:** Creates, verifies, and decodes JSON Web Tokens within a workflow.

**Credentials:** JWT credential (holds algorithm + secret/key).

**Resources / Operations:**
| Operation | Notes |
|-----------|-------|
| Decode | Returns payload (default) or full header+signature with Return Additional Info |
| Sign | Builds and signs a JWT; payload via GUI claims or raw JSON |
| Verify | Validates signature and claims; errors if invalid |

**Key params & gotchas:**
- **Sign → Use JSON to Build Payload** switches payload input to a raw JSON editor.
- Standard claims available in Sign: `aud`, `exp`, `iss`, `jti`, `nbf`, `sub`.
- **Verify → Ignore Expiration** / **Ignore Not Before Claim** skip time-based claim validation.
- **Verify → Clock Tolerance** (seconds) accommodates minor server clock drift.
- **Override Algorithm** on Sign/Verify overrides the credential's default algorithm.
- Can be used as an AI tool node.

**Source:** n8n-nodes-base.jwt.md  [doc-verified]
