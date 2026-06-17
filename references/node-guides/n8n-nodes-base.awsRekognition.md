# AWS Rekognition — `n8n-nodes-base.awsRekognition`
**Type** `n8n-nodes-base.awsRekognition` · **action**
**What:** Analyze images using AWS Rekognition computer vision (labels, faces, text, moderation).
**Credentials:** AWS credential (access key + secret, with Rekognition permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Image | Analyze |

## Key params & gotchas
- Single operation: Analyze — what it detects depends on the **Type** parameter (Labels, Faces, Text, Moderation Labels, etc.).
- Image source can be an S3 object or base64-encoded binary; specify via **Image Source** param.
- Returns confidence scores alongside detected entities; filter by MinConfidence param.
- IAM permissions: `rekognition:DetectLabels`, `rekognition:DetectFaces`, `rekognition:DetectText`, `rekognition:DetectModerationLabels` (depending on type).

**Source:** n8n-nodes-base.awsrekognition.md  [doc-verified]
