# LeetCode Python Learning

A beginner-first path from installing and running Python to coding, system
design, AI engineering, and Forward Deployed Engineer interviews.

This repository assumes nothing. Terminal commands, Python syntax, algorithm
ideas, system architecture, complexity, edge cases, tests, and interview
reasoning are explained in plain language. The code requires Python `3.10` or
newer and uses no external packages.

## What Is Included

| Material | Count | Purpose |
| --- | ---: | --- |
| Python 3 lessons | 12 | Start, debug, and relearn Python from `print` through recursion and Big-O |
| Coding interview problems | 33 | Practice core patterns plus an FDE-oriented pattern extension |
| System design lessons | 4 | Learn reusable patterns and design rate limiting, URL shortening, and image generation |
| FDE interview lessons | 5 | Prepare role knowledge, customer solutioning, cloud architecture, enterprise AI adoption, and behavioral stories |
| AI engineering lessons | 4 | Learn LLM products, RAG, accuracy and latency diagnosis, model delivery, evaluation, and monitoring |
| Guided practice prompts | 100+ | Practice Python, coding, design, AI, and customer skills, then reveal detailed answers |
| Interview study schedules | 5 | Choose a 5-, 10-, 14-, 30-, or 60-day preparation plan |
| Course guides | 14 | Navigate Python, ten coding topics, system design, FDE, and AI engineering |
| Quick references | 2 | Look up Python syntax or choose an algorithm pattern without rereading a course |
| Progress tracker | 1 | Record lessons, problem scores, review dates, and mock results |
| External packages | 0 | Everything runs with the Python standard library |

## Start Here

Choose the row that sounds most like you:

