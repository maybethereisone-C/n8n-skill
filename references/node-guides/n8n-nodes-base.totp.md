# TOTP — `n8n-nodes-base.totp`

**Type** `n8n-nodes-base.totp` · **typeVersion** 1 · **core**

**What:** Generates a time-based one-time password (TOTP / RFC 6238) — useful for automating MFA-protected logins or verifying TOTP codes in workflows.

**Credentials:** `totpApi` (TOTP credential — stores the shared secret seed).

**Resources / Operations:**

| Operation | Description |
|---|---|
| Generate Secret | Produce a current TOTP code from the stored secret |

**Key params & gotchas:**

- **Algorithm** (option) — HMAC hash: SHA1 (default, most compatible), SHA256, SHA512. Must match the issuing service.
- **Digits** (option) — code length, default 6. Some services use 8.
- **Period** (option) — validity window in seconds, default 30. Must match the service; 60 is common for enterprise systems.
- The node generates the *current* code at execution time. If execution is delayed (e.g. by a Wait node) the code may expire before use — generate immediately before the step that needs it.
- The TOTP credential stores the base32 secret seed, not the issuer URI; strip `otpauth://totp/...?secret=` and keep only the base32 value.

**Source:** n8n-nodes-base.totp.md  [doc-verified]
