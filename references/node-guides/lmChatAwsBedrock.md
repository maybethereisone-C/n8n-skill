# AWS Bedrock Chat Model — `@n8n/n8n-nodes-langchain.lmChatAwsBedrock`
**Type** `@n8n/n8n-nodes-langchain.lmChatAwsBedrock` · **typeVersion** 1 · **ai (sub-node / LLM)**
**What:** Sub-node providing AWS Bedrock-hosted LLMs (Claude, Llama, Titan, Mistral, etc.) to AI root nodes (Agent, Chain, etc.).
**Credentials:** `aws` (IAM access key) or `awsAssumeRole` (temporary role assumption).
**Resources / Operations:** LLM provider — no standalone operations; connects to root AI nodes via the `ai_languageModel` connection type.

**Key params & gotchas:**
- **Authentication**: choose IAM (long-lived key) or Assume Role (short-lived, preferred for production).
- **Model**: select from available Bedrock foundation models; see [Amazon Bedrock model list](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). Model availability varies by AWS region.
- **Maximum Number of Tokens**: sets completion length limit.
- **Sampling Temperature**: 0 = deterministic, higher = more creative/random.
- Does NOT support the `NO_PROXY` environment variable — traffic always goes direct to AWS endpoints.
- Bedrock requires the model to be enabled in your AWS account/region before use (request access in AWS console).
- Sub-node expression resolution: parameters using `{{ }}` expressions are evaluated at workflow runtime, not design time.

**Source:** n8n-nodes-langchain.lmchatawsbedrock.md  [doc-verified]
