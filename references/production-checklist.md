# Production Checklist (n8n v2.26.0)

> A pre-ship gate. Run every box before declaring a workflow production-ready. Cross-references error-handling.md, logging-observability.md, security.md.

## Before you build / reality check

**Wireframe first.** Spend >50% of build time planning (Excalidraw or equivalent) before touching the n8n builder. Answer each of these before a single node is dragged:
- What is the trigger and what shape does the incoming data have?
- Where does branch logic occur and what are the branches?
- Where is AI actually needed — and where is a plain IF node enough?
- Is this RAG enrichment, API enrichment, or neither?
- What external integrations does it touch?
- Must steps execute in the same order every run? → workflow. Order varies or depends on context? → agent. (See references/agent-craft.md for the full workflow-vs-agent decision.)

Prevents end-of-build rework when you discover mid-build that the data shape was wrong or a branch condition was unhandled.

**Demos ≠ production.** Online templates — including course and instructor examples — are proofs-of-concept. They break on edge cases, multiple concurrent users, and real data variance. Do not ship a POC as production; use this checklist.

**Know n8n's limits.** n8n excels at rule-based logic, AI-enhanced workflows, and multi-agent orchestration. It is weak at enterprise scale (millions of users), heavy OAuth/token/session management, and very custom processing logic. For those cases: n8n as orchestrator + custom Python (or other service) for the heavy/secure work.

---

This is a hard gate, not a suggestion. An agent shipping a workflow MUST walk every section and not declare "done" until each applicable box is checked or explicitly N/A with a reason.

## Correctness
- [ ] Trigger is the right type (webhook/schedule/poll) and configured for the real cadence.
- [ ] Happy path produces the expected output on representative data.
- [ ] Edge cases handled: empty input, missing fields, large batches, duplicate items.
- [ ] Expressions reference real fields (`$json.x`), no leftover placeholders/test values.
- [ ] No `executeOnce` left on by accident where all items must be processed.

## Errors
- [ ] An **Error Workflow** (`n8n-nodes-base.errorTrigger`) is assigned in Workflow Settings.
- [ ] Critical nodes use `onError: stopWorkflow`; recoverable ones use `continueErrorOutput` with a wired `main[1]` branch.
- [ ] Business-rule violations throw via `n8n-nodes-base.stopAndError` with a clear message.
- [ ] Input is validated with IF/guard nodes before side-effecting nodes.

## Retries / Timeouts
- [ ] Every network-I/O node sets `retryOnFail: true`, `maxTries` 3–5, `waitBetweenTries` ≥ 1000ms.
- [ ] Outbound HTTP has sane timeouts; long loops are throttled to respect upstream rate limits.
- [ ] Workflow has a timeout where appropriate so it can't hang indefinitely.

## Logging
- [ ] Instance log envs set: `N8N_LOG_LEVEL=info`, `N8N_LOG_FORMAT=json`, `N8N_LOG_OUTPUT=console,file`.
- [ ] Execution pruning configured: `EXECUTIONS_DATA_PRUNE=true`, `SAVE_ON_ERROR=all`, age/count caps set.
- [ ] App-level run-log row appended at workflow end (status, timestamp, items, errors), node set to `continueRegularOutput`.
- [ ] Failure alerting flows through the error workflow (Slack/email/PagerDuty).

## Security
- [ ] **No** secrets in node `parameters` — all auth via n8n credentials (referenced by id).
- [ ] Every public webhook uses `basicAuth` / `headerAuth` / `jwtAuth` (never `none` unless behind an authenticating proxy).
- [ ] Webhook payloads validated before use.
- [ ] User-supplied URLs in HTTP Request validated against an allowlist (SSRF guard).
- [ ] `N8N_ENCRYPTION_KEY` set and managed in a secret store; credentials scoped least-privilege; 2FA on; workers isolated in queue mode.

## Idempotency
- [ ] Re-running on the same input does not duplicate side effects (upsert / dedupe key / "already processed" check).
- [ ] At-least-once delivery assumed for webhooks/queues — handle replays.
- [ ] External writes use a stable idempotency key where the API supports one.

## Performance
- [ ] Large datasets batched (Loop Over Items / batching node), not loaded whole into memory.
- [ ] No N+1 calls where a bulk/batch API exists.
- [ ] `EXECUTIONS_DATA_SAVE_ON_PROGRESS=false` unless step-level resume is genuinely needed.
- [ ] Pagination handled for any list/search API.

## Versioning
- [ ] Every node has an explicit `typeVersion` **pinned** (no implicit/latest) so behavior is reproducible across upgrades.
- [ ] Workflow is exported/committed to version control; changes reviewed.
- [ ] Credentials referenced by id exist in the target environment (dev/stage/prod parity).

## Automated validation (complementary)

Run the **czlonkowski n8n MCP** validation as a machine check alongside this manual gate. Profiles, increasing strictness:

| Profile | Scope |
|---|---|
| `minimal` | Required fields present only — fastest sanity check. |
| `runtime` | Required + values that would fail at execution time. |
| `ai-friendly` | Balanced; tuned defaults for agent-built workflows. |
| `strict` | Full validation incl. best-practice/lint warnings — use as the ship gate. |

Treat `strict` (or at least `runtime`) passing as a prerequisite, **not** a replacement for this checklist — automated validation catches structural/required-field errors; it does not verify idempotency, security posture, retry policy, or business correctness.

**Calibration — don't chase false positives.** `strict` generically flags "missing error handling", "no retry logic", "missing rate limiting", "unbounded query". If the Errors / Retries / Security / Performance sections above are already satisfied (error workflow assigned, `retryOnFail` set, webhook auth on, batching in place), those warnings are **expected noise on an already-hardened workflow** — record them as intentional/N-A, don't re-architect to silence a linter. The validator can't see that *this* checklist already covered them.

## Gate verdict
- [ ] All applicable boxes checked or explicitly N/A with reason.
- [ ] `strict`/`runtime` validation passes.
- [ ] Then, and only then, declare the workflow production-ready.

## Resilience (long-running / flaky APIs / bulk) — see resilience.md
- [ ] Work is **batched** (Loop Over Items / pagination), not one monolithic node
- [ ] Progress **checkpointed** to a durable store; restart resumes from last point, not zero
- [ ] Expensive pulls **staged raw** before processing (crash never forces a re-pull)
- [ ] All writes **idempotent** (append-or-update by key / upsert / removeDuplicates)
- [ ] Flaky write node uses `onError: continueErrorOutput` → **dead-letter** sink; good items continue
- [ ] Transient errors: `retryOnFail` + `maxTries` + rising `waitBetweenTries`; batch size tuned for API quota (429)
- [ ] Error workflow alert names the **failed batch/cursor** + execution URL for targeted re-run
