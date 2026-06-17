# Crypto — `n8n-nodes-base.crypto`

**Type** `n8n-nodes-base.crypto` · **typeVersion** 1 · **core**

**What:** Performs cryptographic operations: encrypt/decrypt, hash, HMAC, sign, and generate random strings.

**Credentials:** Crypto credential (stores Hmac Secret, Private Key, Encryption Passphrase, Encryption Public/Private Key). Only needed for Hmac, Sign, Encrypt, Decrypt actions.

**Resources / Operations:**

| Action | Credential Field Used |
|--------|-----------------------|
| Decrypt | Encryption Passphrase (symmetric) or Encryption Private Key (RSA) |
| Encrypt | Encryption Passphrase (symmetric) or Encryption Public Key (RSA) |
| Generate | None |
| Hash | None |
| Hmac | Hmac Secret |
| Sign | Private Key |

**Key params & gotchas:**
- **Encrypt/Decrypt symmetric ciphers**: AES-256-GCM, AES-192-GCM, AES-128-GCM, ChaCha20-Poly1305 — cipher must match between encrypt and decrypt calls.
- **RSA payload size limit**: asymmetric RSA can only encrypt ~190 bytes with a 2048-bit key. Use symmetric mode for any real payload.
- **Encrypt output** is always a Base64 string; pass this directly to Decrypt's **Value** field.
- **Hash types**: MD5, SHA256, SHA3-256/384/512, SHA384, SHA512 — available for both text and binary files.
- **Generate → Type UUID** produces a v4 UUID; length parameter is ignored for UUID type.
- **Property Name** in all actions sets the output field name on the item.

**Source:** n8n-nodes-base.crypto.md  [doc-verified]
