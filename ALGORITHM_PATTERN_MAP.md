# Algorithm Pattern Map for Beginners

[Repository home](./README.md) | [Python cheat sheet](./PYTHON_CHEAT_SHEET.md) | [Interview playbook](./INTERVIEW_PLAYBOOK.md) | [Study plans](./INTERVIEW_STUDY_PLANS.md) | [Progress tracker](./PROGRESS_TRACKER.md)

A pattern is a reusable way to organize information. It is not a magic keyword
and it is not finished code to memorize.

Use this page after you understand the question but before opening its lesson.

## The 60-Second Pattern Check

Ask these questions in order:

1. Do I need fast lookup, counting, grouping, or earlier information?
   Start with a **dictionary** or **set**.
2. Is the answer one continuous range in an array or string?
   Consider a **sliding window** or **prefix sum**.
3. Is the input sorted, or would sorting make movement predictable?
   Consider **two pointers**, **interval sorting**, or **binary search**.
4. Am I finding the minimum or maximum value that passes a yes/no test?
   Consider **binary search on the answer**.
5. Does a new item resolve the latest unresolved larger/smaller question?
   Consider a **monotonic stack**.
6. Is work nested, and must the latest unfinished work resume first?
   Consider a normal **stack**.
7. Do I repeatedly need only the smallest, largest, or best `K` candidates?
   Consider a **heap**.
8. Are values connected as nodes, cells, dependencies, or hierarchy?
   Model a **tree or graph**, then choose DFS, BFS, union-find, or topological sort.
9. Are many operations organized by text prefix?
   Consider a **Trie**.
10. Does one optimal answer reuse optimal answers to smaller repeated states?
    Consider **dynamic programming**.
11. Must I try choices, undo them, and try another path?
    Consider **backtracking**.
12. Must several operations stay fast across many calls?
    Design stored state and an **invariant**.

The question may combine patterns. Name the job of each one.

## Four Words to Say Before Coding

```text
Input -> State -> Invariant -> Answer
```

- **Input:** What shape am I receiving?
- **State:** What information must survive to the next step?
- **Invariant:** What fact stays true while the algorithm runs?
- **Answer:** When and where is the requested result produced?

Example for Two Sum:

```text
Input:     unsorted integers and a target
State:     map earlier value -> earlier index
Invariant: the map contains only indexes before the current index
Answer:    saved complement index plus current index
```

## Master Pattern Table

