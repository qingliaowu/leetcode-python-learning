# LeetCode Python Learning

A beginner-first path from forgotten Python syntax to explaining interview solutions clearly and confidently.

This repository assumes nothing. Python syntax, algorithm ideas, time and space complexity, edge cases, tests, and interview reasoning are explained in plain language.

## What Is Included

| Material | Count | Purpose |
| --- | ---: | --- |
| Python 3 lessons | 11 | Relearn Python from `print` through recursion and Big-O |
| Interview problems | 26 | Practice the patterns most often used in coding interviews |
| Guided self-check questions | 52 | Transfer each pattern to a new example, then reveal a detailed answer |
| Interview study schedules | 5 | Choose a 5-, 10-, 14-, 30-, or 60-day preparation plan |
| Course guides | 10 | Navigate Python foundations and nine interview topics |
| Progress tracker | 1 | Record lessons, problem scores, review dates, and mock results |
| External packages | 0 | Everything runs with the Python standard library |

## Start Here

Choose the row that sounds most like you:

| Your Situation | Start With |
| --- | --- |
| "I forgot most Python syntax." | [Python 3 Basics for Complete Beginners](./python_basics/) |
| "I can code, but Big-O is confusing." | [Time and Space Complexity](./python_basics/11_time_and_space_complexity.md) |
| "My interview is in 5-60 days." | [Choose an Interview Study Plan](./INTERVIEW_STUDY_PLANS.md) |
| "I need to prepare for a coding interview." | [Interview Problem-Solving Playbook](./INTERVIEW_PLAYBOOK.md) |
| "I want one checklist for everything." | [Open the Learning Progress Tracker](./PROGRESS_TRACKER.md) |
| "I am ready to solve problems." | [Interview Problem Roadmap](#interview-problem-roadmap) |

No package installation is needed. Check Python and run the first lesson:

```bash
python3 --version
python3 python_basics/01_first_program.py
```

## Recommended Learning Path

### Phase 1: Relearn Python

Complete the [11 Python lessons](./python_basics/) in order:

```text
first program
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

Every lesson has a plain-English page, runnable examples, prediction exercises, expected answers, and common mistakes.

### Phase 2: Learn One Pattern at a Time

Do not memorize finished code. For each problem:

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

## What Every Problem Contains

| File | What It Gives You |
| --- | --- |
| Lesson `.md` | Problem summary, Python reminders, approach, dry run, correctness, complexity, edge cases, common mistakes, interview explanation, follow-ups, and two self-checks with detailed answers |
| Solution `.py` | Readable Python 3 code, focused comments, type hints, and executable assertions |
| Topic `README.md` | Shared navigation, prerequisites, recommended order, pattern recognition, and a move-on checkpoint |

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

## Interview Problem Roadmap

The order below moves from common collection patterns toward more specialized structures and dynamic programming.

| Order | Topic | Problems | Guide |
| ---: | --- | ---: | --- |
| 1 | Arrays, strings, hash maps, sliding window | 3 | [Open](./arrays_strings/) |
| 2 | Stacks and queues | 1 | [Open](./stacks_queues/) |
| 3 | Intervals, sorting, binary search | 4 | [Open](./intervals_search/) |
| 4 | Data structure design | 2 | [Open](./design_data_structures/) |
| 5 | Trees and graphs | 3 | [Open](./trees_graphs/) |
| 6 | Heaps and top-k | 3 | [Open](./heaps/) |
| 7 | Prefix sums and backtracking | 2 | [Open](./prefix_recursion/) |
| 8 | Trie | 5 | [Open](./trie/) |
| 9 | Dynamic programming | 3 | [Open](./dynamic_programming/) |

## Complete Problem Index

### Arrays, Strings, and Hash Maps

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 1 | [Two Sum](./arrays_strings/0001_two_sum.md) | Complement hash map | [Python](./arrays_strings/0001_two_sum.py) |
| 49 | [Group Anagrams](./arrays_strings/0049_group_anagrams.md) | Immutable grouping key | [Python](./arrays_strings/0049_group_anagrams.py) |
| 3 | [Longest Substring Without Repeating Characters](./arrays_strings/0003_longest_substring_without_repeating_characters.md) | Sliding window | [Python](./arrays_strings/0003_longest_substring_without_repeating_characters.py) |

### Stacks and Queues

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 394 | [Decode String](./stacks_queues/0394_decode_string.md) | Stack of paused nested states | [Python](./stacks_queues/0394_decode_string.py) |

### Intervals and Binary Search

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 56 | [Merge Intervals](./intervals_search/0056_merge_intervals.md) | Sort, then merge | [Python](./intervals_search/0056_merge_intervals.py) |
| 253 | [Meeting Rooms II](./intervals_search/0253_meeting_rooms_ii.md) | Min-heap of end times | [Python](./intervals_search/0253_meeting_rooms_ii.py) |
| 704 | [Binary Search](./intervals_search/0704_binary_search.md) | Discard half of a sorted array | [Python](./intervals_search/0704_binary_search.py) |
| 33 | [Search in Rotated Sorted Array](./intervals_search/0033_search_in_rotated_sorted_array.md) | Modified binary search | [Python](./intervals_search/0033_search_in_rotated_sorted_array.py) |

### Data Structure Design

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 981 | [Time Based Key-Value Store](./design_data_structures/0981_time_based_key_value_store.md) | Hash map and binary search | [Python](./design_data_structures/0981_time_based_key_value_store.py) |
| 146 | [LRU Cache](./design_data_structures/0146_lru_cache.md) | Hash map and doubly linked list | [Python](./design_data_structures/0146_lru_cache.py) |

### Trees and Graphs

| LeetCode | Problem | Main Pattern | Solution |
| ---: | --- | --- | --- |
| 200 | [Number of Islands](./trees_graphs/0200_number_of_islands.md) | Grid DFS | [Python](./trees_graphs/0200_number_of_islands.py) |
| 133 | [Clone Graph](./trees_graphs/0133_clone_graph.md) | BFS and clone map | [Python](./trees_graphs/0133_clone_graph.py) |
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

## Test Everything

Each Python file contains assertions for normal examples and important edge cases. The verifier first checks required root files, topic guides, filename conventions, and every Markdown/Python lesson pair. It then runs all examples in learning order:

```bash
python3 verify_solutions.py
```

A successful run ends with:

```text
37/37 Python files passed.
```

Run one lesson or solution directly while studying:

```bash
python3 python_basics/05_dictionaries_and_sets.py
python3 trie/0208_implement_trie.py
python3 dynamic_programming/0322_coin_change.py
```

## Repository Structure

```text
.
├── python_basics/          # 11 beginner Python lessons
├── arrays_strings/         # hash maps and sliding window
├── stacks_queues/          # nested parsing with a stack
├── intervals_search/       # intervals, sorting, binary search
├── design_data_structures/ # stateful APIs and operation guarantees
├── trees_graphs/           # DFS, BFS, topological sort, graph copying
├── heaps/                  # top-k and multiway merging
├── prefix_recursion/       # prefix sums and backtracking
├── trie/                   # prefix-tree design and applications
├── dynamic_programming/    # saved-state recurrence patterns
├── INTERVIEW_PLAYBOOK.md   # solve-aloud interview process
├── INTERVIEW_STUDY_PLANS.md # 5/10/14/30/60-day preparation tracks
├── PROGRESS_TRACKER.md     # lesson, review, and mock checklist
├── verify_solutions.py     # validates structure and runs every example
├── .gitignore              # ignores local Python and OS artifacts
└── README.md
```

## Adding Another Problem

Keep new material consistent with the beginner-first style:

1. Name files with the zero-padded LeetCode number and descriptive title.
2. Write the question in your own words instead of copying the full statement.
3. Explain new Python syntax before relying on it.
4. Define the algorithm's state or invariant in one sentence.
5. Show a dry run with changing variables or data structures.
6. Explain correctness, assumptions, edge cases, time, and extra space.
7. Include executable assertions in the Python file.
8. Add the problem to its topic guide, the progress tracker, this index, and the ordered `COURSE_SECTIONS` entry in `verify_solutions.py`.
9. Run `python3 verify_solutions.py` to check naming, file pairing, and assertions.

Clarity is the goal. A beginner should be able to understand not only what the code does, but why each step exists.
