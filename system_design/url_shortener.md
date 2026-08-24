# Design a URL Shortener

[System design guide](./README.md) | [Foundational patterns](./foundational_patterns.md) | [Rate limiter](./rate_limiter.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## The Question

Design a service that creates a short URL for a longer destination and redirects
visitors quickly.

Example:

```text
create:   https://example.short/aB3xQp7 -> https://docs.example.com/a/very/long/path
visit:    GET /aB3xQp7
response: redirect to the saved destination
```

The simple data lookup hides important production questions: key collisions,
abuse, expiration, read scale, caching, tenant domains, analytics, consistency,
and deletion.

## 1. Clarify Requirements

Ask:

1. Are links public, private, or both?
2. Can users choose custom aliases and domains?
3. Can a destination change after creation?
4. Do links expire or get deleted?
5. Is immediate read-after-create required worldwide?
6. What redirect latency and availability are expected?
7. Are click analytics exact, near-real-time, or approximate?
8. Which destinations must be blocked?
9. Do enterprise tenants require isolation, audit, and regional storage?
10. Is the short-code length fixed?

## Assumptions for This Design

- Authenticated customers create managed links; public redirects need no login.
- Automatically generated codes use seven base-62 characters initially.
- Custom aliases are unique inside a domain namespace.
- Redirects use HTTP `302` by default so disabling or changing a link remains
  possible; immutable products may choose `301` deliberately.
- Analytics never blocks redirect.
- Links may expire or be disabled.
- Unsafe or abusive destinations can be blocked before or after creation.

## 2. Estimate Scale

Assume:

- `100 million` new links per month,
- `100` redirects for every create operation,
- `10` times average peak traffic,
- `500` logical bytes of metadata per link before indexes and replicas,
- five-year retention for active links.

### Writes

```text
100,000,000 / 30 days / 86,400 seconds
    = about 39 creates/second average

peak creates
    = about 390/second
```

### Reads

```text
average redirects
    = about 3,900/second

peak redirects
    = about 39,000/second
```

The workload is read-heavy, which makes caching useful.

### Stored Links

```text
100 million/month * 60 months
    = 6 billion links

raw logical metadata
    = 6 billion * 500 bytes
    = about 3 TB
```

Indexes, replicas, analytics, backups, and cache add more.

### Code Space

Base 62 uses lowercase letters, uppercase letters, and digits.

```text
62^7 = about 3.5 trillion possible seven-character codes
```

That is much larger than six billion, but random collision probability still
exists. Enforce uniqueness and retry rather than trusting the size alone.

## 3. API Contract

### Create

```http
POST /v1/links
Authorization: Bearer <token>
Idempotency-Key: 60c1...
Content-Type: application/json
```

```json
{
  "destination": "https://docs.example.com/guide",
  "domain_id": "default",
  "custom_alias": null,
  "expires_at": null
}
```

Response:

```http
HTTP/1.1 201 Created
```

```json
{
  "link_id": "link_123",
  "short_url": "https://example.short/aB3xQp7",
  "destination": "https://docs.example.com/guide",
  "status": "ACTIVE"
}
```

The idempotency key prevents a lost response and retry from creating several
different codes and charges.

### Redirect

```http
GET /aB3xQp7
```

```http
HTTP/1.1 302 Found
Location: https://docs.example.com/guide
Cache-Control: appropriate product policy
```

### Manage

```text
GET    /v1/links/{link_id}
PATCH  /v1/links/{link_id}
DELETE /v1/links/{link_id}
GET    /v1/links/{link_id}/analytics
```

Management always authenticates and authorizes the owner or tenant.

## 4. Data Model

### Link

| Field | Purpose |
| --- | --- |
| `domain_id`, `code` | Unique redirect lookup key |
| `link_id` | Stable management identity separate from public code |
| `tenant_id`, `owner_id` | Authorization boundary |
| `destination` | Validated target URL |
| `status` | Active, disabled, expired, or deleted |
| `created_at`, `expires_at` | Lifecycle |
| `destination_version` | Cache invalidation and audit |
| `policy_state` | Safety decision and version |
| `redirect_type` | 301, 302, or product-supported behavior |

Primary lookup is `(domain_id, code)`. Management queries also need tenant and
link indexes. Avoid listing all links through an unbounded scan; use cursor
pagination.

### Idempotency Record

| Field | Purpose |
| --- | --- |
| `tenant_id`, `idempotency_key` | Unique operation identity |
| `request_hash` | Reject reuse of one key with a different payload |
| `status` | In progress, completed, or failed |
| `link_id` | The one link created by this operation |
| `response_snapshot` | Return the same successful result after a lost response |
| `expires_at` | Bounded retention based on the API retry contract |

Store this record durably. A process-local retry cache cannot protect requests
that reach another instance or arrive after a restart.

## 5. Generate Short Codes

### Option A: Random Base-62 Code

Generate a cryptographically strong random code, attempt conditional insertion,
and retry on collision.

**Strengths:** Decentralized generation, hard to enumerate sequentially, and no
central ID service on the hot create path.

**Costs:** Must handle collisions; code length may need to grow; random database
writes can reduce storage locality.

### Option B: Numeric ID Encoded in Base 62

Allocate a globally unique integer, then encode it.

**Strengths:** No collision and compact.

**Costs:** ID allocation coordination, predictable volume and neighboring links,
and possible hot ranges. Scrambling can hide sequence but adds key management.

### Option C: Hash of Destination

Hash the URL and use a prefix.

**Strengths:** Same destination can map consistently if that is desired.

**Costs:** Prefix collisions, canonicalization ambiguity, destination changes,
tenant privacy, and inability to intentionally create independent links with
separate analytics or expiry.

Use random codes for this design. A unique database constraint is the final
collision authority.

## 6. Code Creation Flow

1. Authenticate and derive tenant.
2. Validate destination syntax, supported protocol, length, tenant policy, and quota.
3. Run abuse or destination policy checks.
4. Claim unique `(tenant_id, idempotency_key)` with a request hash. Return the
   saved response when it is already complete, and reject a changed payload.
5. Generate a candidate code or validate custom alias.
6. In one transaction, insert under unique `(domain_id, code)`, write audit
   state, and mark the idempotency record complete with `link_id` and response.
7. On a code collision, keep ownership of the same idempotent operation and
   retry a bounded number of candidates.
8. If link and idempotency state cannot share a transaction, use a unique
   creator operation ID plus reconciliation so a retry finds the existing link.
9. Invalidate a prior negative cache entry if one may exist.
10. Return the short URL.

If repeated collisions exceed the small retry budget, increase code length or
surface an internal error rather than loop forever.

## 7. Redirect Architecture

```text
visitor
  -> DNS and edge
  -> redirect service
       -> abuse/rate checks
       -> cache lookup by domain + code
            -> hit: validate status/expiry and redirect
            -> miss: link store lookup
                      -> populate positive cache
                      -> emit analytics event asynchronously
                      -> redirect
```

The redirect path should be small. Identity provider, analytics warehouse, and
administrative control plane do not belong in its synchronous critical path for
public links.

## 8. Caching

Cache popular active code mappings. Key by domain, code, and behavior version as
needed.

Define:

- TTL and maximum stale behavior,
- invalidation when destination, status, or expiry changes,
- negative caching for missing codes,
- protection against a hot-link stampede,
- cold-cache capacity,
- tenant and private-link scope.

Negative caching needs a short TTL or explicit invalidation. Otherwise a code
checked just before creation can remain falsely missing.

For disabled or malicious links, fast invalidation matters more than cache hit
rate. The product may require an edge denylist or version check.

## 9. Database and Partitioning

A key-value access pattern fits redirects:

```text
(domain_id, code) -> destination and status
```

Partition by a hash of domain and code to spread reads and writes. A viral code
still creates a read hot key, which the cache and edge absorb.

Strong uniqueness is needed on creation. Redirect reads may use replicas or
eventual consistency only if immediate read-after-create, disable, and update
requirements are met through routing, cache invalidation, or a consistent read.

Do not shard before the measured store needs it, but show the key and migration
path.

## 10. Analytics Off the Critical Path

On redirect, publish a small event asynchronously:

```text
event_id, link_id, timestamp, coarse location, referrer category,
device category, bot signal, privacy/consent context
```

Independent consumers can aggregate counts and detect abuse. At-least-once
delivery means exact event IDs or aggregation methods must handle duplicates.

Decide whether counts are approximate. Privacy policy should minimize IP and
user-agent retention, honor consent, and restrict tenant access. Analytics
failure should not prevent a normal safe redirect.

## 11. Expiration, Update, and Deletion

### Expiration

Check `expires_at` during redirect. A background lifecycle job can remove expired
cache and old storage later; correctness should not depend on cleanup timing.

### Destination Update

Increment version, write audit, invalidate caches, and define how quickly all
regions must stop using the old target.

### Delete or Disable

For security response, disabling should take effect quickly and keep necessary
audit state. Hard deletion follows retention and legal requirements later.

Do not silently recycle an old public code unless the product explicitly accepts
that a historic URL may point to a new owner. The safer default is no reuse.

## 12. Abuse and Security

A public shortener can hide phishing, malware, spam, and unwanted tracking.

Controls include:

- authenticated creation or stricter anonymous quota,
- allow only supported `http` and `https` destinations,
- reject malformed, local, or policy-forbidden destinations as applicable,
- reputation and policy checks at create and periodically afterward,
- report and appeal workflow,
- rapid disable propagation,
- rate limits by account, tenant, route, and abuse signal,
- non-enumerable codes and management IDs,
- safe redirect preview for higher-risk contexts,
- audit access and destination changes,
- no server-side destination fetch unless an isolated scanner safely performs it.

Avoid `javascript:`, `data:`, credentials in URLs, and control characters.

Private links need authentication before redirect or a separate unguessable,
expiring access capability. A hard-to-guess public code alone is not fine-grained
authorization.

## 13. Custom Domains and Aliases

For a custom domain:

1. Verify tenant ownership through a domain challenge.
2. Provision routing and certificates.
3. Namespace aliases by verified `domain_id`.
4. Prevent protected or confusing aliases.
5. Define domain removal and certificate failure behavior.

One tenant's custom alias does not reserve the same alias on every other domain.

## 14. Multi-Region Design

Redirects benefit from regional or edge serving. Creation needs unique codes and
fast visibility.

Options:

- Route creation to a home region and replicate mappings globally.
- Let regions generate random codes and use a globally unique conditional store.
- Allocate disjoint code prefixes or ranges by region.

Tradeoffs involve create latency, collision authority, read-after-create, stale
disable, residency, and region failure.

For a new link, the response can route its first reads to the write region until
replication catches up. For a blocked link, a fast global deny path may override
stale cached destinations.

## 15. Reliability and Failure Modes

| Failure | Behavior |
| --- | --- |
| Create response lost | Same idempotency key returns the original link. |
| Random code collides | Conditional insert fails; generate another within a bounded retry. |
| Cache unavailable | Read the durable store with admission limits and protect it from a stampede. |
| Database unavailable | Serve safe cached active links within policy; new or uncached links fail clearly. |
| Analytics unavailable | Redirect continues; buffer or drop according to analytics guarantee. |
| Disable event delayed | Security deny path overrides cache; alert on propagation SLO. |
| Region fails | Route to healthy region if data and residency permit; preserve management consistency. |
| Link expires during cache TTL | Cache value includes expiry and redirect checks it locally. |
| Destination becomes unsafe later | Re-scan or receive reputation signal, disable, invalidate, and audit. |

## 16. Observability

- Create rate, errors, latency, and collision retries
- Redirect rate, p50/p95/p99 latency, cache hit rate, and store load
- Not found, expired, disabled, and blocked results
- Hot codes, hot domains, partitions, and regional replication lag
- Cache invalidation and disable propagation time
- Analytics lag and duplicate handling
- Abuse reports, policy decisions, appeals, and false positives
- Stored links, expirations, deletions, and cost per active link/redirect

Avoid exposing destination URLs in broad logs without a privacy and access need.

## Complexity

Let `K` be the number of stored links.

- Create is expected `O(1)` for random generation and indexed conditional insert,
  with rare bounded collision retries.
- Redirect is expected `O(1)` cache or key lookup.
- Storage is `O(K)` plus analytics events or aggregates.
- Listing a page is `O(P)` returned items with cursor pagination, not `O(K)`.

Network, cache misses, hot keys, and replication dominate the constant lookup.

## Edge Cases

- Same idempotency key with a different destination.
- Custom alias differs only by case under domain policy.
- Destination URL is extremely long or malformed.
- Code exists but is expired, disabled, deleted, or under review.
- Negative cache exists immediately before successful creation.
- Link is disabled while a redirect response is cached at the edge.
- Destination changes from safe to malicious.
- Viral link overwhelms one cache node or analytics partition.
- Custom domain ownership expires or changes.
- Redirect loop points through short links back to itself.

## Test the Design Aloud

### Lost Create Response

> The link row commits but the response is lost. The client retries with the same
> tenant-scoped idempotency key and request hash, receives the original code, and
> creates no second link or charge.

### Hot Link

> One code becomes viral. Edge and regional caches absorb reads; request coalescing
> protects the backing store on miss. Analytics is partitioned or sampled so it
> cannot slow redirect.

### Emergency Disable

> Safety marks a destination blocked, writes durable status, publishes invalidation,
> and adds a fast deny override. Every redirect checks status or the deny version,
> and propagation SLO is monitored.

## Common Mistakes

- Choosing a code scheme without estimating key space or handling collisions.
- Using destination hash and assuming same URL must mean same link.
- Blocking redirect on analytics storage.
- Caching without expiry or disable invalidation.
- Treating random codes as private authorization.
- Reusing expired codes and surprising old-link visitors.
- Ignoring abuse because redirect is "only a lookup."
- Claiming eventual replication while promising instant global disable.
- Using offset pagination for a huge changing tenant link list.

## Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| Use 301 or 302? | 301 enables durable client/cache behavior for immutable links; 302 preserves control for updates, analytics, and disable. Match product contract. |
| Support one-time links. | Use strongly consistent conditional consume state; caching normal redirects is unsafe for the one-time guarantee. |
| Support private links. | Authenticate before lookup or issue a scoped expiring capability; public code entropy alone is not enough. |
| Count clicks exactly. | Define identity and duplicate semantics, accept more coordination, and keep billing-grade counters separate from approximate analytics. |
| Shorten the same URL once. | Define canonicalization and ownership; deterministic reuse changes analytics, expiry, privacy, and update semantics. |

## Two-Minute Interview Summary

> I would clarify public versus private access, custom aliases, mutability,
> expiration, analytics, and global visibility. The create API validates and
> policy-checks the destination, uses a tenant idempotency key, generates a random
> seven-character base-62 code, and conditionally inserts under a unique domain
> and code key. Redirect is a small read-heavy path through edge and regional
> cache to a partitioned key lookup, returning 302 by default. Analytics publishes
> asynchronously. I would deep-dive on collisions, cache invalidation, immediate
> disable, abuse, custom domains, read-after-create, and multi-region replication,
> then test lost responses, hot links, stale caches, unsafe destinations, expiry,
> and regional failure.

## Check Your Understanding

### Question 1: Why a Unique Constraint?

If seven base-62 characters give trillions of possibilities, why still require a
unique insert and retry?

<details>
<summary>Show answer and explanation</summary>

Random generation can collide before the space is full. A large space makes the
probability small, not zero, and concurrency means two creators can choose the
same candidate at once. Only an atomic unique constraint or equivalent ownership
operation proves that one code maps to one link.

The service retries with another random code. Monitoring collision rate can show
a broken random generator, attack, or need for longer codes.

</details>

### Question 2: Design One-Time Links

A link must reveal a secret exactly once. What changes from the normal redirect?

<details>
<summary>Show answer and detailed explanation</summary>

1. Use a high-entropy capability token and store only an appropriate hash where
   possible.
2. Keep the secret encrypted separately with strict retention.
3. On access, perform one strongly consistent conditional transition from
   `UNUSED` to `CONSUMED` and return the secret only to the winner.
4. Do not serve the secret through ordinary redirect caches or analytics logs.
5. Define whether a response lost after consumption can be recovered; exactly
   once delivery to a human cannot be guaranteed across a lost network response.
6. Add expiry, attempt rate limit, audit, and immediate revocation.
7. Test simultaneous requests, lost response, stale replica, expired token,
   guessed token, and administrative access.

This is no longer an eventually consistent public redirect. The single-use state
requires a stronger consistency boundary and an honest lost-response contract.

</details>
