# Paddle — `n8n-nodes-base.paddle`
**Type** `n8n-nodes-base.paddle` · **action**
**What:** Manage Paddle billing — coupons, payments, plans, products, and users.
**Credentials:** `paddleApi`

## Resources / Operations
| Resource | Operation |
|----------|-----------|
| Coupon | Create, Get All, Update |
| Payment | Get All, Reschedule |
| Plan | Get, Get All |
| Product | Get All |
| User | Get All |

## Key params & gotchas
- Paddle's classic API (v1/v2) is implied; does not target Paddle Billing (v2 new stack). Verify your account tier.
- "Reschedule payment" changes the next bill date for a subscription payment.
- No Coupon Delete operation — use Paddle dashboard for removal.

**Source:** n8n-nodes-base.paddle.md  [doc-verified]
