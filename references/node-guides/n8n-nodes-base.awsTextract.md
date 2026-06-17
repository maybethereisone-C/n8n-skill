# AWS Textract — `n8n-nodes-base.awsTextract`
**Type** `n8n-nodes-base.awsTextract` · **action**
**What:** Extract structured data from receipts and invoices using AWS Textract's document analysis.
**Credentials:** AWS credential (access key + secret, with Textract permissions).

## Resources / Operations
- Analyze Receipt or Invoice

## Key params & gotchas
- Single operation: AnalyzeExpense — extracts line items, totals, vendor names, dates from receipts/invoices.
- Input must be binary image data (JPEG, PNG) or an S3 object reference — not a URL.
- Returns structured expense fields and line items with confidence scores.
- For general document OCR (forms, tables), use the HTTP Request node with Textract's AnalyzeDocument or DetectDocumentText APIs directly.
- IAM permissions: `textract:AnalyzeExpense`.

**Source:** n8n-nodes-base.awstextract.md  [doc-verified]
