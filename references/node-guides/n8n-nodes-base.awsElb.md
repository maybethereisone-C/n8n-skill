# AWS Elastic Load Balancing — `n8n-nodes-base.awsElb`
**Type** `n8n-nodes-base.awsElb` · **action**
**What:** Manage AWS Application and Network Load Balancers and their listener certificates.
**Credentials:** AWS credential (access key + secret, with ELB permissions).

## Resources / Operations
| Resource | Operations |
|---|---|
| Listener Certificate | Add, Get Many, Remove |
| Load Balancer | Create, Delete, Get, Get Many |

## Key params & gotchas
- **Gateway Load Balancers are not supported** — only Application (ALB) and Network (NLB) load balancers.
- Listener Certificate ops require a **Listener ARN** (not the load balancer ARN).
- Load Balancer/Create requires subnets and security groups (ALB) or subnets (NLB).
- IAM permissions: `elasticloadbalancing:*` or scoped permissions per operation.

**Source:** n8n-nodes-base.awselb.md  [doc-verified]
