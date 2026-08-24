# System Design for Beginners

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md)

System design interviews ask how many pieces of software work together. You are
not expected to guess one perfect architecture. You are expected to clarify the
goal, make reasonable assumptions, explain tradeoffs, and notice failure cases.

## Case Study

| Order | Design Question | Main Ideas |
| ---: | --- | --- |
| 1 | [Design an Image-Generation Platform](./image_generation_platform.md) | Asynchronous jobs, safety, idempotency, scheduling, tenant isolation, storage, evaluation, model rollout, and cost |

## Before You Start

It helps to understand these lessons first:

1. [Classes and Objects](../python_basics/08_classes_and_objects.md) for thinking about entities and responsibilities.
2. [Time and Space Complexity](../python_basics/11_time_and_space_complexity.md) for estimates and growth.
3. [LRU Cache](../design_data_structures/0146_lru_cache.md) for state, invariants, and operation guarantees.
4. [Course Schedule](../trees_graphs/0207_course_schedule.md) for dependencies and work ordering.
5. [Heaps and Top-K](../heaps/README.md) for priority scheduling.

You do not need cloud certification or machine-learning expertise. Every new
system term is defined before it is used.

## The Interview Order

Use the same sequence for almost any system design question:

| Step | Question to Answer |
| ---: | --- |
| 1 | Who is the customer, and what successful outcome do they need? |
| 2 | Which features are required now, and which are out of scope? |
| 3 | What scale, latency, availability, safety, and privacy assumptions will we use? |
| 4 | What APIs and durable data represent the workflow? |
| 5 | What is the smallest high-level architecture that satisfies the requirements? |
| 6 | Which two or three hard parts deserve a deeper design? |
| 7 | What fails, how does the system recover, and what do we measure? |
| 8 | What tradeoffs would change if an assumption changes? |

Do not begin by naming databases or drawing twenty boxes. First make the target
clear. Architecture choices only make sense after the requirements are known.

## Beginner Vocabulary

| Term | Plain-English Meaning |
| --- | --- |
| **Synchronous** | The caller waits on the same request until all work finishes. |
| **Asynchronous** | The request records work and returns early; background workers finish it later. |
| **Queue** | A durable waiting line for work that has not started yet. |
| **Worker** | A process or machine that takes a job from a queue and performs it. |
| **Idempotency** | Retrying the same request has the same effect as doing it once. |
| **Tenant** | One customer organization whose users and data share an account boundary. |
| **Control plane** | APIs and metadata that decide what work should happen. |
| **Data plane** | The heavy work and large files, such as model inference and image bytes. |
| **Object storage** | Storage designed for large files addressed by object keys. |
| **CDN** | Servers near users that deliver files without sending every download to the main application. |
| **Signed URL** | A file URL that grants limited access and expires after a short time. |
| **p95 latency** | Ninety-five percent of requests finish within this time; five percent take longer. |
| **SLO** | A measurable reliability or performance target for the service. |
| **At-least-once delivery** | A queue may deliver a message again, so workers must safely handle duplicates. |
| **Lease** | Temporary ownership of a job that expires if a worker disappears. |
| **Backpressure** | Slowing or rejecting new work when downstream capacity is full. |

## Recommended Study Method

1. Read the prompt and spend five minutes writing clarifying questions.
2. Compare your assumptions with the case study.
3. Redraw the architecture from memory using no more than ten boxes.
4. Explain the normal request flow aloud.
5. Explain a duplicate request, worker crash, unsafe output, and traffic spike.
6. Recalculate capacity after changing one scale assumption.
7. Attempt both transfer designs before opening their answers.
8. Run a 45-minute mock and record the result in the [progress tracker](../PROGRESS_TRACKER.md).

## Ready to Move On

You are ready for another system design case when you can:

- begin with customers and requirements instead of technology names,
- state assumptions and perform simple throughput and storage estimates,
- explain why long-running work belongs behind a durable queue,
- prevent a retry from creating duplicate work or duplicate billing,
- keep one tenant from reading or consuming another tenant's resources,
- describe safety checks before and after model inference,
- identify useful product, reliability, safety, and cost metrics,
- test the design with failures and changed requirements,
- explain at least three tradeoffs without claiming there is one perfect answer.

After this case, practice it beside normal coding mocks. System design improves
through repeated explanation and revision, not through memorizing one diagram.
