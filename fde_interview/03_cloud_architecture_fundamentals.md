# Cloud Architecture Fundamentals

[FDE track](./README.md) | [Customer solutioning](./02_customer_discovery_and_solutioning.md) | [System design](../system_design/README.md) | [AI engineering](../ai_engineering/README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Learn Categories Before Product Names

Cloud providers give similar building blocks different names. In an interview,
first explain the requirement and category:

```text
"I need durable buffering because uploads arrive faster than processing. I will
use a managed queue with at-least-once delivery, a dead-letter path, and
idempotent consumers. In your preferred cloud, I would map that category to the
approved managed service."
```

This answer survives product renaming and shows why the component exists.

Before a provider-specific interview, map every category in this guide to that
provider using its current official documentation.

## The Cloud Mental Map

```text
users and external systems
          |
          v
edge, DNS, firewall, load balancing
          |
          v
compute and application services
          |
    +-----+------+----------------+
    |            |                |
    v            v                v
data stores   messages/events   object files
    |            |                |
    +------------+----------------+
                 |
                 v
identity, encryption, observability, policy, cost controls
```

Security and operations surround every layer. They are not boxes added after the
happy path.

## 1. Compute Choices

| Compute Form | Good Fit | Tradeoff |
| --- | --- | --- |
| Virtual machine | Full operating-system control, legacy software, unusual networking or hardware | Most patching, scaling, and host management |
| Managed container | Packaged service with controlled runtime and portable dependencies | Still requires image, resource, rollout, and service design |
| Serverless request service | Stateless HTTP or event work with variable traffic | Runtime limits, cold starts, less host control, and provider constraints |
| Orchestrated containers | Many services, custom scheduling, long-lived workers, specialized networking | Powerful but operationally complex |
| Batch job | Finite background work that values throughput over immediate response | Queue time and job orchestration; not an interactive endpoint |
| Managed function | Small event handler or glue logic | Easy to fragment architecture; duration and package limits |

Ask:

- Is work request-driven, event-driven, scheduled, or continuous?
- Is it stateless?
- How long does it run?
- What latency, concurrency, memory, accelerator, and network access does it need?
- Does the team need host control enough to own the operations it creates?

Choose the least operationally complex form that satisfies the hard constraints.

## 2. Data and Storage Choices

| Data Need | Typical Category | Important Questions |
| --- | --- | --- |
| Transactions and relationships | Relational database | Schema, indexes, isolation, joins, write rate, replicas |
| Key lookup at large scale | Key-value or document store | Partition key, access patterns, consistency, hot keys |
| Large files and immutable blobs | Object storage | Object key, lifecycle, encryption, signed access, versioning |
| Repeated low-latency reads | Cache | Source of truth, TTL, invalidation, eviction, stampede |
| Analytical scans and aggregation | Data warehouse or lakehouse | Partitioning, file format, freshness, scan cost, governance |
| Ordered event history | Log or stream | Retention, partitions, ordering scope, replay, consumer offsets |
| Similarity retrieval | Vector index | Embedding version, metadata filters, recall, freshness, tenancy |

Start from access patterns:

```text
What will be written?
How is it read?
How fresh must it be?
What consistency is required?
How large and how fast will it grow?
Who may access or delete it?
```

Do not put images in relational rows because "we already have a database." Do
not add a distributed database when one managed relational instance meets the
measured workload.

## 3. Queue, Publish/Subscribe, and Stream

These categories are related but solve different communication needs.

| Category | Mental Model | Good Fit |
| --- | --- | --- |
| Work queue | One waiting line; one consumer completes each item | Background jobs, retries, smoothing bursts |
| Publish/subscribe | One event is copied to independent subscriptions | Notifications, analytics, audit, fan-out |
| Durable stream | Ordered partitioned event log consumers can replay | High-volume events, state reconstruction, multiple speeds |

### Delivery Reality

Assume a message can arrive more than once unless the selected service and end
to end design prove otherwise.

An idempotent consumer needs:

- stable event or operation ID,
- atomic or conditional state change,
- safe output naming,
- bounded retries with backoff and jitter,
- dead-letter and replay process,
- metrics for duplicate, old, and poisoned messages.

Acknowledging after a database commit avoids losing work, but a crash between
commit and acknowledgement can cause redelivery. Design for it.

## 4. Networking and Delivery

| Component | Plain-English Job |
| --- | --- |
| DNS | Maps a name to the current service entry point. |
| CDN | Caches approved content near users and reduces origin load. |
| Web application firewall | Blocks known malicious web traffic patterns and enforces coarse rules. |
| Load balancer | Distributes requests across healthy service instances. |
| API gateway | Applies authentication integration, quotas, request policy, and routing. |
| Private network | Limits direct exposure and controls service-to-service paths. |
| Egress control | Restricts and observes outbound connections from workloads. |
| Service discovery | Lets one service find healthy instances of another. |

For every arrow on a diagram, ask:

1. Who initiates this connection?
2. How is each side authenticated?
3. Is traffic public or private?
4. Is it encrypted?
5. What timeout and retry apply?
6. What happens when the destination is slow or unavailable?

## 5. Identity, Authorization, and Secrets

Authentication answers "who are you?" Authorization answers "may you do this?"

Separate:

- human identities,
- customer or tenant identities,
- workload identities for services,
- temporary delegated access such as signed URLs,
- secrets such as external API credentials.

Use least privilege. A processor that reads one input bucket and writes one
output prefix should not be an account administrator.

Prefer short-lived workload credentials over long-lived keys. Store secrets in a
managed secret system, rotate them, audit access, and keep them out of source
code, images, logs, and error messages.

## 6. Availability and Recovery

### Failure Boundaries

- **Instance:** one process or machine fails.
- **Zone:** one local data-center failure domain fails.
- **Region:** a broad geographic cloud region fails.
- **Provider or dependency:** a shared control plane or external vendor fails.

Do not claim multi-region unless data replication, routing, queues, identity,
secrets, deployment, and operations all support it.

### Four Useful Terms

| Term | Meaning |
| --- | --- |
| Availability target | How often the service should accept and serve work |
| RTO | Maximum desired time to restore service after disaster |
| RPO | Maximum tolerable amount of recent data loss measured in time |
| Error budget | Allowed unreliability implied by the service objective |

A system needing near-zero RPO may require synchronous or durable cross-boundary
writes, which increase cost and latency. State the tradeoff.

### Reliability Patterns

- Health checks and replacement
- Redundant stateless instances across zones
- Timeouts before retries
- Exponential backoff with jitter
- Circuit breakers and bulkheads
- Durable queues and idempotent consumers
- Database backups plus tested restore
- Load shedding and admission control
- Graceful degradation
- Reconciliation jobs for incomplete workflows

Retries without limits or idempotency make incidents worse.

## 7. Observability

Three basic signals answer different questions:

| Signal | Answers |
| --- | --- |
| Metrics | Is a measured behavior changing across many requests? |
| Logs | What discrete event or error occurred? |
| Traces | Where did one request spend time across services? |

Add business and workflow state as well:

- accepted, queued, running, succeeded, failed, and abandoned jobs,
- oldest queue age,
- user-visible success,
- safety and authorization decisions,
- cost per completed or useful outcome.

Carry request, tenant, job, model, and deployment version identifiers. Avoid raw
secrets, personal data, prompts, and document contents in ordinary logs.

## 8. Cost and Capacity

Estimate before selecting size:

```text
average requests/second = daily requests / 86,400
peak requests/second = average * peak factor
concurrent work = arrival rate * average service time
storage growth = objects/day * bytes/object * retention days
```

Cost categories include:

- always-on compute,
- per-request or per-second compute,
- accelerator time,
- database capacity and replicas,
- stored bytes and operations,
- network egress,
- log and trace volume,
- cross-region replication,
- engineering and on-call burden.

Set budgets and quotas by tenant or workload. Alert on unit-cost regressions, not
only the monthly total after it is too late.

## 9. Example: Event-Driven Document Processing

### Requirements

- Customers upload documents.
- Processing can take two minutes.
- Bursts may reach 20 times normal traffic.
- Each tenant's data is private.
- Users can reconnect and inspect status.
- Failed processing can retry without duplicate output or billing.

### Architecture

```text
client
  -> authenticated upload request
  -> short-lived object-storage upload URL
  -> private input object
  -> object-created event
  -> durable queue
  -> fair scheduler
  -> stateless processing worker
  -> private output object
  -> conditional job completion
  -> status event and authorized download URL
```

### Durable Records

- Tenant and user
- Job and allowed state transition
- Input object and checksum
- Attempt and lease
- Output object and version
- Idempotency record
- Billing event key
- Audit and deletion state

### Why These Choices

- Direct upload keeps large bytes out of the application server.
- A queue separates fast acceptance from slow processing and absorbs bursts.
- A lease and conditional completion fence duplicate workers.
- Object storage fits large files; a database fits searchable metadata.
- Tenant-derived authorization and short-lived URLs protect objects.
- Durable status lets users leave and return.

### Failure Test

If a worker uploads output and crashes before completion, the object remains
private under a temporary key. The message returns after lease expiry. A retry or
reconciler checks the job and object checksum, then safely finalizes one output.
The billing event key prevents a second settlement.

This is the same long-running-work pattern used by the
[image-generation design](../system_design/image_generation_platform.md), applied
to a different data plane.

## 10. Choosing With Constraints

| Constraint | Likely Direction | Still Ask |
| --- | --- | --- |
| Millisecond online lookup | Cache or serving database close to compute | Consistency, miss behavior, hot keys |
| Minutes-long processing | Queue and background workers | Progress, cancellation, retry, deadline |
| Large immutable files | Object storage and signed access | Retention, encryption, delivery, deletion |
| Strict transactions | Relational or transactional store | Scale, isolation level, schema evolution |
| Independent event consumers | Publish/subscribe or stream | Ordering, replay, duplicate handling |
| Spiky stateless HTTP | Autoscaled container or serverless request compute | cold start, maximum duration, connection needs |
| Data residency | Region-pinned data and processing | backup, logs, support, disaster recovery |
| Small operations team | More managed components and fewer platforms | lock-in, limits, cost visibility |

"Likely" is intentional. A constraint narrows choices but rarely determines an
entire architecture by itself.

## Assumptions to Say Aloud

- Expected average and peak workload
- Synchronous versus background experience
- Data sensitivity, residency, retention, and deletion
- Availability, RTO, and RPO
- Ordering and consistency needs
- Existing provider, skills, contracts, and network
- Who operates the system
- Budget and expected growth

## Edge Cases and Failure Questions

- What happens when a region cannot reach the identity provider?
- Can a repeated event create another customer-visible side effect?
- What if a queue grows faster than autoscaling can react?
- What if cache data is stale or the cache is empty after restart?
- What if the database write succeeds but event publication fails?
- Can tenant A infer tenant B's IDs, volume, or files?
- What if a secret rotates while instances are running?
- Can backups actually restore within the RTO?
- What if observability cost exceeds application compute cost?
- What happens when an external API is slow for six hours?

## Common Mistakes

- Naming a provider product without explaining its category and requirement.
- Drawing every managed service instead of one understandable request flow.
- Choosing serverless only because traffic is low, ignoring job duration or runtime needs.
- Treating a cache as the source of truth without a recovery plan.
- Saying a queue provides exactly-once end-to-end behavior.
- Adding retries before timeouts and idempotency.
- Claiming multi-region while leaving one regional database or secret dependency.
- Ignoring IAM, data deletion, observability, and ownership.
- Optimizing infrastructure cost while creating excessive operating complexity.

## Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| When would you choose a VM? | When host control, legacy runtime, special networking, or hardware matters enough to own patching and scaling. |
| Queue or pub/sub? | Queue for one worker completing each job; pub/sub when independent consumers each need the event. |
| SQL or key-value? | Start with transactions and access patterns; neither label is universally more scalable or correct. |
| When should you cache? | After measuring expensive repeated reads and defining source of truth, freshness, invalidation, and miss behavior. |
| How do you avoid provider lock-in? | Preserve business interfaces and portable data where valuable; accept managed-service coupling when its benefit exceeds migration risk. |

## Cloud Design Scorecard

- [ ] Every component has a requirement-based reason.
- [ ] Compute form matches duration, state, traffic, and team operations.
- [ ] Data stores match access, consistency, growth, and retention.
- [ ] Async delivery assumptions and idempotency are explicit.
- [ ] Every network arrow has identity, encryption, timeout, and failure behavior.
- [ ] Tenant and human authorization are enforced at each resource.
- [ ] Availability, backup, RTO, and RPO claims are internally consistent.
- [ ] Metrics, logs, traces, alerts, and ownership cover the workflow.
- [ ] Capacity and unit-cost arithmetic are stated.
- [ ] The design can be mapped to the target provider from current official docs.

## Check Your Understanding

### Question 1: Queue or Publish/Subscribe?

An uploaded image needs thumbnail generation, malware scanning, analytics, and an
audit record. Should all four services compete on one queue?

<details>
<summary>Show answer and explanation</summary>

No. Each independent responsibility needs to observe the upload event. Publish
the event to separate durable subscriptions, one for each consumer group. Within
the thumbnail subscription, several worker instances may compete so one worker
handles each thumbnail task.

This combines fan-out between responsibilities with work sharing inside one
responsibility. Every consumer still needs idempotency because an event may be
redelivered.

</details>

### Question 2: Choose Compute for a Nightly Export

A report reads a large warehouse table, writes one file, takes 45 minutes, and
runs once each night. Users never wait interactively. Which compute form fits?

<details>
<summary>Show answer and detailed explanation</summary>

A scheduled batch job is the natural starting point. It runs finite work, values
throughput over request latency, and should release resources after completion.

The design should also define:

- a scheduler and unique run ID,
- input snapshot or partition so reruns are reproducible,
- checkpoint or safe restart behavior,
- deterministic output key or version,
- timeout, retry limit, and alert,
- data permissions and encryption,
- success record and late-data policy,
- cost and duration metrics.

A permanently running web server adds idle cost and does not improve the workflow.
A short-duration function may be inappropriate if its runtime and resource limits
cannot support a 45-minute scan.

</details>
