# Design an Image-Generation Platform

[System design guide](./README.md) | [Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## The Question

Design a platform where a user enters a text prompt, receives several candidate
images, refines a selected result, and downloads or shares the final asset.

A prototype can call one image model and return its response. A production
system must also handle slow inference, unsafe requests and outputs, retries,
billing, enterprise isolation, storage, model changes, traffic spikes, quality
measurement, and cost.

This guide builds the design one decision at a time. The numbers are interview
assumptions, not facts about a particular company.

## What the Interviewer Is Testing

The interviewer is not testing whether you know a secret architecture. They
want to see whether you can:

- turn an open-ended prompt into clear requirements,
- make and revise reasonable assumptions,
- separate quick API work from slow model work,
- protect users, customer data, and money,
- reason about scale and failure,
- compare alternatives and explain tradeoffs,
- define how the team knows the system is useful and healthy.

## How to Study This Guide

Do not try to memorize all sections in one sitting.

| Pass | Read | Goal |
| ---: | --- | --- |
| 1 | Sections 1-7 and the two-minute summary | Understand the customer, requirements, estimates, API, data, architecture, and normal flow. |
| 2 | Sections 8-15 | Learn the major production deep dives. |
| 3 | Sections 16-24 | Learn operations, failures, security, cost, tests, and tradeoffs. |
| 4 | Follow-ups, transfer questions, and scorecard | Practice adapting the design without notes. |

After each pass, draw only what you remember and explain why each box exists.
Missing a box is useful feedback; it shows exactly what to review.

## A 45-Minute Interview Plan

| Time | Work |
| ---: | --- |
| 0-5 minutes | Clarify the customer, outcome, features, and boundaries. |
| 5-10 minutes | State scale, latency, availability, safety, and retention assumptions. |
| 10-15 minutes | Define APIs, core data, and the job state machine. |
| 15-25 minutes | Draw the high-level architecture and walk through one request. |
| 25-38 minutes | Deep-dive on asynchronous jobs, idempotency, policy, scheduling, and isolation. |
| 38-43 minutes | Cover failures, observability, model rollout, evaluation, and cost. |
| 43-45 minutes | Summarize tradeoffs and answer follow-ups. |

If the interviewer redirects you, follow them. The schedule is a safety rail,
not a script that matters more than the conversation.

## 1. Clarify the Customer and Outcome

Start with questions, not components.

Useful questions include:

1. Is this for individual creators, professional teams, or both?
2. Is the main goal exploration, or producing a final commercial asset?
3. How many candidates should one request create?
4. Does refinement mean a new prompt, an image mask, an uploaded reference, or all three?
5. Must results appear in real time, or is a saved background job acceptable?
6. Are private enterprise projects, regional storage, and audit logs required?
7. How long should prompts and images be retained?
8. Are users charged per request, per candidate, or by consumed compute?
9. Which safety and legal policies apply to prompts, reference images, and outputs?

### Assumptions for This Design

Say your assumptions aloud so the interviewer can change them.

| Area | Assumption |
| --- | --- |
| Customer | Individual creators and creative teams, including enterprise tenants |
| Outcome | Reach a usable final asset quickly, not merely generate many images |
| Generation | One request asks for four candidates from a text prompt |
| Refinement | A new job can reference a parent image, optional mask, and revised prompt |
| Delivery | Jobs are asynchronous because generation can take about 40 seconds |
| Privacy | Assets are private by default; users explicitly create revocable share links |
| Billing | The system reserves credits at acceptance and settles once for completed work |
| Retention | Hot assets remain for 30 days by default; product and tenant policy may differ |
| Availability | The control-plane API targets 99.9% availability across multiple zones |
| Performance | Submit API p95 below 300 ms; normal completed-job p95 below 60 seconds |

**Say aloud:**

> I will optimize for a creator reaching a usable asset. Generation is slow, so
> the API will create a durable asynchronous job instead of holding one HTTP
> request open for 40 seconds.

### Out of Scope for the First Version

- Training a foundation model from scratch
- Video or 3D generation
- A public social feed and recommendation system
- Real-time multi-user canvas editing
- A marketplace for third-party models
- Full payment-processor internals

Stating what is out of scope protects time for the hard parts that belong to
this question.

## 2. Define Requirements

### Required User Features

1. Sign in and belong to a personal or enterprise tenant.
2. Submit a prompt and generation settings.
3. Receive a job ID immediately.
4. See queued, running, blocked, failed, canceled, and completed states.
5. Receive up to four safe candidate images.
6. Refine a chosen image while preserving its version history.
7. Download an authorized asset.
8. Create, expire, and revoke a share link.
9. View project history and retry an eligible failure.
10. Delete assets according to retention and tenant rules.

### Production Requirements

- Durable job state survives API, worker, and model-server crashes.
- Client and queue retries do not duplicate work or billing.
- Unsafe prompts and unsafe generated images are not delivered.
- One tenant cannot read another tenant's data or monopolize shared capacity.
- Traffic spikes do not crash the control plane or overload the inference fleet.
- Every asset records the model, policy, settings, and parent used to create it.
- Model versions can be evaluated, released gradually, and rolled back.
- Operators can observe latency, queue age, errors, safety, quality, and cost.

### Useful SLOs

| SLO | Example Target | Why It Matters |
| --- | ---: | --- |
| Submit API availability | 99.9% monthly | Users can reliably create or inspect jobs. |
| Submit API latency | p95 under 300 ms | Acceptance should feel immediate. |
| Queue wait in normal load | p95 under 10 seconds | A healthy fleet starts work quickly. |
| End-to-end generation | p95 under 60 seconds | Includes queue, inference, checks, and upload. |
| Durable job loss | 0 acknowledged jobs | An accepted job must remain recoverable. |
| Duplicate charge rate | Effectively zero | Retries must not charge twice. |
| Cross-tenant data access | Zero | Isolation is a correctness and security boundary. |

An SLO is a design target, not a promise that no request will ever fail.

## 3. Estimate Scale Before Choosing Capacity

Use round numbers. The goal is to find the order of magnitude.

Assume:

- `100,000` daily active users,
- `3` generation jobs per active user per day,
- `4` candidates per job,
- `2 MB` average stored size per candidate,
- traffic peaks at `10` times the daily average,
- one inference slot spends about `40` seconds on a four-image job.

### Job Throughput

```text
jobs per day = 100,000 users * 3 jobs
             = 300,000 jobs/day

average jobs/second = 300,000 / 86,400
                    = about 3.5 jobs/second

peak jobs/second = 3.5 * 10
                 = about 35 jobs/second
```

### Concurrent Inference

For a stable system, work must finish as fast as it arrives. A useful estimate
comes from Little's Law:

```text
concurrent inference slots = arrival rate * service time
                           = 35 jobs/second * 40 seconds
                           = 1,400 slots at peak

with 30% headroom = 1,400 * 1.3
                  = about 1,820 slots
```

A slot is a unit of model capacity, not automatically one whole GPU. Benchmarking
may show that one accelerator serves several batched jobs or that one job needs
several accelerators. The estimate tells the infrastructure team what to measure.

### Image Storage

```text
images per day = 300,000 jobs * 4 images
               = 1,200,000 images/day

new bytes per day = 1,200,000 * 2 MB
                  = about 2.4 TB/day

30-day hot storage = 2.4 TB * 30
                   = about 72 TB
```

Replicas, thumbnails, masks, refined versions, and uploaded references add more.
Downloads can also make network egress cost larger than metadata storage cost.

### Why These Estimates Matter

- The control plane sees only tens or hundreds of submissions per second, but
  the inference fleet needs many concurrent slots because each job is slow.
- Images belong in object storage, not inside database rows.
- Retention and deletion policies have a large cost effect.
- Frequent status polling can create more API traffic than submissions, so the
  client should use server events or exponential polling backoff.

## 4. Design the API Contract

The API should expose jobs, not model-server details.

| Method and Path | Purpose |
| --- | --- |
| `POST /v1/generations` | Validate and accept a new generation job |
| `GET /v1/jobs/{job_id}` | Read durable status, progress, errors, and result IDs |
| `GET /v1/jobs/{job_id}/events` | Receive status changes through server-sent events |
| `POST /v1/jobs/{job_id}/cancel` | Request cancellation if work is not terminal |
| `POST /v1/assets/{asset_id}/refinements` | Create a child job from an image, prompt, and optional mask |
| `GET /v1/assets/{asset_id}/download` | Return a short-lived signed download URL |
| `POST /v1/assets/{asset_id}/shares` | Create an expiring, revocable share link |
| `DELETE /v1/assets/{asset_id}` | Schedule deletion under retention policy |

### Submit Request

```http
POST /v1/generations
Authorization: Bearer <token>
Idempotency-Key: 7cb2f45d-...
Content-Type: application/json
```

```json
{
  "project_id": "project_123",
  "prompt": "A clean product photo of a blue ceramic mug",
  "candidate_count": 4,
  "aspect_ratio": "1:1",
  "model_alias": "standard"
}
```

### Immediate Response

```http
HTTP/1.1 202 Accepted
```

```json
{
  "job_id": "job_456",
  "status": "QUEUED",
  "status_url": "/v1/jobs/job_456"
}
```

`202 Accepted` means the service durably accepted the work. It does not claim
that generation already succeeded.

The server derives `tenant_id` and `user_id` from the verified identity token.
It never trusts a caller to choose another tenant in the request body.

### Idempotency Contract

The pair `(tenant_id, idempotency_key)` is unique.

- Repeating the key with the same normalized request returns the original job.
- Reusing the key with a different request returns a conflict error.
- A new key means the user intentionally wants new random candidates, even when
  the prompt text is identical.

This distinction prevents accidental duplicates without destroying the valid
use case of generating fresh results from the same prompt.

## 5. Store Durable State

### Core Records

| Record | Important Fields | Purpose |
| --- | --- | --- |
| `tenants` | `tenant_id`, plan, region, quotas, retention policy | Customer boundary and operating policy |
| `users` | `user_id`, `tenant_id`, role, status | Identity and authorization |
| `projects` | `project_id`, `tenant_id`, owner, permissions | Groups related generation work |
| `jobs` | `job_id`, tenant, request hash, status, model version, policy version, timestamps | Durable source of truth for one request |
| `job_attempts` | job, attempt number, lease owner, heartbeat, error, compute used | Separates retries from the logical job |
| `assets` | asset, tenant, job, candidate index, parent asset, object key, dimensions, safety state | Metadata for generated and uploaded files |
| `idempotency_records` | tenant, key, request hash, job ID, expiry | Maps a client retry to one logical job |
| `billing_ledger` | event key, tenant, job, event type, amount, status | Append-only reservation, settlement, refund, and adjustment events |
| `share_links` | token hash, asset, tenant, expiry, revoked time | Controlled access without exposing object keys |
| `policy_decisions` | job or asset, policy version, decision, reason codes | Auditable input and output checks |
| `model_versions` | immutable version, artifact hash, status, rollout rules | Reproducible routing and safe releases |

Every customer-owned row includes `tenant_id`. Database access methods require
it, and authorization tests verify that omitting or changing it cannot reveal
another tenant's data.

### Job State Machine

```text
RECEIVED
   -> INPUT_REVIEW
       -> BLOCKED
       -> QUEUED
           -> RUNNING
               -> OUTPUT_REVIEW
                   -> SUCCEEDED
                   -> BLOCKED
               -> FAILED
               -> CANCELED
           -> CANCELED
```

Terminal states are `SUCCEEDED`, `FAILED`, `CANCELED`, and `BLOCKED`. A retry is
a new `job_attempt` under the same logical job; it does not invent a second job.

Allowed transitions are enforced with a conditional update such as "change
`QUEUED` to `RUNNING` only if it is still `QUEUED` and I own the lease." This
stops two workers from both finalizing the same job.

## 6. Draw the High-Level Architecture

```text
Web or mobile client
        |
        v
CDN / WAF / API gateway
        |
        +----> Identity provider
        |
        v
Generation API ----> Prompt policy service
        |
        +----> Job database + idempotency + billing ledger
        |                         |
        |                         v
        |                  Transactional outbox
        |                         |
        v                         v
Status events <------------ Durable job queue
                                  |
                                  v
                         Fair scheduler / admission control
                                  |
                                  v
                         Model router and GPU workers
                                  |
                                  v
                         Output policy service
                                  |
                    +-------------+-------------+
                    |                           |
                    v                           v
              Object storage              Job database
                    |
                    v
              CDN / signed URLs
```

### What Each Part Owns

| Component | Responsibility |
| --- | --- |
| API gateway | TLS, request size limits, coarse rate limits, and routing |
| Identity provider | Login, tokens, enterprise single sign-on, and user lifecycle |
| Generation API | Authorization, validation, idempotency, job creation, and status reads |
| Policy services | Versioned decisions for prompts, uploads, and generated candidates |
| Job database | Durable workflow state and metadata |
| Transactional outbox | Reliably publishes accepted database work to the queue |
| Durable queue | Buffers slow work and redelivers messages after worker failure |
| Scheduler | Applies priorities, quotas, fairness, batching, and capacity limits |
| Model router | Resolves a product alias to an immutable model version and compatible fleet |
| GPU workers | Perform expensive generation or refinement inference |
| Object storage | Stores images, thumbnails, masks, and uploaded references |
| CDN | Delivers authorized files close to users |
| Evaluation pipeline | Computes quality signals and joins them with user outcomes |
| Observability stack | Metrics, logs, traces, alerts, dashboards, and audit evidence |

### Control Plane and Data Plane

The **control plane** handles small records: identity, policy decisions, job
status, routing, quotas, and billing. The **data plane** handles expensive model
execution and large image bytes.

Keeping image bytes out of the API database lets those two sides scale and fail
independently.

## 7. Walk Through One Normal Request

1. The gateway authenticates the user and applies a coarse rate limit.
2. The Generation API derives the tenant and checks project permissions.
3. It validates prompt length, settings, candidate count, quota, and budget.
4. The prompt policy service returns a versioned allow or block decision.
5. In one database transaction, the API creates the idempotency record, job,
   initial billing reservation, and outbox event.
6. The API returns `202 Accepted` with the job ID.
7. An outbox publisher sends the event to the durable queue and marks it sent.
8. The scheduler considers service tier, tenant fairness, model, region, queue
   age, and available capacity.
9. A worker acquires a lease, creates a job attempt, and sends heartbeats.
10. The model router records the exact model and configuration used.
11. The inference worker generates candidate images.
12. The output policy service checks every candidate independently.
13. Allowed outputs upload to temporary object keys, then receive committed
    asset rows and final object keys.
14. The job conditionally moves to `SUCCEEDED`, billing settles once, and a
    status event is published.
15. The client receives the event, requests signed thumbnail or download URLs,
    and displays only authorized, policy-approved assets.

For a refinement, the new job also stores `parent_asset_id`, the revised prompt,
and optional mask or reference. The asset history is a graph of immutable
versions; refining does not overwrite the original.

## 8. Deep Dive: Inference Takes 40 Seconds

Holding one HTTP request open for 40 seconds is fragile. Browsers, proxies, and
mobile networks may disconnect, and an API process would own many idle sockets.

Use this asynchronous pattern:

1. Validate and durably create a job quickly.
2. Return `202` and a stable job ID.
3. Buffer the work in a durable queue.
4. Let the client subscribe to server-sent events or poll with backoff.
5. Persist every meaningful state so reconnecting clients can recover.
6. Heartbeat long attempts and reclaim a lease after a worker disappears.
7. Support best-effort cancellation and expose when cancellation is too late.
8. Deliver candidates as a complete set or incrementally, according to the API
   contract, but never expose a candidate before its output check finishes.

An estimated completion time is helpful but must be labeled approximate. It can
come from queue age, jobs ahead, model type, and recent service time. Do not make
the user watch a fake precise countdown.

## 9. Deep Dive: Duplicate Work and Duplicate Billing

There are two different duplicate problems.

### Client Retry

The user submits, the API commits, but the response is lost. The client retries.

Solution:

```text
UNIQUE (tenant_id, idempotency_key)
```

The transaction either creates one job or returns the existing one. Store a
hash of the normalized request so the same key cannot silently mean different
work.

### Queue Redelivery

A worker finishes inference but crashes before acknowledging the message. The
queue sends the message again.

Solution:

- Claim work with a lease and conditional status transition.
- Pass a fencing token or current attempt ID to downstream services so a stale
  worker cannot publish after a newer attempt takes ownership.
- Give every attempt a number and deterministic temporary object prefix.
- Finalize results only if the logical job is still eligible.
- Make completion and billing events unique by logical job and event type.
- Run a reconciler that repairs expired leases and incomplete commits.

Useful database constraints include:

```text
UNIQUE assets (job_id, candidate_index)
UNIQUE billing_ledger (event_key)
UNIQUE job_attempts (job_id, attempt_number)
```

For example, a settlement command always uses `settle:<job_id>` as its event
key. A later manual adjustment uses a different key tied to its support or audit
record, so it remains append-only without allowing the settlement to repeat.

A lease and fencing token guarantee one accepted result, not magical exactly-once
physical execution. If a worker loses network access but keeps computing, a new
worker may temporarily repeat that compute after the lease expires. The design
limits this window and prevents the stale attempt from publishing or charging.

### Billing Lifecycle

1. Reserve the estimated credits once when the job is accepted.
2. Settle actual usage once after an eligible completion.
3. Release or refund the reservation for a system failure or cancellation under
   product policy.
4. Record adjustments as new ledger entries instead of rewriting history.

The billing ledger is append-only and idempotent. A message retry may repeat a
settlement command, but the unique event key prevents a second charge.

Do **not** globally deduplicate matching prompt text. Generative outputs are
expected to vary, and cross-tenant caching can leak private intent. An explicit
"reuse this result" operation may reuse an existing asset inside the same tenant.

## 10. Deep Dive: Safety and Policy Enforcement

Policy is a pipeline, not one prompt filter.

### Example Decision Matrix

The exact matrix belongs to safety, legal, and product owners. The architecture
must support versioned decisions such as these:

| Decision | Example Category | System Action |
| --- | --- | --- |
| Hard block | Illegal sexual exploitation, any sexual content involving minors, non-consensual intimate imagery, or a credible request for fraudulent impersonation | Reject the input or quarantine the output, reveal no asset, record a safe reason code, and trigger required abuse handling. |
| Restrict or review | Ambiguous high-risk identity use, sensitive graphic content, or a case whose legality depends on region and context | Require more context, apply age or enterprise controls, or send to trained review according to policy. |
| Allow with disclosure | Synthetic media that is permitted but requires provenance or labeling | Deliver only after adding required metadata or visible disclosure. |
| Allow | Benign creative, educational, product, and editing requests within account policy | Continue through normal generation and output checks. |

Low classifier confidence is not automatically permission. High-risk uncertain
cases should wait for review or fail closed according to the product policy.

### Before Inference

- Authenticate the user and tenant.
- Apply account, region, age, and contractual restrictions.
- Validate prompt and uploaded reference size and type.
- Scan uploads and remove untrusted metadata.
- Evaluate the prompt and references with a versioned policy service.
- Rate-limit abusive patterns and repeated blocked attempts.

### After Inference

- Evaluate each output independently before it becomes readable.
- Block or quarantine disallowed images.
- Record policy version and reason codes without exposing sensitive classifier
  details that would make evasion easier.
- Optionally generate a replacement up to a small retry limit when only one
  candidate fails, then stop to control cost.
- Apply required provenance or watermark metadata before delivery.

The policy matrix is owned with legal, safety, and product teams and can vary by
region and customer contract. Typical blocked categories include illegal sexual
exploitation, non-consensual intimate imagery, credible fraudulent impersonation,
and other content forbidden by product policy or law. Some categories may be
allowed only with restrictions, review, or clear labeling.

If all candidates are blocked, return a safe reason category and do not expose
the images. Billing behavior must be explicit; a reasonable default is not to
charge for unusable system-generated output.

For a high-risk check, an unavailable policy service should fail closed or leave
the job pending for review. It should not silently treat "no answer" as "safe."

## 11. Deep Dive: Enterprise Tenant Isolation

Isolation must exist at every layer.

| Layer | Isolation Control |
| --- | --- |
| Identity | Tenant comes from verified claims; enterprise roles use least privilege. |
| API | Every resource lookup requires both resource ID and authorized tenant ID. |
| Database | Tenant partition keys and row-level policies prevent cross-tenant reads. |
| Object storage | Private buckets, tenant-prefixed keys, scoped service roles, and short-lived signed URLs. |
| Queue and scheduler | Per-tenant quotas, concurrency limits, and weighted fairness prevent noisy neighbors. |
| Encryption | Encryption at rest; high-assurance tiers may use separate tenant keys. |
| Models | Customer prompts and outputs are excluded from training unless the contract and explicit choice allow it. |
| Network | Private service networking; stronger tiers may use dedicated accounts, clusters, or inference pools. |
| Operations | Tenant-scoped audit logs, retention, deletion, region pinning, and support access controls. |

A shared database with strong tenant keys is simpler and cheaper for most
customers. Dedicated infrastructure offers stronger isolation but costs more and
is harder to operate. Present it as a premium option, not the default answer for
every tenant.

Test isolation with automated negative tests: a token from tenant A must fail to
read, refine, share, cancel, or download every resource belonging to tenant B.

## 12. Scheduling, Traffic Spikes, and Backpressure

The scheduler should dispatch only work the inference fleet can actually run.

### Scheduling Inputs

- service tier and reserved enterprise capacity,
- job age so old work cannot starve,
- per-tenant concurrency and daily quota,
- model version, resolution, and region,
- cancellation and deadline state,
- available memory and compatible accelerator type.

Weighted fair queues let paid tiers receive promised service while still giving
each active tenant progress. A single large customer cannot fill every worker.

### During a Spike

1. Keep accepted work in a durable queue.
2. Autoscale from queue age, arrival rate, and accelerator utilization, not CPU
   alone.
3. Keep popular model versions warm to avoid repeated loading delays.
4. Dynamically batch compatible requests when throughput gain is worth the
   extra wait.
5. Enforce quotas and return `429 Too Many Requests` with `Retry-After` before
   the queue grows without limit.
6. Pause low-priority batch work before interactive enterprise work.
7. Offer a lower-cost preview model or fewer candidates only with explicit user
   choice; never silently change quality or billing.

Autoscaling GPUs can take minutes, so headroom, warm pools, admission control,
and honest queue status matter even when autoscaling exists.

## 13. Storage, Refinement, Download, and Sharing

Store metadata in the database and bytes in object storage.

### Asset Lifecycle

```text
temporary upload -> safety approved -> committed private asset
                  -> thumbnail and download derivatives
                  -> refined child versions
                  -> archive or deletion by lifecycle policy
```

- Use random, non-guessable object keys that include a tenant partition.
- Keep buckets private; application authorization creates short-lived signed URLs.
- Put a CDN in front of approved assets for efficient download.
- Save immutable originals and create new asset rows for refinements.
- Store the parent asset, prompt revision, mask, seed, model version, and policy
  version needed to understand lineage.
- Hash share tokens in the database, allow expiry and revocation, and optionally
  restrict enterprise links to a domain or authenticated users.
- Delete database metadata and object derivatives through a durable deletion
  workflow, with audit evidence and retries.

If an object upload succeeds but the database commit fails, the object remains
temporary and invisible. A sweeper deletes stale temporary objects later. This
is safer than publishing an object before the durable asset record exists.

## 14. Model Versions and Safe Rollout

`standard` is a product alias. Each accepted job resolves that alias to an
immutable model version and records it.

A release process should:

1. Register the model artifact, configuration, compatible hardware, and checksum.
2. Run offline quality, safety, latency, and cost evaluations on versioned sets.
3. Shadow a small amount of eligible traffic without showing results to users.
4. Canary the version to a small percentage of real jobs.
5. Compare usefulness, safety, latency, errors, and cost against the current model.
6. Increase traffic gradually only while guardrails remain healthy.
7. Roll back the alias quickly while preserving jobs already pinned to a version.

Enterprise tenants may need a pinned version and advance notice before migration.
Record prompt, seed, sampler, configuration, and hardware details where practical,
but do not promise pixel-identical reproduction across every model and hardware
change.

## 15. Measure Whether an Image Is Useful

Generation count is not the goal. A product can generate more images while
helping users less.

### Product Funnel

```text
job completed
    -> candidate viewed
    -> candidate selected
    -> refined or edited
    -> downloaded or shared
    -> used again in a project
```

### Metric Groups

| Group | Examples |
| --- | --- |
| User outcome | Time to first usable asset, selection rate, download/share rate, successful refinement rate |
| Explicit feedback | Thumbs up/down, reason labels, quality survey, enterprise review sample |
| Model quality | Prompt-image alignment, visual artifacts, text rendering, diversity among candidates |
| Safety | Prompt block rate, output block rate, appeal overturn rate, unsafe escape rate from reviewed samples |
| Reliability | Submit success, queue age, completion rate, retry rate, cancellation, orphaned job count |
| Performance | API latency, queue wait, inference time, policy time, upload and delivery latency |
| Cost | Accelerator seconds per completed job, cost per selected asset, storage, egress, wasted retry compute |

A useful north-star metric is **median time to first selected or downloaded
asset**, with safety, reliability, latency, and cost as guardrails.

Behavioral signals are imperfect. A download may not mean the image was good,
and an image may be useful without a download. Combine opt-in user feedback,
funnel behavior, expert human review, and versioned offline evaluation. Respect
enterprise privacy choices when collecting evaluation data.

## 16. Observability and Operating Controls

Every request should carry `request_id`, `job_id`, `tenant_id`, `attempt_id`,
`model_version`, and `policy_version` through logs, metrics, and traces. Avoid
putting raw prompts or image contents into normal logs.

### Dashboards

- API request rate, errors, and p50/p95/p99 latency
- Queue depth and oldest-job age by tier, region, and model
- Active leases, expired leases, attempts, and dead-letter jobs
- Accelerator utilization, memory, batch size, inference latency, and failures
- Policy latency and allow/block/error rates by policy version
- Upload failures, storage growth, CDN hit rate, and egress
- Reservations, settlements, refunds, and duplicate-event rejections
- User outcome and model evaluation metrics by version

### Alerts and Controls

- Alert on SLO error-budget burn, not every isolated error.
- Page on rapidly growing queue age, cross-tenant authorization signals,
  duplicate billing, lost-job reconciliation failures, or unsafe-output escapes.
- Provide controls to pause a model, region, tenant, job type, or rollout.
- Keep runbooks for stuck queues, policy outages, model regression, storage
  errors, and billing reconciliation.
- Use kill switches that preserve durable state and explain user-visible impact.

## 17. Failure Modes and Recovery

| Failure | Expected Behavior |
| --- | --- |
| Client repeats submit | Return the original job for the same idempotency key and payload. |
| API commits but cannot publish | Transactional outbox retries publishing without losing the job. |
| Queue delivers twice | Lease and conditional updates allow only one valid finalization. |
| Worker crashes during inference | Lease expires; retry if policy and attempt limit allow it. |
| Model times out | Mark the attempt failed, retry with bounded backoff, then fail the logical job clearly. |
| Policy service is unavailable | Keep high-risk work pending or fail closed; do not expose unchecked output. |
| One of four outputs is blocked | Hide it and optionally replace it within a bounded cost policy. |
| All outputs are blocked | End as `BLOCKED`, reveal no images, and apply the documented billing rule. |
| Object upload succeeds, DB commit fails | Leave the temporary object private; reconciler deletes or safely finalizes it. |
| Status event is missed | Client reads current durable status; events are a convenience, not the source of truth. |
| Cancellation races with completion | Conditional transition decides one terminal state; billing follows that state. |
| Traffic exceeds maximum capacity | Enforce admission limits, preserve accepted jobs, and return honest retry guidance. |
| One region fails | Route control-plane traffic to a healthy region and recover queued work according to data residency rules. |
| Billing dependency is down | Preserve the job and reservation intent; reconcile before settlement instead of guessing. |
| Share link is revoked | New authorization fails immediately; an already issued signed URL works until its short expiry unless the CDN supports active invalidation. |

Use bounded retries with exponential backoff and jitter. Unlimited retries can
turn one dependency failure into a traffic storm and repeated compute cost.

## 18. Security and Privacy Checklist

- Use standards-based login, short-lived access tokens, and enterprise SSO where required.
- Apply role-based authorization to projects, assets, sharing, billing, and administration.
- Validate image dimensions, file signatures, and decompression limits for uploads.
- Prefer direct presigned uploads over fetching arbitrary user URLs; if URLs are
  supported, defend against server-side request forgery.
- Encrypt network traffic and stored data; rotate secrets and encryption keys.
- Keep object storage private and signed URLs short-lived.
- Log administrative and support access to enterprise data.
- Support retention, legal hold, export, and deletion workflows by tenant policy.
- Minimize prompt and image data in logs, metrics, support tools, and evaluation sets.
- Threat-model share links, model supply chain, malicious files, quota abuse, and insider access.

## 19. Cost Controls

The dominant cost is usually expensive inference, followed by image storage and
delivery. Track cost per **useful** result, not only cost per request.

```text
job compute cost
    = accelerator seconds
    * accelerator price per second
    * number of required accelerators

total unit cost
    = compute + policy checks + storage + network egress + support overhead
```

Useful controls include:

- show an estimated credit cost before acceptance,
- reserve tenant budget before scheduling,
- enforce per-user and per-tenant quotas,
- use a cheap preview model before an optional high-resolution pass,
- batch only compatible jobs when latency permits,
- cap safety replacements and infrastructure retries,
- move old assets to cheaper storage or delete them by policy,
- deduplicate thumbnails and derivatives inside one authorized asset lineage,
- route models by quality, latency, region, and budget,
- measure accelerator seconds per selected or downloaded asset,
- stop a rollout when quality falls or cost rises beyond a guardrail.

Do not save money by silently using a lower-quality model than the API promised.

## 20. Correctness Invariants

An invariant is a rule that must remain true after every operation.

1. One `(tenant_id, idempotency_key)` identifies at most one logical request.
2. A job follows only allowed state transitions and has one terminal outcome.
3. A worker without a valid lease cannot finalize a job.
4. No asset becomes readable before authorization and output policy approval.
5. Every customer resource is owned and queried through exactly one tenant.
6. Every billable event settles at most once for a logical job.
7. Every delivered asset records its model, policy, job, and lineage metadata.
8. Deleting or revoking access eventually removes every supported delivery path.

These rules are more useful than memorizing individual service names. They tell
you what database constraints, transactions, and tests the design needs.

## 21. Complexity and Capacity in Plain Language

System design rarely has one Big-O answer, but operation costs still matter.

Let:

- `J` be queued jobs,
- `A` be stored assets,
- `S` be average asset bytes,
- `K` be assets shown on one history page,
- `lambda` be arriving jobs per second,
- `T` be average inference seconds per job.

| Operation or Resource | Cost |
| --- | --- |
| Submit a job | `O(1)` expected metadata writes; it does not wait for inference |
| Read one job | `O(1)` indexed lookup by tenant and job ID |
| List one history page | `O(K)` returned records using a tenant/time index and cursor |
| Priority scheduling | Often `O(log J)` per heap operation, or near `O(1)` with bucketed queues |
| Stored image bytes | `O(A * S)` |
| Required concurrent inference | Approximately `lambda * T` |
| End-to-end latency | Queue wait + inference + output review + upload |

The dominant bottleneck is accelerator time, not the constant-time job lookup.
That is why queues, admission control, batching, and model efficiency receive
more attention than micro-optimizing the submit endpoint.

## 22. Edge Cases to Say Aloud

- Empty, whitespace-only, or extremely long prompt
- Unsupported dimensions, candidate count, file type, or mask shape
- Idempotency key reused with a different payload
- Same prompt intentionally submitted with a new key
- User leaves and reconnects while the job is running
- User cancels exactly as the worker completes
- Tenant quota or credit becomes exhausted between acceptance and scheduling
- One candidate succeeds while another inference or policy check fails
- Every generated candidate is blocked
- Worker heartbeat stops after compute has already been spent
- Model version is paused after a job is accepted
- Parent asset is deleted while a refinement is queued
- Signed URL expires during a large download
- Share link is revoked while a CDN copy exists
- Enterprise tenant changes region or retention policy
- User requests deletion while backup retention still applies

Naming these cases demonstrates that the architecture is a workflow, not a
single model call.

## 23. Test the Design Aloud

### Normal Request

> A signed-in user submits four candidates. The API checks identity, quota,
> input policy, and idempotency, then commits a job and outbox event before
> returning 202. A scheduled worker generates the candidates, output policy
> approves them, object storage receives them, billing settles once, and the
> client receives a completion event with authorized asset IDs.

### Lost Response and Retry

> The first submit commits but its response is lost. The retry uses the same
> idempotency key. The unique tenant/key record returns the existing job, so no
> second queue item or reservation is created.

### Worker Crash

> The worker stops heartbeating during inference. Its lease expires. A bounded
> retry creates a new attempt under the same job. Only a worker with the current
> lease can commit results, and billing still settles once.

### Unsafe Output

> The prompt passes, but one generated image fails output policy. That image
> never receives a readable asset state. The other approved images may be
> delivered, and replacement behavior follows a bounded documented rule.

### Tenant Isolation

> A user from tenant A guesses an asset ID from tenant B. Authorization queries
> by both asset ID and the tenant from the token, finds no authorized row, and
> never creates a signed URL.

### Traffic Spike

> Arrival rate exceeds warm inference capacity. The durable queue absorbs work
> up to its admission limit, fair scheduling protects tenants, autoscaling reacts
> to queue age, and excess new requests receive 429 with retry guidance instead
> of causing an unbounded backlog.

## 24. Important Tradeoffs

| Choice | Benefit | Cost or Risk |
| --- | --- | --- |
| Asynchronous jobs | Survives long inference and reconnects | More states, queue logic, and client handling |
| Polling | Simple client and server | Repeated traffic and slower updates |
| Server-sent events | Efficient one-way status updates | Connection management; polling fallback still needed |
| Shared multi-tenant storage | Efficient and operationally simpler | Requires rigorous tenant keys and authorization |
| Dedicated enterprise infrastructure | Stronger isolation and predictable capacity | Higher cost and operational complexity |
| Four images in one model batch | Efficient and easy to bill | One slow or failed batch can delay all candidates |
| One job per candidate | Partial completion and independent retries | More scheduling, policy, and billing coordination |
| Dynamic batching | Better accelerator throughput | Adds queue delay and batching complexity |
| Strict fail-closed policy | Prevents unchecked content exposure | Can reduce availability during policy outages |
| Model alias | Easy rollout and rollback | Must record the resolved immutable version per job |
| Long retention | Convenient project history | Higher privacy exposure and storage cost |

There is no universally correct row. Choose based on the stated customer and
SLO, then name the downside.

## 25. A Two-Minute Interview Summary

> I would design generation as a durable asynchronous workflow because model
> inference takes around 40 seconds. The submit API authenticates the user,
> derives the tenant, enforces quota and prompt policy, and atomically creates an
> idempotency record, job, billing reservation, and outbox event before returning
> 202. A durable queue and fair scheduler feed model-versioned GPU workers. Every
> output is checked before private object storage commits it, and users access
> approved assets through short-lived signed URLs.
>
> Client retries map to the same logical job, queue retries use leases and
> conditional state transitions, and billing uses an append-only ledger with
> unique settlement events. Tenant IDs, authorization, storage policy, quotas,
> encryption, and audit controls enforce enterprise isolation. I would release
> models through offline evaluation, shadowing, canaries, and rollback. I would
> measure time to first usable asset alongside safety, reliability, latency, and
> accelerator cost, then test worker crashes, blocked outputs, cancellation
> races, regional failure, and traffic spikes.

## 26. Possible Follow-up Questions

| Follow-up | Strong Answer Direction |
| --- | --- |
| How would you show candidates one at a time? | Give each candidate its own child state; publish only after its output check, while the parent job tracks partial and terminal completion. |
| How would image-to-image editing work? | Upload source and mask privately, validate both, create a child job with lineage, and route to an editing-capable model. |
| How would you support a one-hour enterprise deadline? | Add deadline-aware admission, reserved capacity, per-tenant budgets, and reject early when the SLO cannot be met. |
| Can identical prompts use a cache? | Only through explicit same-tenant reuse; a new random seed should normally create new work, and cross-tenant caching risks privacy leakage. |
| How do users reproduce an image? | Record model version, seed, parameters, inputs, and environment metadata, while explaining that exact reproduction may vary across hardware or implementation changes. |
| What if a new model is safer but slower? | Compare it against explicit quality, safety, latency, and cost guardrails; route by product tier or use case rather than assuming one model fits all. |
| How would webhooks work for an API customer? | Sign events, include an event ID, retry with backoff, let consumers deduplicate, and provide a status API as the source of truth. |
| How would you handle data residency? | Pin metadata, queues, object storage, policy execution, and inference to allowed regions; control cross-region logs and disaster recovery copies. |
| How would you support bulk generation? | Separate interactive and batch queues, expose batch progress, use lower priority and larger batches, and cap per-tenant concurrency. |
| What would you partition first? | Partition high-volume job and asset access by tenant and time; shard only after measurements show one store is insufficient. |
| SQL or NoSQL for jobs? | Both can work. Choose the store that supports conditional transitions, indexes, durability, and scale; explain why workflow correctness matters more than the label. |
| What happens if moderation rules change? | Version decisions, apply the new version to new work, define whether old assets need rescanning, and preserve auditable reason codes. |

## 27. Check Your Understanding

Attempt each design aloud before opening its answer. Start with the customer and
requirements, not with a list of cloud services.

### Question 1: Design an AI Video-Generation Platform

Users submit a prompt, wait several minutes for a video, preview it, request a
revision, and download the final file. What changes from the image platform?

<details>
<summary>Show answer and detailed explanation</summary>

The same durable-job foundation applies, but longer work and larger assets make
several decisions more important.

**Assumptions:** A video takes 5-15 minutes, contains multiple generation stages,
and produces a file hundreds of megabytes in size. Creators need progress,
cancellation, preview clips, and resumable download.

**Architecture changes:**

1. Represent the job as a stage graph: script or prompt expansion, key frames,
   frame generation, consistency pass, audio, encoding, policy review, and upload.
2. Persist stage progress and checkpoint expensive intermediate results so one
   late failure does not restart every minute of compute.
3. Schedule by accelerator type, memory, estimated duration, deadline, and
   tenant budget. Separate interactive previews from final high-resolution jobs.
4. Upload directly to object storage using multipart uploads. Deliver previews
   and final video through a CDN with range requests.
5. Run policy checks on prompt, reference media, representative frames, audio,
   and final output according to product policy.
6. Reserve a larger budget, meter actual stage compute, and settle once through
   the same idempotent ledger.
7. Record every model and stage version so a revision has understandable lineage.

**Capacity:** If peak arrival is `2 jobs/second` and average service time is
`600 seconds`, the rough concurrency is `2 * 600 = 1,200` active job slots before
headroom. If each output averages `300 MB`, only `10,000` completed videos add
about `3 TB` before previews, replicas, and intermediate files.

**Failure cases:** Worker loss after minute nine, one failed stage, expired upload,
cancellation during encoding, inconsistent policy results across frames, and a
user retry after the original job already started.

**Useful metrics:** Time to first playable preview, successful final export rate,
revision rate, stage failure rate, unsafe-frame escape rate, accelerator minutes
per exported video, storage, and egress.

The main insight is that a video is not merely a slower image. It is a durable,
multi-stage workflow that benefits from checkpoints, progress, and resumable
large-file delivery.

</details>

### Question 2: Design Enterprise Batch Background Removal

A retailer uploads a catalog of one million product images, removes each
background, and downloads the results. Jobs must be isolated, resumable, and
charged exactly once. How would you design it?

<details>
<summary>Show answer and detailed explanation</summary>

**Customer outcome:** Produce a complete, auditable transformed catalog without
manually tracking one million individual requests.

**API and data:**

1. Create a `batch` with a tenant-scoped idempotency key.
2. Return presigned multipart upload locations for a manifest and source files.
3. Validate the manifest, then create item records in chunks.
4. Expose batch totals such as pending, running, succeeded, failed, and canceled.
5. Produce a result manifest and signed archive or per-file download URLs.

**Architecture:** A batch coordinator pages through the manifest and sends item
jobs to a durable queue. Fair scheduling limits each tenant's active work. Workers
claim item leases, read private source objects, run the model, validate output,
and commit deterministic result keys. A reconciliation worker finds expired
leases and missing outputs. Webhooks and the status API report progress.

**Idempotency and billing:** The logical batch is unique by tenant/key. Each item
has a stable source ID and at most one successful result version. Queue redelivery
cannot create another committed asset. Reserve a batch budget, meter successful
or attempted items according to contract, and use unique ledger events for final
settlement and adjustments.

**Isolation:** Tenant-scoped database partitions, private object prefixes,
short-lived URLs, per-tenant keys where required, region pinning, quotas, and
negative authorization tests protect customer catalogs.

**Capacity and complexity:** Do not load one million rows into memory. Stream the
manifest and page records in `O(K)` work per page. Total transformation work is
`O(N)` for `N` images and can be parallelized up to tenant and fleet limits.

**Failure and testing:** Test a repeated batch request, duplicate manifest rows,
malformed images, worker death after upload, partial batch cancellation, webhook
redelivery, quota exhaustion, one tenant attempting another tenant's result, and
restarting a batch with only failed items.

The main change from an interactive product is priority: throughput, resumability,
manifest correctness, and auditability matter more than second-by-second updates.

</details>

## 28. System Design Mock Scorecard

Give yourself one point for each item:

- [ ] I clarified the customer and successful outcome.
- [ ] I separated required features from out-of-scope work.
- [ ] I stated scale and calculated throughput, concurrency, and storage.
- [ ] I defined an asynchronous API and durable job states.
- [ ] I drew a readable high-level architecture and walked one request through it.
- [ ] I prevented duplicate work and duplicate billing.
- [ ] I covered both input and output policy enforcement.
- [ ] I explained tenant isolation, security, and privacy.
- [ ] I covered failure recovery, observability, model rollout, and cost.
- [ ] I named tradeoffs and adapted when an assumption changed.

| Score | Meaning |
| ---: | --- |
| 0-4 | Re-read the requirements, API, and normal request flow. |
| 5-6 | The foundation is present; repair missing deep dives and failure handling. |
| 7-8 | Interview-ready for a normal prompt; practice changing assumptions. |
| 9-10 | Strong structure and depth; maintain it with timed mocks. |

## Final Readiness Check

You understand this design when you can close the guide and explain:

1. why a 40-second model call becomes an asynchronous durable job,
2. how one idempotency key prevents repeat submissions,
3. how leases and conditional updates handle queue redelivery,
4. why billing uses unique append-only events,
5. where prompt and output safety checks occur,
6. how every data path enforces tenant isolation,
7. how peak arrival rate and service time determine inference concurrency,
8. which metrics distinguish generated images from useful images,
9. how model canaries, guardrails, and rollback reduce release risk,
10. what the system does during a worker crash, policy outage, or traffic spike.
