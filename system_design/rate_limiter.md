# Design a Distributed Rate Limiter

[System design guide](./README.md) | [Foundational patterns](./foundational_patterns.md) | [Image platform](./image_generation_platform.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## The Question

Design a service that decides whether an API request is allowed under configured
rate and burst limits.

A rate limiter can protect:

- service capacity,
- fair tenant access,
- abuse and credential attacks,
- external dependency quotas,
- inference or data-processing budget.

It is one protective layer, not a replacement for authentication, authorization,
fraud detection, or capacity planning.

## 1. Clarify the Contract

Ask:

1. What identity is limited: IP, user, API key, tenant, endpoint, or combination?
2. Is the rule requests per second, weighted cost, concurrent work, or daily budget?
3. How much short burst is allowed?
4. Is the decision local, regional, or globally shared?
5. What accuracy and added latency are acceptable?
6. What happens when the limiter is unavailable?
7. How quickly do configuration changes apply?
8. Are there priority tiers or reserved capacity?
9. What response and headers must clients receive?
10. Which endpoints have high security or financial consequences?

## Assumptions for This Design

- Limit by `(tenant_id, route_group)` with optional stricter user or IP rules.
- Support weighted requests, so an expensive generation can cost more than a read.
- Allow configured bursts while enforcing a long-term average.
- Make a decision in a few milliseconds at peak.
- Operate regionally by default; explicitly configured global budgets use a
  stronger cross-region design.
- Return `429 Too Many Requests` with retry guidance on a normal rejection.
- Use different failure policy for low-risk reads and high-risk writes.

## 2. Compare Algorithms

| Algorithm | Strength | Limitation |
| --- | --- | --- |
| Fixed window counter | Very simple and compact | A caller can burst at both sides of a window boundary |
| Sliding log | Exact recent request history | Stores and removes many timestamps |
| Sliding window counter | Better boundary behavior with compact counts | Approximate and slightly more calculation |
| Leaky bucket | Smooths output at a steady drain rate | Often behaves like a queue and needs overflow policy |
| Token bucket | Allows bounded bursts while enforcing average refill | Requires atomic time-based state update |

Use a token bucket as the main design because APIs often need both an average
rate and a controlled burst.

## 3. Token Bucket From Scratch

Each key stores:

```text
capacity         maximum saved tokens
refill_rate      tokens added per second
tokens           current available tokens
last_refill      timestamp used for the last calculation
```

A request has a token `cost`.

### Decision

```text
elapsed = now - last_refill
refilled = min(capacity, tokens + elapsed * refill_rate)

if refilled >= cost:
    allow
    tokens = refilled - cost
else:
    reject
    tokens = refilled
```

Save the new token count and refill timestamp atomically with the decision.

### Example

Capacity is 10 tokens and refill is 2 tokens/second.

```text
time 0: bucket has 10
request costs 7 -> allow, 3 remain
after 2 seconds -> 3 + 4 = 7 available
request costs 8 -> reject, needs 1 more token
retry after about 0.5 seconds
```

## 4. Correctness Invariants

1. Stored tokens never fall below zero or exceed capacity.
2. One accepted request deducts its cost exactly once from the relevant rules.
3. Concurrent decisions for one key are serialized or updated atomically.
4. A caller cannot choose another tenant's rate-limit identity.
5. Configuration version and decision reason are observable.
6. Rejected requests do not consume protected downstream capacity.

## 5. API and Placement

The limiter may run:

- inside an API gateway,
- as a shared low-latency service,
- as a library with shared state,
- at both local and global layers.

A gateway integration is useful because rejection happens before expensive
application work. The application may still enforce business-specific limits
after it knows request cost or resource ownership.

Internal decision interface:

```http
POST /v1/rate-limit/check
```

```json
{
  "subject": "tenant_123",
  "route_group": "image_generation",
  "cost": 4,
  "request_id": "request_456"
}
```

The caller must be an authenticated trusted service. An external user must not
submit arbitrary `subject` values.

Response:

```json
{
  "allowed": false,
  "limit": 120,
  "remaining": 2,
  "retry_after_ms": 1000,
  "policy_version": "policy_17",
  "reason": "tenant_generation_rate"
}
```

Public API rejection commonly includes:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 1
```

Remaining-quota headers are estimates under concurrency unless the contract
promises exact values.

## 6. Data Model and Key

```text
bucket key:
    policy scope + trusted subject + route group + region if regional

bucket value:
    tokens, last_refill, policy_version, expiry
```

Do not include raw secrets in the key. Hash or map sensitive API keys to internal
identities after authentication.

Expire an idle bucket after enough time to refill fully plus a safety margin. A
missing bucket starts full under a normal burst-friendly policy.

## 7. High-Level Architecture

```text
client
  -> edge or API gateway
       -> authenticate and derive subject
       -> load matching policy
       -> atomic bucket decision store
            -> allow: forward to application
            -> reject: return 429

configuration control plane
  -> validate and version policy
  -> publish to gateway/limiter caches

decision metrics and sampled audit
  -> dashboards, alerts, abuse analysis, billing reconciliation
```

Keep policy management separate from the hot decision path. A slow administrative
database should not be read on every request.

## 8. Atomic Distributed Decision

Several gateway instances may check the same tenant concurrently. A normal
read-modify-write race can allow both requests to spend the same token.

Use one atomic operation in a shared low-latency store:

```text
atomically:
    read bucket
    compute refill with server time
    compare available tokens with cost
    update tokens and timestamp
    return decision and retry time
```

Implementation options include a transaction, compare-and-swap loop, or
server-side script supported by the chosen store. Benchmark contention and
failure behavior.

## 9. Scale Estimate

Assume:

- `100,000` peak incoming API requests/second,
- each request checks two rules on average,
- `2,000,000` active bucket keys during a busy hour,
- a compact logical bucket is about `64` bytes before database overhead and replicas.

```text
peak decisions/second = 100,000 * 2
                      = 200,000

raw bucket bytes = 2,000,000 * 64
                 = about 128 MB
```

Actual memory can be several times larger because of keys, metadata, indexes,
allocator overhead, replicas, and persistence. The hard problem is often hot-key
atomic throughput, not raw storage.

## 10. Partitioning and Hot Keys

Partition by a stable hash of the complete bucket key. This spreads ordinary
tenants.

A single enormous tenant or shared anonymous IP can still be hot. Options:

- use hierarchical local and global buckets,
- reserve dedicated limiter partitions for very large tenants,
- split a global budget into regional allowances and reconcile,
- limit concurrency as well as request rate,
- apply coarser edge protection before the precise tenant rule.

Splitting one exact bucket across shards can overshoot because each shard spends
part of the allowance independently. Quantify and accept the error or coordinate
more strongly.

## 11. Hierarchical Limits

One request may need all of these:

```text
global emergency limit
tenant plan limit
user abuse limit
route cost limit
concurrent-job limit
daily budget
```

Evaluate cheap broad limits first. Define whether a rejected request consumes any
earlier reservation and how partial multi-rule updates are repaired.

For strict atomicity across several buckets, keep related keys colocated or use a
transaction. For less strict protection, small bounded overrun may be acceptable
and much cheaper. State the business consequence.

## 12. Regional and Global Limits

### Regional

Each region has its own bucket. Fast and resilient, but a tenant using three
regions may receive roughly three times a nominal global allowance unless budgets
are divided.

### Globally Coordinated

One globally consistent decision or owner preserves an exact shared budget but
adds cross-region latency and availability dependency.

### Allocated Budget

Divide a global budget among regions and periodically rebalance unused tokens.
This provides local speed with bounded overshoot or underuse.

Choose based on whether the limit protects approximate fairness or a hard
financial/security boundary.

## 13. Time and Clock Safety

Clock movement can create or remove tokens incorrectly.

- Prefer server-side or monotonic elapsed time within one owner.
- Never trust a client timestamp.
- Clamp negative elapsed time to zero.
- Cap refill at bucket capacity.
- Record policy and store time behavior in tests.
- For multi-region coordination, avoid assuming perfectly synchronized clocks.

## 14. Failure Policy

The limiter can fail too.

### Fail Open

Allow requests temporarily. Good when availability is more important and the
downstream has its own capacity protection. Risk: abuse and overload.

### Fail Closed

Reject when no trustworthy decision is available. Good for login abuse,
expensive operations, hard budget, or high-impact writes. Risk: limiter outage
becomes product outage.

### Degraded Local Limit

Use a conservative in-process emergency bucket while shared state is unavailable.
This sacrifices global accuracy but bounds one instance.

Choose by endpoint. A public product read and a costly money-moving write should
not automatically share failure behavior.

## 15. Configuration Safety

Policies need:

- schema validation,
- version and author,
- tenant and route scope,
- effective time,
- preview of affected traffic,
- staged rollout,
- rollback,
- bounds preventing accidental zero or unlimited settings,
- break-glass control with audit and expiry.

Cache policies on the hot path and distribute invalidation events. Keep a safe
last-known version when the control plane is unavailable.

## 16. Observability

Measure:

- allowed and rejected requests by policy and reason,
- decision latency and store errors,
- active keys and memory,
- hot keys and partition imbalance,
- token cost distribution,
- fail-open, fail-closed, and degraded-local events,
- 429 retry behavior,
- downstream saturation despite the limiter,
- configuration changes and rollback,
- tenant complaints and false-positive abuse blocks.

Do not log raw credentials or every high-volume decision indefinitely.

## Complexity

For one token bucket check:

- Expected decision time is `O(1)` arithmetic plus one atomic store operation.
- Stored state is `O(K)` for `K` active bucket keys.
- A sliding-log alternative can require `O(R)` timestamps for `R` requests in the
  window and removal work, which is why token bucket is more compact.

Network and contention latency dominate the constant arithmetic.

## Edge Cases

- First request for a missing bucket.
- Request cost exceeds total bucket capacity.
- Two requests arrive at the same instant for the last token.
- Clock appears to move backward.
- Policy changes while requests are in flight.
- Tenant sends traffic through several regions.
- One shared corporate IP represents thousands of legitimate users.
- Limiter store is slow or unavailable.
- Client retries a rejected non-idempotent operation.
- A zero-cost or negative-cost request appears because of bad configuration.

## Test the Design Aloud

### Boundary Burst

> A bucket has capacity ten, zero current tokens, and refills two per second. At
> two seconds it has four tokens. Two concurrent cost-three requests cannot both
> succeed because the decision is atomic; one spends three and the other sees one.

### Limiter Outage

> Login attempts fail closed or use a conservative local emergency limit because
> unlimited attempts create security risk. A low-risk cached product read may
> fail open while downstream admission control remains active. Both modes emit an
> alert and metric.

### Multi-Tenant Fairness

> Tenant A exhausts its generation bucket. Its requests receive 429, while tenant
> B's separate bucket and scheduler capacity remain available. A global emergency
> limit can still protect the whole fleet.

## Common Mistakes

- Limiting only by IP and blocking a whole enterprise office.
- Updating token state with a non-atomic read and write.
- Using client clocks.
- Treating a regional count as an exact global limit.
- Returning 500 for a normal quota rejection.
- No burst definition, so callers cannot use idle capacity.
- Rate limiting requests while expensive requests have very different cost.
- Fail-open for a hard billing or security boundary without another control.
- Storing every request timestamp when a compact algorithm satisfies accuracy.

## Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| Support request weights. | Deduct configured cost; reject impossible cost above capacity or route to a different policy. |
| Limit concurrent jobs. | Use a semaphore-like lease count released on terminal state or expiry, not only a per-second bucket. |
| Give premium tenants reserved capacity. | Separate quotas and scheduler pools while preserving a global safety ceiling. |
| Need an exact global daily spend cap. | Use strongly coordinated reservation/ledger state; a fast regional token estimate is insufficient. |
| Prevent retry storms after 429. | Return retry guidance and require exponential backoff with jitter; avoid one synchronized reset boundary. |

## Two-Minute Interview Summary

> I would clarify identity, average rate, burst, weighted cost, geographic scope,
> and failure policy. I would use a token bucket per trusted tenant and route
> because it enforces average refill while allowing a bounded burst. Gateway
> instances execute one atomic refill-and-deduct operation in a partitioned
> low-latency store and return 429 with retry guidance on rejection. Policies are
> versioned and cached separately from the hot path. I would address hot tenants,
> regional versus global accuracy, clock behavior, hierarchical limits, and
> endpoint-specific fail-open or fail-closed behavior, then monitor decision
> latency, rejections, hot keys, degraded mode, downstream saturation, and fairness.

## Check Your Understanding

### Question 1: Trace a Token Bucket

Capacity is 5, refill is 1 token/second, and the bucket starts full. At time zero,
requests cost 3, 2, and 1 tokens in that order. At time two, another request costs
2. Which requests succeed?

<details>
<summary>Show answer and explanation</summary>

- First cost-3 request succeeds; 2 remain.
- Cost-2 request succeeds; 0 remain.
- Cost-1 request at the same time fails.
- Two seconds add 2 tokens.
- The final cost-2 request succeeds and leaves 0.

Concurrent requests at one timestamp still need one atomic ordering so they
cannot both spend the same token.

</details>

### Question 2: Combine Tenant and User Limits

An enterprise plan allows 1,000 requests/minute, but one compromised user must
not consume all of it. Design the checks.

<details>
<summary>Show answer and detailed explanation</summary>

Use at least two token buckets derived from authenticated identity:

```text
tenant bucket: (tenant_id, route_group)
user bucket:   (tenant_id, user_id, route_group)
```

The request is allowed only if both policies allow it. The tenant bucket protects
plan capacity; the smaller user bucket limits one account. Add an IP or credential
abuse rule where useful, but do not rely on shared IP alone.

For atomic spending, colocate related keys and use a transaction or a reservation
protocol. If small bounded overrun is acceptable, evaluate rules independently
and reconcile failed partial deductions. State that tradeoff instead of assuming
two remote writes are one operation.

Monitor rejection reason separately so support can distinguish tenant exhaustion
from one-user abuse. Provide administrative changes with version, expiry, and
audit.

</details>
