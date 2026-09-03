# Google and Sierra Interview Mastery Track

[Repository home](./README.md) | [Study CLI](./study.py) | [Study plans](./INTERVIEW_STUDY_PLANS.md) | [Progress tracker](./PROGRESS_TRACKER.md) | [Interview playbook](./INTERVIEW_PLAYBOOK.md) | [Pattern map](./ALGORITHM_PATTERN_MAP.md) | [System design](./system_design/README.md) | [FDE track](./fde_interview/README.md) | [AI engineering](./ai_engineering/README.md)

## Purpose

Use this track when your goal is to be strong enough for both Google-style
software engineering interviews and Sierra-style AI agent engineering
interviews.

The overlap is bigger than it first looks:

```text
clear thinking
    -> precise requirements
    -> clean Python implementation
    -> algorithmic correctness
    -> production design judgment
    -> structured communication
    -> calm follow-up handling
```

Google raises the bar on algorithms, data structures, correctness, and scale.
Sierra raises the bar on product scope, AI agent systems, production readiness,
debugging, and review judgment. The strongest preparation path trains both
without letting either one crowd out the other.

## Sources Checked

- [Google Careers: How we hire](https://www.google.com/about/careers/applications/how-we-hire/)
- [Google Careers: Interview tips](https://www.google.com/about/careers/applications/interview-tips/)
- [Google Careers: Build your future resources](https://www.google.com/about/careers/applications/buildyourfuture/resources/)
- [Google Careers role examples](https://careers.google.com/jobs/results/)
- [Sierra: The AI-native interview](https://sierra.ai/blog/the-ai-native-interview)
- [Sierra careers](https://sierra.ai/careers)
- [Sierra: Context engineering](https://sierra.ai/blog/context-engineering-the-key-to-great-agents)
- [Sierra: Voice AI is only as good as what it hears](https://sierra.ai/blog/voice-ai-is-only-as-good-as-what-it-hears)

As of September 3, 2026, interview loops can still vary by team, country,
seniority, and recruiter instructions. If your recruiter gives a specific
format, that format overrides this plan.

## The Target Skill Stack

| Layer | Google Signal | Sierra Signal | What To Practice |
| --- | --- | --- | --- |
| Problem framing | Understand ambiguous prompts quickly | Scope ambiguous product/customer needs | Clarify inputs, constraints, success, and tradeoffs |
| Python fluency | Implement without autocomplete mistakes | Build/debug quickly in realistic code | Lists, dicts, sets, heaps, recursion, classes, parsing |
| Algorithms | Correct and efficient DS&A | Practical implementation under change | Hash maps, sliding windows, binary search, graphs, DP, tries |
| Communication | Think aloud and justify complexity | Explain product and production choices | State invariants, alternatives, risks, and follow-ups |
| System design | Large-scale distributed systems | AI agent production systems | APIs, state, storage, queues, caches, reliability, observability |
| AI systems | Useful for AI/ML or GenAI roles | Central to the company | RAG, tools, evals, guardrails, context, model releases |
| Review judgment | Senior signal and code quality | Core AI-native onsite signal | Tests, production gaps, data model, abstractions, debugging |

## Weekly Operating System

Run this weekly cycle until the interview. If you only have one hour, do the
first block of the day. If you have more time, add a second problem or a mock.

| Day | Focus | Output |
| --- | --- | --- |
| Monday | Google coding core | One arrays/hash/sliding-window problem solved aloud |
| Tuesday | Graphs, trees, or trie | One traversal problem plus edge-case dry run |
| Wednesday | DP, binary search, or heap | One harder pattern problem plus complexity explanation |
| Thursday | System design fundamentals | One 45-minute design with scale and failure handling |
| Friday | Sierra practical coding and APIs | One parser/API/retry/nested-data prompt |
| Saturday | AI agent or voice design | One customer-service agent, voice, or eval design |
| Sunday | Review and mock repair | Re-solve misses, update tracker, run one scorecard |

Use the CLI for the daily queue:

```bash
python3 study.py next --track google_sierra
python3 study.py mock --kind coding
python3 study.py mock --kind system
python3 study.py scorecard --kind coding
```

## Google-Strength Coding Core

These are the repo problems that give the best Google-style coverage. The goal
is not memorization. The goal is to derive the pattern, code it cleanly, prove
why it works, and survive a changed requirement.

| Priority | Pattern | Problems |
| --- | --- | --- |
| Critical | Hash maps and strings | [Two Sum](./arrays_strings/0001_two_sum.md), [Group Anagrams](./arrays_strings/0049_group_anagrams.md), [Longest Substring](./arrays_strings/0003_longest_substring_without_repeating_characters.md) |
| Critical | Sorting, intervals, binary search | [3Sum](./arrays_strings/0015_3sum.md), [Merge Intervals](./intervals_search/0056_merge_intervals.md), [Binary Search](./intervals_search/0704_binary_search.md), [Koko Eating Bananas](./intervals_search/0875_koko_eating_bananas.md) |
| Critical | Trees and graphs | [Number of Islands](./trees_graphs/0200_number_of_islands.md), [Rotting Oranges](./trees_graphs/0994_rotting_oranges.md), [Clone Graph](./trees_graphs/0133_clone_graph.md), [Course Schedule](./trees_graphs/0207_course_schedule.md) |
| High | Heaps and top-k | [Kth Largest](./heaps/0215_kth_largest_element.md), [Top K Frequent](./heaps/0347_top_k_frequent_elements.md), [Merge K Sorted Lists](./heaps/0023_merge_k_sorted_lists.md) |
| High | Stateful design | [Time Based Key-Value Store](./design_data_structures/0981_time_based_key_value_store.md), [LRU Cache](./design_data_structures/0146_lru_cache.md) |
| High | Trie and prefix structures | [Implement Trie](./trie/0208_implement_trie.md), [Search Suggestions](./trie/1268_search_suggestions_system.md), [Add and Search Words](./trie/0211_design_add_and_search_words.md) |
| Medium | DP and backtracking | [House Robber](./dynamic_programming/0198_house_robber.md), [Coin Change](./dynamic_programming/0322_coin_change.md), [LIS](./dynamic_programming/0300_longest_increasing_subsequence.md), [Word Search](./prefix_recursion/0079_word_search.md) |

### Google Coding Gate

You are not Google-ready until you can do this three times in a row:

```text
45 minutes
    -> clarify constraints
    -> propose brute force
    -> optimize
    -> code without notes
    -> dry-run sample and edge case
    -> explain time and space
    -> answer one follow-up
```

Minimum target:

- `3/4` or higher on at least 12 core/critical problems,
- one graph problem solved cleanly,
- one DP problem solved cleanly,
- one design-data-structure problem solved cleanly,
- no hidden syntax dependence on autocomplete.

## Sierra-Strength Practical Core

Sierra-style strength starts with practical implementation and then moves into
production AI agent judgment.

| Priority | Drill | Source |
| --- | --- | --- |
| Critical | Filter duplicates, count word frequencies, merge person data | [High-priority practical questions](./fde_interview/08_high_priority_practical_coding_questions.md) |
| Critical | Accept-Language parser | [Sierra mastery plan](./fde_interview/09_sierra_ai_agent_interview_mastery.md#high-priority-coding-drills) |
| Critical | API client with retry/backoff/idempotency | [Sierra mastery plan](./fde_interview/09_sierra_ai_agent_interview_mastery.md#high-priority-coding-drills) |
| High | Nested JSON flatten/traversal | [Sierra mastery plan](./fde_interview/09_sierra_ai_agent_interview_mastery.md#high-priority-coding-drills) |
| High | Dependency graph and connected components | [Course Schedule](./trees_graphs/0207_course_schedule.md), [Number of Islands](./trees_graphs/0200_number_of_islands.md) |
| High | Customer-service AI agent design | [Sierra mastery plan](./fde_interview/09_sierra_ai_agent_interview_mastery.md#system-design-master-prompt) |
| High | Voice agent design and evaluation | [Sierra mastery plan](./fde_interview/09_sierra_ai_agent_interview_mastery.md#voice-agent-deep-dive) |

### Sierra Readiness Gate

You are not Sierra-ready until you can:

- build a small but usable product in two hours,
- explain what scope you cut and why,
- demo the main workflow clearly,
- review your code's data model, abstraction, and tests,
- explain the path to production,
- design a customer-service AI agent with tools, context, evals, guardrails,
  observability, and human handoff,
- explain voice-specific failures: ASR, endpointing, turn-taking, tool latency,
  TTS, language switching, and task success.

## Unified Daily Drill

Use this sequence for every coding problem, regardless of company:

```text
1. Restate the problem in one sentence.
2. Ask about constraints, input shape, output order, and malformed data.
3. Give one concrete example.
4. Name the brute-force approach.
5. Identify the bottleneck.
6. Choose the optimized state and invariant.
7. Code in small blocks.
8. Dry-run the sample.
9. Test empty, single, duplicate, missing, and boundary cases.
10. Explain time and space.
11. Handle a follow-up.
```

Use this sequence for every system design prompt:

```text
1. Clarify user, product goal, functional requirements, non-functional requirements.
2. State scale assumptions and simple estimates.
3. Define APIs and durable state.
4. Draw the normal request flow.
5. Deep-dive on the hardest bottleneck or correctness risk.
6. Explain reliability, security, privacy, abuse, and cost.
7. Define observability and evaluation.
8. Handle one changed assumption.
```

## Four-Week Combined Plan

If you have four focused weeks, use this. If you have less time, compress by
keeping the critical items and skipping medium items.

| Week | Goal | Must Finish |
| --- | --- | --- |
| 1 | Python and Google coding base | Hash maps, sliding window, intervals, binary search, `study.py mock --kind coding` twice |
| 2 | Graphs, tries, heaps, DP | Islands, Course Schedule, Trie, Top-K, one DP, one full 45-minute coding mock |
| 3 | System design and AI systems | Foundational design, URL shortener, image platform, enterprise AI adoption, customer-service agent |
| 4 | Sierra production and final mocks | Practical FDE drills, API retry, voice design, Plan-Build-Review, behavioral stories, two mixed mocks |

## Final Mock Week

Run this in the last seven days:

| Day | Mock | Passing Bar |
| --- | --- | --- |
| 1 | Google coding: hash/sliding window | `3/4`, no major edge-case miss |
| 2 | Google coding: graph or trie | `3/4`, clear visited/state invariant |
| 3 | Google coding: DP or binary search on answer | `3/4`, correct recurrence or monotonic condition |
| 4 | Distributed system design | `7/10`, covers storage, cache, queue, failure, observability |
| 5 | AI agent system design | `7/10`, covers tools, permissions, context, evals, human handoff |
| 6 | Sierra Plan-Build-Review | Usable demo plus honest production review |
| 7 | Behavioral and repair day | Six stories under two minutes plus re-solve weakest problem |

## What To Stop Doing

- Do not grind random LeetCode Hard before the critical patterns are automatic.
- Do not read system design answers without doing the 45-minute spoken attempt.
- Do not use AI for no-AI coding practice.
- Do not count a problem as learned if you cannot reproduce it without notes.
- Do not let Sierra prep replace Google fundamentals.
- Do not let Google prep replace product and production judgment.

## Final Readiness Gate

You are ready to interview when all of these are true:

- You can solve unseen Medium coding prompts with structured communication.
- You can explain correctness, not just complexity.
- You can handle graph, trie, heap, binary search, and one DP pattern.
- You can design a scalable backend with APIs, storage, caching, queues,
  failure handling, security, and observability.
- You can design an AI agent with retrieval/context, tools, evals, guardrails,
  and human handoff.
- You can review your own code and name production gaps without sounding
  defensive.
- You can tell six truthful stories about ownership, ambiguity, conflict,
  failure, customer impact, and learning.

## Check Your Understanding

### Question 1:

Why is `Course Schedule` useful for both Google and Sierra preparation?

<details>
<summary>Answer</summary>

For Google, it tests graph modeling, indegree or DFS state, cycle detection, and
correctness reasoning. For Sierra, dependency graphs appear in deployment,
tool orchestration, workflow ordering, and debugging cross-service changes. One
problem trains both algorithmic precision and production reasoning.

</details>

### Question 2:

What is the biggest mistake in trying to prepare for both companies at once?

<details>
<summary>Answer</summary>

The biggest mistake is treating the prep as two unrelated tracks. The better
approach is to build one strong core: precise problem framing, clean Python,
algorithmic correctness, production design, and clear communication. Then add
company-specific spikes: more DS&A depth for Google and more AI agent,
product, debugging, and review practice for Sierra.

</details>