| Your Situation | Start With |
| --- | --- |
| "I do not know how to run the files." | [Setup, Running Files, and Reading Errors](./python_basics/00_setup_and_errors.md) |
| "I forgot most Python syntax." | [Python 3 Basics for Complete Beginners](./python_basics/) |
| "I need one Python syntax page." | [Python Interview Cheat Sheet](./PYTHON_CHEAT_SHEET.md) |
| "I can code, but Big-O is confusing." | [Time and Space Complexity](./python_basics/11_time_and_space_complexity.md) |
| "I understand the question but cannot choose a pattern." | [Algorithm Pattern Map](./ALGORITHM_PATTERN_MAP.md) |
| "My interview is in 5-60 days." | [Choose an Interview Study Plan](./INTERVIEW_STUDY_PLANS.md) |
| "I need to prepare for a coding interview." | [Interview Problem-Solving Playbook](./INTERVIEW_PLAYBOOK.md) |
| "I need to prepare for a system design interview." | [System Design for Beginners](./system_design/) |
| "I am targeting a Forward Deployed Engineer role." | [FDE Interview Track](./fde_interview/) |
| "I need to design enterprise AI adoption." | [Enterprise AI Adoption Design](./fde_interview/05_enterprise_ai_adoption.md) |
| "I need AI engineering fundamentals." | [AI Engineering for Beginners](./ai_engineering/) |
| "My RAG system is inaccurate or slow." | [RAG Accuracy and Latency Playbook](./ai_engineering/04_rag_accuracy_latency_playbook.md) |
| "I want one checklist for everything." | [Open the Learning Progress Tracker](./PROGRESS_TRACKER.md) |
| "I am ready to solve problems." | [Interview Roadmap](#interview-roadmap) |

No package installation is needed. Run the setup check from the repository root:

```bash
python3 python_basics/00_setup_and_errors.py
```

Windows PowerShell users can replace `python3` with `py -3`.

## Recommended Learning Path

### Phase 1: Relearn Python

Complete the [12 Python lessons](./python_basics/) in order:

```text
setup, running files, and reading errors
    -> first program
    -> variables and values
    -> strings
    -> lists and tuples
    -> dictionaries and sets
    -> conditions and loops
    -> functions
    -> classes and objects
    -> recursion
    -> Python for LeetCode
    -> time and space complexity
```

Every lesson has a plain-English page, runnable examples, expected answers, and
common mistakes. Use the [Python cheat sheet](./PYTHON_CHEAT_SHEET.md) for quick
lookups instead of trying to memorize every method.

### Phase 2: Learn One Pattern at a Time

Open the [Algorithm Pattern Map](./ALGORITHM_PATTERN_MAP.md) when you need help
turning question clues into a candidate approach. Do not memorize finished code.
For each problem:

1. Read the question summary and examples.
2. Restate the input, output, and assumptions aloud.
3. Describe a direct or brute-force approach.
4. Identify its repeated work or bottleneck.
5. Choose a pattern and state what your variables mean.
6. Code the solution in small logical blocks.
7. Trace a normal example and an edge case through the code.
8. Explain time and space complexity in complete sentences.
9. Attempt both self-check questions before opening their answers.

The [Interview Playbook](./INTERVIEW_PLAYBOOK.md) provides sentence templates for every step. The [5-, 10-, 14-, 30-, and 60-day study plans](./INTERVIEW_STUDY_PLANS.md) turn this process into a daily schedule. Record attempts and review dates in the [progress tracker](./PROGRESS_TRACKER.md).

### Phase 3: Practice Without Notes

A problem is interview-ready when you can:

- recognize the pattern from the question,
- derive the approach instead of reciting code,
- explain why the algorithm is correct,
- write it without hidden gaps,
- test assumptions and edge cases aloud,
- justify time and space complexity,
- adapt the solution when an interviewer changes one requirement.

Repeat difficult problems after one day and again after one week.

### Phase 4: Practice System Design

If your target role includes system design, begin with [Foundational System Design Patterns](./system_design/foundational_patterns.md), then practice the [rate limiter](./system_design/rate_limiter.md), [URL shortener](./system_design/url_shortener.md), and [image-generation platform](./system_design/image_generation_platform.md).

Run each case aloud in 45 minutes. Redraw it without notes, change one assumption, and use the [system design scorecard](./system_design/image_generation_platform.md#28-system-design-mock-scorecard) to find the next area to repair.

### Phase 5: Add FDE and AI Engineering

For a customer-facing engineering role, use the [FDE Interview Track](./fde_interview/)
to practice role mapping, customer discovery, cloud architecture, enterprise AI
adoption, and truthful behavioral stories. Complete
[AI Engineering for Beginners](./ai_engineering/) when the role includes LLM,
retrieval, model delivery, or evaluation depth. Use
[Enterprise AI Adoption Design](./fde_interview/05_enterprise_ai_adoption.md) as
the capstone that connects a business problem to production architecture,
evaluation, rollout, user adoption, operating ownership, and measurable value.
Use the [RAG Accuracy and Latency Playbook](./ai_engineering/04_rag_accuracy_latency_playbook.md)
to practice isolating retrieval, context, generation, queue, and serving failures
without guessing.

The FDE extension also adds seven coding patterns after the original 15-problem core. Keep the core first when time is short.

## What Each Lesson Contains

| File | What It Gives You |
| --- | --- |
| Lesson `.md` | Problem summary, Python reminders, approach, dry run, correctness, complexity, edge cases, common mistakes, interview explanation, follow-ups, and two self-checks with detailed answers |
| Solution `.py` | Readable Python 3 code, focused comments, type hints, and executable assertions |
| Topic `README.md` | Shared navigation, prerequisites, recommended order, pattern recognition, and a move-on checkpoint |
| Python cheat sheet | One-page-style lookup for syntax, collections, tools, mutation, and common operation costs |
| Algorithm pattern map | Recognition questions, pattern comparisons, state, invariants, and a complete problem map |
| System design lesson | Requirements, assumptions, estimates, architecture patterns, failures, testing, follow-ups, scorecard, and detailed transfer designs |
| FDE or AI lesson | Plain-language concepts, decision frameworks, customer context, production risks, mock scorecards, and detailed exercises |

## Core 15-Problem Checklist

This requested interview set is fully included. Use the links to open each beginner lesson:

1. [1 Two Sum](./arrays_strings/0001_two_sum.md)
2. [49 Group Anagrams](./arrays_strings/0049_group_anagrams.md)
3. [3 Longest Substring Without Repeating Characters](./arrays_strings/0003_longest_substring_without_repeating_characters.md)
4. [208 Implement Trie](./trie/0208_implement_trie.md)
5. [1268 Search Suggestions System](./trie/1268_search_suggestions_system.md)
6. [981 Time Based Key-Value Store](./design_data_structures/0981_time_based_key_value_store.md)
7. [146 LRU Cache](./design_data_structures/0146_lru_cache.md)
8. [394 Decode String](./stacks_queues/0394_decode_string.md)
9. [200 Number of Islands](./trees_graphs/0200_number_of_islands.md)
10. [133 Clone Graph](./trees_graphs/0133_clone_graph.md)
11. [207 Course Schedule](./trees_graphs/0207_course_schedule.md)
12. [347 Top K Frequent Elements](./heaps/0347_top_k_frequent_elements.md)
13. [215 Kth Largest Element](./heaps/0215_kth_largest_element.md)
14. [56 Merge Intervals](./intervals_search/0056_merge_intervals.md)
15. [704 Binary Search](./intervals_search/0704_binary_search.md)

## Interview Roadmap

The order below moves from common collection patterns toward specialized structures, production architecture, and customer-facing engineering.

| Order | Topic | Lessons | Guide |
| ---: | --- | ---: | --- |
| 1 | Arrays, strings, hash maps, sliding window, two pointers | 4 | [Open](./arrays_strings/) |
| 2 | Stacks and queues | 2 | [Open](./stacks_queues/) |
| 3 | Linked lists | 1 | [Open](./linked_lists/) |
| 4 | Intervals, sorting, binary search | 5 | [Open](./intervals_search/) |
| 5 | Data structure design | 2 | [Open](./design_data_structures/) |
| 6 | Trees and graphs | 6 | [Open](./trees_graphs/) |
| 7 | Heaps and top-k | 3 | [Open](./heaps/) |
| 8 | Prefix sums and backtracking | 2 | [Open](./prefix_recursion/) |
| 9 | Trie | 5 | [Open](./trie/) |
| 10 | Dynamic programming | 3 | [Open](./dynamic_programming/) |
| 11 | System design | 4 | [Open](./system_design/) |
| 12 | FDE interview preparation | 5 | [Open](./fde_interview/) |
| 13 | AI engineering | 4 | [Open](./ai_engineering/) |

## Complete Learning Index

### Arrays, Strings, and Hash Maps

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 1 | [Two Sum](./arrays_strings/0001_two_sum.md) | Complement hash map | [Python](./arrays_strings/0001_two_sum.py) |
| 49 | [Group Anagrams](./arrays_strings/0049_group_anagrams.md) | Immutable grouping key | [Python](./arrays_strings/0049_group_anagrams.py) |
| 3 | [Longest Substring Without Repeating Characters](./arrays_strings/0003_longest_substring_without_repeating_characters.md) | Sliding window | [Python](./arrays_strings/0003_longest_substring_without_repeating_characters.py) |
| 15 | [3Sum](./arrays_strings/0015_3sum.md) | Sorting and two pointers | [Python](./arrays_strings/0015_3sum.py) |

### Stacks and Queues

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 394 | [Decode String](./stacks_queues/0394_decode_string.md) | Stack of paused nested states | [Python](./stacks_queues/0394_decode_string.py) |
| 739 | [Daily Temperatures](./stacks_queues/0739_daily_temperatures.md) | Monotonic decreasing stack | [Python](./stacks_queues/0739_daily_temperatures.py) |

### Linked Lists

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 206 | [Reverse Linked List](./linked_lists/0206_reverse_linked_list.md) | Three-pointer rewiring | [Python](./linked_lists/0206_reverse_linked_list.py) |

### Intervals and Binary Search

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 56 | [Merge Intervals](./intervals_search/0056_merge_intervals.md) | Sort, then merge | [Python](./intervals_search/0056_merge_intervals.py) |
| 253 | [Meeting Rooms II](./intervals_search/0253_meeting_rooms_ii.md) | Min-heap of end times | [Python](./intervals_search/0253_meeting_rooms_ii.py) |
| 704 | [Binary Search](./intervals_search/0704_binary_search.md) | Discard half of a sorted array | [Python](./intervals_search/0704_binary_search.py) |
| 33 | [Search in Rotated Sorted Array](./intervals_search/0033_search_in_rotated_sorted_array.md) | Modified binary search | [Python](./intervals_search/0033_search_in_rotated_sorted_array.py) |
| 875 | [Koko Eating Bananas](./intervals_search/0875_koko_eating_bananas.md) | Binary search on the answer | [Python](./intervals_search/0875_koko_eating_bananas.py) |

### Data Structure Design

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 981 | [Time Based Key-Value Store](./design_data_structures/0981_time_based_key_value_store.md) | Hash map and binary search | [Python](./design_data_structures/0981_time_based_key_value_store.py) |
| 146 | [LRU Cache](./design_data_structures/0146_lru_cache.md) | Hash map and doubly linked list | [Python](./design_data_structures/0146_lru_cache.py) |

### Trees and Graphs

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 102 | [Binary Tree Level Order Traversal](./trees_graphs/0102_binary_tree_level_order_traversal.md) | Tree BFS by level | [Python](./trees_graphs/0102_binary_tree_level_order_traversal.py) |
| 200 | [Number of Islands](./trees_graphs/0200_number_of_islands.md) | Grid DFS | [Python](./trees_graphs/0200_number_of_islands.py) |
| 994 | [Rotting Oranges](./trees_graphs/0994_rotting_oranges.md) | Multi-source BFS | [Python](./trees_graphs/0994_rotting_oranges.py) |
| 133 | [Clone Graph](./trees_graphs/0133_clone_graph.md) | BFS and clone map | [Python](./trees_graphs/0133_clone_graph.py) |
| 684 | [Redundant Connection](./trees_graphs/0684_redundant_connection.md) | Union-find | [Python](./trees_graphs/0684_redundant_connection.py) |
| 207 | [Course Schedule](./trees_graphs/0207_course_schedule.md) | Topological sort | [Python](./trees_graphs/0207_course_schedule.py) |

### Heaps and Top-K

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 215 | [Kth Largest Element](./heaps/0215_kth_largest_element.md) | Min-heap of size `k` | [Python](./heaps/0215_kth_largest_element.py) |
| 347 | [Top K Frequent Elements](./heaps/0347_top_k_frequent_elements.md) | Frequency map and heap | [Python](./heaps/0347_top_k_frequent_elements.py) |
| 23 | [Merge K Sorted Lists](./heaps/0023_merge_k_sorted_lists.md) | Heap-based multiway merge | [Python](./heaps/0023_merge_k_sorted_lists.py) |

### Prefix Sums and Backtracking

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 560 | [Subarray Sum Equals K](./prefix_recursion/0560_subarray_sum_equals_k.md) | Prefix-sum frequency map | [Python](./prefix_recursion/0560_subarray_sum_equals_k.py) |
| 79 | [Word Search](./prefix_recursion/0079_word_search.md) | DFS backtracking | [Python](./prefix_recursion/0079_word_search.py) |

### Trie

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 208 | [Implement Trie](./trie/0208_implement_trie.md) | Core Trie operations | [Python](./trie/0208_implement_trie.py) |
| 1268 | [Search Suggestions System](./trie/1268_search_suggestions_system.md) | Cached prefix suggestions | [Python](./trie/1268_search_suggestions_system.py) |
| 211 | [Design Add and Search Words](./trie/0211_design_add_and_search_words.md) | Trie and wildcard DFS | [Python](./trie/0211_design_add_and_search_words.py) |
| 648 | [Replace Words](./trie/0648_replace_words.md) | Shortest saved prefix | [Python](./trie/0648_replace_words.py) |
| 677 | [Map Sum Pairs](./trie/0677_map_sum_pairs.md) | Cached prefix totals | [Python](./trie/0677_map_sum_pairs.py) |

### Dynamic Programming

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 198 | [House Robber](./dynamic_programming/0198_house_robber.md) | Take or skip | [Python](./dynamic_programming/0198_house_robber.py) |
| 322 | [Coin Change](./dynamic_programming/0322_coin_change.md) | Minimum result for each amount | [Python](./dynamic_programming/0322_coin_change.py) |
| 300 | [Longest Increasing Subsequence](./dynamic_programming/0300_longest_increasing_subsequence.md) | Best sequence ending at each index | [Python](./dynamic_programming/0300_longest_increasing_subsequence.py) |

### System Design

| Lesson | Main Interview Skill |
| --- | --- |
| [Foundational System Design Patterns](./system_design/foundational_patterns.md) | Requirements, estimates, APIs, storage, caching, queues, reliability, security, observability, and cost |
| [Design a Rate Limiter](./system_design/rate_limiter.md) | Algorithms, atomic counters, distributed enforcement, hot keys, and fail-open versus fail-closed behavior |
| [Design a URL Shortener](./system_design/url_shortener.md) | Key generation, redirects, caching, storage, abuse prevention, analytics, and expiration |
| [Design an Image-Generation Platform](./system_design/image_generation_platform.md) | Long-running jobs, safety, idempotency, billing, scheduling, tenant isolation, storage, model rollout, evaluation, observability, and cost |

### FDE Interview Preparation

| Lesson | Main Interview Skill |
| --- | --- |
| [Role and Interview Map](./fde_interview/01_role_and_interview_map.md) | Translate an ambiguous role description into evidence you must demonstrate |
| [Customer Discovery and Solutioning](./fde_interview/02_customer_discovery_and_solutioning.md) | Discover the real outcome, constraints, stakeholders, risks, and acceptance test |
| [Cloud Architecture Fundamentals](./fde_interview/03_cloud_architecture_fundamentals.md) | Explain portable cloud building blocks and their tradeoffs without hiding behind service names |
| [Behavioral Story Workbook](./fde_interview/04_behavioral_story_workbook.md) | Build truthful STAR-L stories about ownership, ambiguity, conflict, failure, and customer impact |
| [Enterprise AI Adoption Design](./fde_interview/05_enterprise_ai_adoption.md) | Select a valuable workflow and design the AI system, evaluation, governance, rollout, adoption, ownership, and economics |

### AI Engineering

| Lesson | Main Interview Skill |
| --- | --- |
| [LLM Product Fundamentals](./ai_engineering/01_llm_product_fundamentals.md) | Choose prompting, retrieval, tools, or fine-tuning and place policy around probabilistic output |
| [Retrieval-Augmented Generation](./ai_engineering/02_rag_systems.md) | Design ingestion, tenant-safe retrieval, citations, evaluation, and failure handling |
| [Model Delivery and Evaluation](./ai_engineering/03_model_delivery_and_evaluation.md) | Version, test, release, monitor, roll back, and control the cost of model changes |
| [RAG Accuracy and Latency Troubleshooting](./ai_engineering/04_rag_accuracy_latency_playbook.md) | Trace one failed request, isolate the broken layer, repair quality or tail latency, and prove the tradeoff |

## Test Everything

Each Python file contains assertions for normal examples and important edge cases. The verifier first checks required root files, topic guides, documentation lessons, filename conventions, and every Markdown/Python lesson pair. It then runs all examples in learning order:

```bash
python3 verify_solutions.py
```

A successful run ends with:

```text
45/45 Python files passed.
```

Run one lesson or solution directly while studying:

```bash
python3 python_basics/00_setup_and_errors.py
python3 python_basics/05_dictionaries_and_sets.py
python3 linked_lists/0206_reverse_linked_list.py
python3 trie/0208_implement_trie.py
python3 dynamic_programming/0322_coin_change.py
```

## Repository Structure

```text
.
├── python_basics/          # 12 beginner Python lessons
├── arrays_strings/         # hash maps, sliding window, two pointers
├── stacks_queues/          # nested parsing and monotonic stacks
├── linked_lists/           # pointer updates on linked nodes
├── intervals_search/       # intervals and two forms of binary search
├── design_data_structures/ # stateful APIs and operation guarantees
├── trees_graphs/           # DFS, BFS, union-find, graph copying
├── heaps/                  # top-k and multiway merging
├── prefix_recursion/       # prefix sums and backtracking
├── trie/                   # prefix-tree design and applications
├── dynamic_programming/    # saved-state recurrence patterns
├── system_design/          # foundations and production design cases
├── fde_interview/          # role, customer, cloud, AI adoption, and behavioral skills
├── ai_engineering/         # LLM, RAG, troubleshooting, delivery, and evaluation skills
├── INTERVIEW_PLAYBOOK.md   # solve-aloud interview process
├── INTERVIEW_STUDY_PLANS.md # 5/10/14/30/60-day preparation tracks
├── PROGRESS_TRACKER.md     # lesson, review, and mock checklist
├── PYTHON_CHEAT_SHEET.md   # quick syntax and standard-library reference
├── ALGORITHM_PATTERN_MAP.md # beginner pattern-selection decision map
├── verify_solutions.py     # validates structure and runs every example
├── .gitignore              # ignores local Python and OS artifacts
└── README.md
```

## Adding Another Coding Problem

Keep new material consistent with the beginner-first style:

1. Name files with the zero-padded LeetCode number and descriptive title.
2. Write the question in your own words instead of copying the full statement.
3. Explain new Python syntax before relying on it.
4. Define the algorithm's state or invariant in one sentence.
5. Show a dry run with changing variables or data structures.
6. Explain correctness, assumptions, edge cases, time, and extra space.
7. Include executable assertions in the Python file.
8. Add the problem to its topic guide, the pattern map, the progress tracker,
   this index, and the ordered `COURSE_SECTIONS` entry in
   `verify_solutions.py`.
9. Run `python3 verify_solutions.py` to check navigation, Markdown structure,
   file pairing, and assertions.

## Adding Another Documentation Lesson

1. Begin with the customer, outcome, scope, and explicit assumptions.
2. Estimate request rate, concurrent work, storage, and dominant cost.
3. Define APIs, durable records, state transitions, and correctness invariants.
4. Draw the smallest architecture that satisfies the requirements.
5. Deep-dive on the hardest reliability, security, and scaling decisions.
6. Explain policy, tenant isolation, observability, evaluation, and operations where relevant.
7. Include failures, edge cases, tradeoffs, an interview summary, follow-ups, and two transfer exercises with detailed answers.
8. Add the lesson to its course guide, this index, the progress tracker, and `DOCUMENTATION_SECTIONS` in `verify_solutions.py`.
9. Run `python3 verify_solutions.py` to check navigation, Markdown structure,
   curriculum indexing, and every executable example.

Clarity is the goal. A beginner should understand not only what the code or architecture does, but why each step and design decision exists.
