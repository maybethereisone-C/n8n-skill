# Guardrails — `@n8n/n8n-nodes-langchain.guardrails`

**Type** `@n8n/n8n-nodes-langchain.guardrails` · **typeVersion** 3.4 · **ai**

**What:** Enforces safety, content, and data-leakage policies on text — validate user input before sending to AI, or scrub AI output before using downstream.

**Credentials:** none (uses connected Chat Model node for LLM-based checks).

**Resources / Operations:**

| Operation | Description |
|---|---|
| Check Text for Violations | Full guardrail set; violations route items to Fail output |
| Sanitize Text | Detects URLs, regex, secret keys, PII and replaces with placeholders |

**Key params & gotchas:**

- **Chat Model required** for LLM-based guardrails (Jailbreak, NSFW, Topical Alignment, Custom). Connect a Chat Model sub-node to the Model input.
- **Check Text for Violations** — outputs two branches: pass and fail. Items with any violation go to Fail.
- **Guardrail types:**
  - `Keywords` — exact keyword blocklist (comma-separated).
  - `Jailbreak` — LLM-based; `Threshold` 0–1 (higher = stricter). Customizable prompt.
  - `NSFW` — LLM-based; same threshold pattern.
  - `PII` — regex/NLP scan; choose All entities or specific types (`CREDIT_CARD`, `EMAIL_ADDRESS`, `PHONE_NUMBER`, `US_SSN`, etc.).
  - `Secret Keys` — API key / credential detection; Permissiveness: Strict / Balanced / Permissive.
  - `Topical Alignment` — LLM-based; define the allowed topic in Prompt; threshold flags off-topic content.
  - `URLs` — blocks all URLs by default; allowlist via `Block All URLs Except`; supports scheme filtering, subdomain allowance, and userinfo blocking.
  - `Custom` — LLM-based; write your own detection prompt + threshold.
  - `Custom Regex` — pure regex patterns; name is used as placeholder in Sanitize mode.
- **Sanitize mode** — does not route to Fail; replaces violations inline (e.g. `[PHONE_NUMBER]`). Only supports: URLs, regex, secret keys, PII.
- **Customize System Message** — global override for the guardrail system prompt; changes JSON schema enforcement behavior.

**Source:** n8n-nodes-langchain.guardrails.md  [doc-verified]