| Pattern | Recognition Signal | State to Explain | Typical Cost | First Lesson |
| --- | --- | --- | --- | --- |
| Hash map lookup | Need a partner or earlier fact quickly | Key and exact meaning of its value | `O(N)` time, `O(N)` space | [Two Sum](./arrays_strings/0001_two_sum.md) |
| Hash map grouping | Equivalent items belong together | Immutable group key | Often `O(N * K log K)` | [Group Anagrams](./arrays_strings/0049_group_anagrams.md) |
| Sliding window | Longest/shortest continuous valid range | `left`, `right`, and what makes the window valid | Often `O(N)` | [Longest Substring](./arrays_strings/0003_longest_substring_without_repeating_characters.md) |
| Two pointers | Sorted values guide which side moves | Fixed value plus left/right candidates | Often `O(N)` after sorting | [3Sum](./arrays_strings/0015_3sum.md) |
| Nested stack | Latest unfinished work closes first | Saved outer state | Input plus output size | [Decode String](./stacks_queues/0394_decode_string.md) |
| Monotonic stack | Next greater/smaller item | Unresolved indexes in monotonic order | `O(N)` | [Daily Temperatures](./stacks_queues/0739_daily_temperatures.md) |
| Pointer rewiring | Change links without losing the rest | Previous, current, saved next | `O(N)` time, `O(1)` space | [Reverse Linked List](./linked_lists/0206_reverse_linked_list.md) |
| Sort and merge | Overlapping ranges | Last merged interval | `O(N log N)` | [Merge Intervals](./intervals_search/0056_merge_intervals.md) |
| Heap of resources | Reuse earliest available resource | One availability per allocated resource | `O(N log N)` | [Meeting Rooms II](./intervals_search/0253_meeting_rooms_ii.md) |
| Binary search in data | Sorted data permits half-discard | Inclusive or half-open candidate range | `O(log N)` | [Binary Search](./intervals_search/0704_binary_search.md) |
| Modified binary search | Sorted structure has a twist | Candidate range plus proof of sorted side | `O(log N)` | [Rotated Search](./intervals_search/0033_search_in_rotated_sorted_array.md) |
| Binary search on answer | Feasibility changes only once | First feasible or last feasible boundary | `O(N log M)` commonly | [Koko Eating Bananas](./intervals_search/0875_koko_eating_bananas.md) |
| Historical design | Query value at or before a point | Sorted history per key | `O(log M)` query | [TimeMap](./design_data_structures/0981_time_based_key_value_store.md) |
| Combined structures | Two jobs need two structures | Shared invariant across both | Required operation bounds | [LRU Cache](./design_data_structures/0146_lru_cache.md) |
| Tree BFS | Output or process by depth | Queue containing one frontier | `O(N)` | [Level Order](./trees_graphs/0102_binary_tree_level_order_traversal.md) |
| Grid DFS | Count or visit connected regions | Stack/recursion plus visited marking | `O(R * C)` | [Number of Islands](./trees_graphs/0200_number_of_islands.md) |
| Multi-source BFS | Spread starts simultaneously | Queue seeded with all distance-zero sources | `O(R * C)` | [Rotting Oranges](./trees_graphs/0994_rotting_oranges.md) |
| Graph copy | Copy cycles without duplicate objects | Original node -> cloned node | `O(V + E)` | [Clone Graph](./trees_graphs/0133_clone_graph.md) |
| Union-find | Connectivity changes as edges arrive | Parent and component size/rank | Almost `O(E)` | [Redundant Connection](./trees_graphs/0684_redundant_connection.md) |
| Topological sort | Directed dependencies need an order | In-degree plus outgoing edges | `O(V + E)` | [Course Schedule](./trees_graphs/0207_course_schedule.md) |
| Size-`K` heap | Keep only best `K` seen so far | Heap containing current best `K` | `O(N log K)` | [Kth Largest](./heaps/0215_kth_largest_element.md) |
| Frequency plus heap | Rank distinct values by counts | Frequency map, then best-`K` heap | `O(N log K)` | [Top K Frequent](./heaps/0347_top_k_frequent_elements.md) |
| Multiway merge | Several sorted sources | One next candidate per source | `O(N log K)` | [Merge K Lists](./heaps/0023_merge_k_sorted_lists.md) |
| Prefix sum counts | Continuous sums include negatives | Count of each earlier prefix | `O(N)` | [Subarray Sum](./prefix_recursion/0560_subarray_sum_equals_k.md) |
| Backtracking | Try a path without reusing choices | Current path and reversible choice | Search-tree dependent | [Word Search](./prefix_recursion/0079_word_search.md) |
| Trie path | Many words share prefixes | Child map and optional end/cached state | `O(L)` basic operation | [Implement Trie](./trie/0208_implement_trie.md) |
| Trie cached answers | Need top results after every prefix | Up to three sorted products per prefix node | Build plus `O(M)` query | [Search Suggestions](./trie/1268_search_suggestions_system.md) |
| Trie wildcard DFS | One character may match any edge | Pattern index and current Trie node | Branching worst case | [Add and Search Words](./trie/0211_design_add_and_search_words.md) |
| Trie shortest prefix | Replace by first complete root | First end marker on each word path | `O(T + S)` | [Replace Words](./trie/0648_replace_words.md) |
| Trie cached aggregate | Query a total under a prefix | Prefix total updated by `new - old` | `O(L)` update/query | [Map Sum Pairs](./trie/0677_map_sum_pairs.md) |
| One-dimensional DP | Take/skip decisions repeat | Best answer through current position | `O(N)` | [House Robber](./dynamic_programming/0198_house_robber.md) |
| Amount DP | Minimum choices build larger totals | Best answer for each amount | `O(A * C)` | [Coin Change](./dynamic_programming/0322_coin_change.md) |
| Sequence DP | Best sequence ending at each item | `dp[i]` meaning exactly | `O(N^2)` here | [Longest Increasing Subsequence](./dynamic_programming/0300_longest_increasing_subsequence.md) |

