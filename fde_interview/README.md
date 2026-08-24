# Forward Deployed Engineer Interview Track

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Coding playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [AI engineering](../ai_engineering/README.md) | [System design](../system_design/README.md)

A Forward Deployed Engineer, or FDE, works close to customers while still doing
real engineering. Exact titles and interview loops vary by company. This track
teaches the durable skills that transfer across them: clarify ambiguous needs,
build and explain technical solutions, manage delivery risk, and connect an
architecture to a measurable customer outcome.

## Learning Path

| Order | Lesson | Main Skill |
| ---: | --- | --- |
| 1 | [Role and Interview Map](./01_role_and_interview_map.md) | Understand what to prepare and how the rounds connect |
| 2 | [Customer Discovery and Solutioning](./02_customer_discovery_and_solutioning.md) | Turn ambiguity into a phased recommendation with tradeoffs |
| 3 | [Cloud Architecture Fundamentals](./03_cloud_architecture_fundamentals.md) | Choose compute, data, messaging, networking, and operating controls |
| 4 | [Behavioral Story Workbook](./04_behavioral_story_workbook.md) | Build truthful stories about ownership, customers, conflict, and learning |

Then complete the [AI Engineering for Beginners](../ai_engineering/) course and
the [System Design for Beginners](../system_design/) cases.

## Coding Pattern Extension

The existing 15-problem core remains the first priority. These additional
problems close pattern gaps that often appear inside real-world framing:

| Pattern | Lesson | Real-World Signal |
| --- | --- | --- |
| Two pointers | [15 3Sum](../arrays_strings/0015_3sum.md) | Find combinations after ordering data |
| Monotonic stack | [739 Daily Temperatures](../stacks_queues/0739_daily_temperatures.md) | Resolve the next greater event in a stream |
| Binary search on answer | [875 Koko Eating Bananas](../intervals_search/0875_koko_eating_bananas.md) | Find the smallest capacity that satisfies an SLO |
| Tree BFS | [102 Binary Tree Level Order](../trees_graphs/0102_binary_tree_level_order_traversal.md) | Process hierarchy one depth at a time |
| Multi-source BFS | [994 Rotting Oranges](../trees_graphs/0994_rotting_oranges.md) | Simulate propagation from many starting points |
| Union-find | [684 Redundant Connection](../trees_graphs/0684_redundant_connection.md) | Maintain connectivity while links arrive |
| Linked-list pointers | [206 Reverse Linked List](../linked_lists/0206_reverse_linked_list.md) | Change a pointer-based structure without losing state |

## Choose a Preparation Track

Use this as an add-on to the repository's main [coding study plan](../INTERVIEW_STUDY_PLANS.md).

| Time | FDE Add-On |
| --- | --- |
| 5 days | Read the role map and customer framework; rehearse one customer scenario and two behavioral stories. |
| 10 days | Add cloud fundamentals, LLM fundamentals, RAG, and one system design mock. |
| 14 days | Complete every FDE and AI lesson, three pattern-extension problems, two customer scenarios, and two design mocks. |
| 30 days | Complete all seven extension problems, all FDE/AI lessons, three design cases, four scenario mocks, and a six-story behavioral bank. |
| 60 days | Repeat the 30-day work with spaced review, a small portfolio prototype, weekly mixed mocks, and role-specific research from primary sources. |

For a five-day emergency, do not abandon the coding core to read every new page.
Use the role map to identify the rounds actually present in your interview and
spend time in proportion to those rounds.

## The FDE Mock Loop

One complete practice loop has four parts:

1. **Coding:** solve one problem aloud and test it.
2. **Customer scenario:** clarify, recommend, phase, and handle an objection.
3. **System or AI design:** estimate, draw, deep-dive, and failure-test.
4. **Behavioral:** answer one prompt, then handle three follow-up questions.

Record the weakest observable behavior, not a vague feeling:

```text
Weak note:  "Customer scenario felt bad."
Useful note: "I recommended a vector database before asking how often the
documents change or whether answers require citations."
```

## Ready to Move On

You are ready for an FDE-style interview when you can:

- explain why this role fits you without describing it as easier SWE,
- extract a technical core from an ambiguous customer story,
- state users, current state, constraints, and success metrics before proposing,
- compare at least two options and recommend one with a migration trigger,
- draw a secure, operable cloud architecture without relying on product names,
- explain RAG, prompting, fine-tuning, online serving, and evaluation choices,
- solve coding patterns while translating domain language into data structures,
- tell six truthful behavioral stories with specific personal actions and results,
- adapt calmly when an interviewer changes budget, latency, privacy, or timeline.

## Curriculum Note

This extension was planned after comparing this repository with
[Cracking the FDE Interview](https://github.com/backend-bytes127/cracking-the-fde-interview),
an MIT-licensed community project. The explanations, examples, exercises, and
curriculum structure in this repository are written for this beginner-first
course rather than copied from that project.
