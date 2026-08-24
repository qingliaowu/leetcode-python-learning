# Foundational System Design Patterns

[System design guide](./README.md) | [Image platform](./image_generation_platform.md) | [Cloud fundamentals](../fde_interview/03_cloud_architecture_fundamentals.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Patterns Are Responses to Requirements

A pattern is a reusable response to a recurring force. It is not a box that must
appear in every diagram.

```text
requirement or failure
    -> constraint
    -> pattern
    -> new tradeoff
    -> operating control
```

Example:

```text
Slow processor and bursty uploads
    -> request cannot wait and work must not be lost
    -> durable queue
    -> duplicates and delayed completion are possible
    -> idempotent worker, retries, dead-letter queue, queue-age alert
```

Always explain the full chain.

## Quick Pattern Map

| Signal | Useful Pattern | Question You Must Still Answer |
| --- | --- | --- |
| Expensive repeated reads | Cache | How fresh, invalidated, and recovered? |
| Read traffic exceeds one database | Read replicas | Which reads can tolerate replica delay? |
| Data exceeds one write node | Partition or shard | Which key distributes load and supports queries? |
| Slow background work | Durable queue | How are duplicates, poison jobs, and progress handled? |
| One event needs many consumers | Publish/subscribe | Does each subscription own retry and ordering? |
| Write plus event must agree | Transactional outbox | Who publishes and reconciles unsent events? |
| Retried command has side effects | Idempotency key | What identity and retention define "same command"? |
| Dependency is failing | Timeout, backoff, circuit breaker | What fallback is actually safe? |
| Downstream is full | Backpressure and admission control | Which traffic is delayed, rejected, or degraded? |
| One tenant is noisy | Quotas and fair scheduling | What service promise does each tier receive? |
| Large changing result set | Cursor pagination | What stable order and cursor semantics apply? |
| Multi-step distributed workflow | State machine and compensation | Which step is durable and how is partial work repaired? |

## 1. Caching

A cache stores a reusable result closer to the reader.

### Cache-Aside Flow

```text
read cache
    -> hit: return
    -> miss: read source of truth
             -> populate cache with TTL
             -> return
```

### Questions

- What is the source of truth?
- Which key includes tenant, permissions, locale, and version?
- How stale may data be?
- What invalidates or expires it?
- What happens after a full cache restart?
- How do you prevent many simultaneous misses for one hot key?
- Can negative results be cached safely?
- Is the saved latency or compute worth memory and complexity?

### Common Failure: Stampede

A hot entry expires and thousands of callers recompute it. Controls include
single-flight locking, jittered TTLs, refresh-before-expiry, stale-while-revalidate,
and admission limits.

Never place unauthorized data in a cache key that omits the authorization scope.

## 2. Replication

Replication keeps copies of data for availability or read scale.

### Leader and Replicas

Writes go to a leader; replicas receive changes and serve eligible reads.

Tradeoff: replicas may lag. A user who writes a profile then immediately reads
from a lagging replica may see old data.

Possible controls:

- read your own writes from the leader for a short session,
- wait for a replication position,
- route strongly consistent operations to the leader,
- accept eventual consistency for feeds or analytics.

Replication is not backup. A bad delete can replicate perfectly.

## 3. Partitioning and Sharding

Partitioning divides data so several nodes share storage and work.

### Key Choice

A good partition key:

- distributes load and bytes,
- supports common access paths,
- avoids one tenant or date becoming a hot partition,
- has a migration and rebalancing story.

Tenant ID gives isolation and common query locality, but one giant tenant can be
hot. Time gives retention locality, but the newest partition can receive every
write. Composite and hierarchical strategies can help.

New costs include cross-partition queries, transactions, joins, rebalancing,
operational complexity, and uneven capacity. Do not shard before measurement
shows one well-tuned store is insufficient.

## 4. Queue and Worker

A queue decouples acceptance from completion and buffers a finite burst.

### Required Design

- durable job record and stable ID,
- message that references the job rather than containing every large byte,
- lease or visibility timeout,
- idempotent state transition and output,
- bounded retry with backoff and jitter,
- dead-letter and replay policy,
- cancellation and deadline behavior,
- queue depth and oldest-age monitoring,
- admission control before backlog becomes unbounded.

At-least-once delivery can repeat compute. Conditional finalization and fencing
ensure one accepted result, while monitoring exposes wasted attempts.

## 5. Publish/Subscribe

Publish/subscribe copies one event to independent subscriptions.

```text
order_completed
    -> fulfillment subscription
    -> notification subscription
    -> analytics subscription
    -> audit subscription
```

Each consumer evolves and retries independently. Define event schema, version,
ordering scope, retention, replay, and idempotency.

An event states something that happened. A command asks one owner to do something.
Mixing them makes ownership unclear.

## 6. Transactional Outbox

Problem:

```text
database commit succeeds
event publication fails
```

Writing to a database and remote broker is not one local transaction.

Outbox pattern:

1. In one database transaction, update business state and insert an outbox row.
2. A publisher repeatedly reads unsent outbox rows and publishes them.
3. Mark publication progress idempotently.
4. Consumers deduplicate because publication can repeat.
5. Reconcile old unsent rows and alert.

The pattern prevents silent event loss but adds outbox storage, publisher lag,
duplicate publication, and cleanup.

## 7. Idempotency and Fencing

An idempotent operation has the same logical effect when repeated.

For a client command:

```text
UNIQUE (tenant_id, idempotency_key)
```

Store a request hash so one key cannot mean two payloads.

For background ownership, a lease alone is not enough. A paused old worker may
wake after a new worker owns the job. Use a monotonically increasing attempt or
fencing token; the database and downstream commit reject stale tokens.

Exactly-once physical execution is often impossible across failures. Design for
one durable logical effect and one charge.

## 8. Timeouts, Retries, and Circuit Breakers

### Timeout

Stop waiting when the remaining user or job deadline cannot be met. Use separate
connect and operation timeouts where useful.

### Retry

Retry only errors likely to be temporary and only when the operation is safe.
Use bounded attempts, exponential backoff, jitter, and an overall deadline.

### Circuit Breaker

After enough dependency failures, stop sending normal traffic temporarily. This
protects both systems and gives fast failures. A small probe in half-open state
tests recovery.

A circuit breaker does not fix the dependency. Define fallback, user behavior,
and alert ownership.

## 9. Backpressure, Load Shedding, and Bulkheads

### Backpressure

Signal producers to slow down when consumers are full.

### Load Shedding

Reject lower-priority new work before accepted work and core service collapse.
Return honest retry guidance.

### Bulkhead

Separate resource pools so one tenant, model, endpoint, or dependency cannot use
every thread, connection, worker, or budget.

Combine with per-tenant quotas and weighted fair scheduling.

## 10. Rate Limiting

Rate limiting protects capacity, fairness, security, and budget.

Define:

- identity: IP, user, tenant, API key, endpoint, or combination,
- rate and burst,
- global versus regional scope,
- fail-open versus fail-closed behavior,
- response headers and retry time,
- exemptions and administrative safety.

See [Design a Distributed Rate Limiter](./rate_limiter.md).

## 11. Cursor Pagination

Offset pagination such as `offset=10000` is simple but can scan or skip many rows
and can duplicate or miss items when inserts happen between requests.

Cursor pagination uses the last stable sort key:

```text
ORDER BY created_at DESC, id DESC
WHERE (created_at, id) < (:cursor_time, :cursor_id)
LIMIT 50
```

The cursor should be opaque, signed if callers must not alter it, and tied to the
filter and sort contract. Choose a deterministic unique tie-breaker.

## 12. State Machines and Compensation

For a multi-step workflow, persist allowed states:

```text
PENDING -> RESERVED -> PROCESSING -> COMPLETED
             |             |
             v             v
          CANCELED       FAILED
```

Each transition checks current state and operation identity.

When one distributed transaction is unavailable, compensation may undo or offset
completed steps. A refund compensates a settled charge; it does not erase the
ledger event. Compensation can fail too, so persist and retry it.

## 13. Consistency During Network Partitions

In a distributed system, network partitions can prevent nodes from communicating.
For an operation affected by a partition, decide whether to:

- reject or delay to preserve a single consistent decision, or
- serve an available but potentially stale or conflicting result and reconcile.

Examples:

- Payment settlement and unique username claims usually favor consistency.
- A public feed or cached product description may favor availability with
  eventual convergence.

The choice is per operation and business consequence, not one permanent label
for an entire company.

## 14. Observability and Reconciliation

Patterns create new hidden states. Observe them:

- cache hit, miss, age, eviction, and stampede,
- replica lag,
- partition size and hot-key load,
- queue depth, age, retries, leases, and dead letters,
- outbox lag and duplicate rejection,
- circuit state and fallback use,
- rate-limit decisions,
- state transition failures,
- reconciliation findings.

A reconciler compares desired durable state with external reality and repairs or
alerts. It is essential for workflows spanning database, object storage, broker,
billing, or third-party APIs.

## Pattern Selection Order

1. State the user operation and SLO.
2. Identify the source of truth and correctness invariant.
3. Estimate reads, writes, bytes, service time, and peak.
4. Draw the simplest single-node or synchronous design.
5. Locate the measured bottleneck or failure boundary.
6. Add one pattern that addresses it.
7. State the pattern's new failure and operating cost.
8. Add tests, metrics, and ownership.

This creates a reasoned architecture instead of a box collection.

## Common Pattern Mistakes

- Cache with no invalidation or source of truth.
- Queue with no idempotency, dead-letter, or admission limit.
- Retry with no timeout, jitter, or total deadline.
- Shard with no access pattern or rebalancing plan.
- Replica reads used for operations requiring immediate consistency.
- Rate limit only by IP behind shared enterprise networks.
- Cursor without a stable unique sort.
- Circuit breaker with an unsafe or untested fallback.
- Multi-region claim with a single regional dependency.
- Compensation described as guaranteed instant rollback.

## Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| When should I add a cache? | After finding expensive repeated reads and defining freshness, source, invalidation, and cold-cache behavior. |
| Does a queue guarantee no work is lost? | Only with durable acceptance, producer handoff, correct acknowledgement, retention, monitoring, and recovery design. |
| Can idempotency stop duplicate compute? | It prevents duplicate logical effects; a failure or partition can still waste physical work before fencing. |
| When should I shard? | After indexing, query design, vertical scale, replicas, and measured load no longer satisfy the SLO. |
| Is eventual consistency bad? | It is appropriate when stale reads have acceptable consequences and convergence is defined. |

## Check Your Understanding

### Question 1: Pick the Missing Patterns

An API stores an order, publishes `order_created`, and returns. Sometimes the
database commit succeeds but no event appears. Retrying the API sometimes creates
two orders. Which patterns address both failures?

<details>
<summary>Show answer and explanation</summary>

Use a tenant-scoped idempotency key with a request hash and unique constraint so
client retries return one logical order. In the same database transaction that
creates the order, insert a transactional outbox row. A publisher retries the
outbox event until the broker accepts it, and consumers deduplicate the stable
event ID.

The API should return success only after the local transaction is durable. The
outbox prevents the database/event gap; idempotency prevents the retry/order gap.

</details>

### Question 2: Protect a Slow Dependency

A recommendation service calls a personalization dependency. The dependency
becomes slow and ties up every request thread. Design the protective behavior.

<details>
<summary>Show answer and detailed explanation</summary>

1. Give the dependency a timeout shorter than the remaining request deadline.
2. Retry only safe transient failures with a small bounded budget and jitter;
   do not retry latency timeouts repeatedly inside one request.
3. Use a circuit breaker to stop normal calls during sustained failure.
4. Isolate personalization in a connection/thread bulkhead so it cannot consume
   all recommendation capacity.
5. Serve an evaluated non-personalized fallback or fail clearly if no fallback
   is safe.
6. Shed optional low-priority traffic if core capacity is threatened.
7. Monitor dependency latency, timeouts, circuit state, fallback rate, overall
   recommendation success, and user outcome.
8. Probe recovery gradually before closing the circuit.

The fallback must obey current policy and be tested. Fast wrong output is not
resilience.

</details>