`N`, `K`, `M`, `R`, `C`, `V`, `E`, `A`, and `L` mean different things by
problem. Define every symbol when you explain complexity.

## When Two Patterns Look Similar

### Sliding Window or Prefix Sum?

Use a sliding window when moving one boundary predictably restores validity.
This often works with nonnegative values or a rule such as "no duplicates."

Use prefix sums when the answer depends on totals between positions and negative
values make boundary movement unpredictable.

### DFS or BFS?

Both can visit a connected component.

- DFS is often simplest for "visit everything in this region."
- BFS is natural for shortest unweighted distance, layers, or simultaneous spread.

Choose from the required output, not personal habit.

### Heap or Full Sort?

- Sort when you need the complete ordered collection or neighboring order.
- Use a heap when you repeatedly need one extreme or only the best `K` items.

A heap is not automatically faster. Count how much data it stores and how often
it pushes or pops.

### Backtracking or Dynamic Programming?

- Backtracking explores concrete choices and undoes them.
- DP saves answers when different paths reach the same smaller state.

Some problems use both: backtracking defines possibilities, while memoization
prevents repeated states.

### Trie or Dictionary?

- A dictionary is simplest for complete-key lookup.
- A Trie helps when many queries ask about prefixes or branch one character at a
  time.

Do not build a Trie when exact dictionary lookup already meets the requirement.

### Graph Traversal or Union-Find?

- DFS/BFS can inspect paths and full component contents.
- Union-find efficiently answers whether two nodes are already connected while
  undirected edges arrive.

Union-find does not naturally recover the actual path.

### Binary Search in Data or on an Answer?

Binary search in data compares the target with values already in sorted order.

Binary search on an answer tests a candidate using a monotonic predicate:

```text
too small, too small, too small, feasible, feasible, feasible
```

The goal is to find the boundary where the answer changes.

## The Pattern Selection Script

Say this before coding:

```text
The direct approach repeats ______, which costs ______.
I can make that work fast by storing ______ in a ______.
During the algorithm, ______ will always remain true.
That lets each input item do ______ work, so total time is ______ and extra
space is ______.
```

If you cannot fill the invariant blank, keep working on the plan before typing
the main loop.

## Mini Recognition Practice

Name the likely pattern before opening the answers.

1. Find the longest continuous range containing at most two distinct values.
2. Return the earliest minute every room is reached from several exits.
3. Find the smallest server capacity that finishes all jobs by a deadline.
4. Repeatedly return the smallest item among several sorted streams.
5. Determine whether adding an undirected cable connects nodes already connected.
6. Count continuous ranges summing to a target when values may be negative.
7. Return a deployment order from directed prerequisites.
8. Support exact words and prefix queries.

<details>
<summary>Show answers and reasoning</summary>

1. **Sliding window.** The answer is continuous, and moving `left` can remove
   old values until at most two distinct values remain.
2. **Multi-source BFS.** Put every exit in the initial queue. One BFS layer is
   one minute of equal-distance expansion.
3. **Binary search on the answer.** Capacity has a monotonic feasibility rule:
   once a capacity is large enough, every larger capacity is also feasible.
4. **Heap-based multiway merge.** Keep one current candidate from each stream;
   the heap exposes the globally smallest candidate.
5. **Union-find.** Each edge asks whether two endpoints are already in the same
   changing undirected component.
6. **Prefix-sum frequency map.** Negative values prevent reliable sliding-window
   movement, while earlier prefix `current - target` identifies every valid start.
7. **Topological sort.** In-degree records remaining prerequisites; a cycle
   prevents every node in that cycle from reaching zero.
8. **Trie.** Each character is one edge, and an end marker distinguishes a
   complete word from a prefix.

</details>

## Final Reminder

Pattern recognition proposes a plan. A correctness argument proves it. A dry run
tests the code you actually wrote. Use all three.
