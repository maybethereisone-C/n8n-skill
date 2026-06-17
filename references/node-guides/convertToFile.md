# Convert to File — `n8n-nodes-base.convertToFile`

**Type** `n8n-nodes-base.convertToFile` · **typeVersion** 1 · **core**

**What:** Converts JSON input data to a binary file in various formats (CSV, HTML, ICS, JSON, ODS, RTF, Text, XLS, XLSX, or moves a Base64 string to a file).

**Credentials:** None.

**Resources / Operations:**

| Operation | Output Format |
|-----------|--------------|
| Convert to CSV | .csv |
| Convert to HTML | .html (table) |
| Convert to ICS | .ics (calendar event) |
| Convert to JSON | .json |
| Convert to ODS | .ods (LibreOffice spreadsheet) |
| Convert to RTF | .rtf |
| Convert to Text File | .txt |
| Convert to XLS | .xls |
| Convert to XLSX | .xlsx |
| Move Base64 String to File | any (set MIME type) |

**Key params & gotchas:**
- **Put Output File in Field**: the binary property name where the node places the output file (default `data`). Must reference this name in downstream nodes.
- **ICS operation**: supports rich calendar options — attendees, RRULE recurrence, geolocation, organizer, busy status for Outlook, timezone. UID auto-generated if blank; increment **Sequence** for updates to existing events.
- **Convert to JSON → Mode**: "All Items to One File" bundles all input items; "Each Item to Separate File" creates one file per item.
- **Move Base64 String to File**: set correct MIME type or downstream consumers may mishandle the file.
- **Header Row** option (CSV/XLS/XLSX/ODS/RTF): controls whether the first row is treated as headers.
- Pair with **Extract from File** node for the reverse operation.

**Source:** n8n-nodes-base.converttofile.md  [doc-verified]
