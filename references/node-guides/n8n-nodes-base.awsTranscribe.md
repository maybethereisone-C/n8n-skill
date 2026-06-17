# AWS Transcribe — `n8n-nodes-base.awsTranscribe`
**Type** `n8n-nodes-base.awsTranscribe` · **action**
**What:** Create and manage AWS Transcribe speech-to-text jobs that convert audio files to text.
**Credentials:** AWS credential (access key + secret, with Transcribe permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Transcription Job | Create, Delete, Get, Get All |

## Key params & gotchas
- **Async workflow:** Transcription jobs are asynchronous — Create starts the job, then poll with Get until status is COMPLETED before reading the transcript.
- Audio source must be in **S3** — specify an S3 URI (`s3://bucket/key`). Local files must be uploaded to S3 first.
- Supported formats: MP3, MP4, WAV, FLAC, OGG, AMR, WebM.
- Language code must be specified (e.g. `en-US`) unless auto language detection is enabled.
- Transcript output is written to an S3 bucket (auto-managed by Transcribe or a custom bucket you specify).
- IAM permissions: `transcribe:StartTranscriptionJob`, `transcribe:GetTranscriptionJob`, `transcribe:DeleteTranscriptionJob`, `transcribe:ListTranscriptionJobs`.

**Source:** n8n-nodes-base.awstranscribe.md  [doc-verified]
