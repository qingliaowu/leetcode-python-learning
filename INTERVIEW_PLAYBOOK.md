# Interview Problem-Solving Playbook

An interview is not only a test of whether the final code works. The interviewer is also evaluating how you clarify uncertainty, improve an initial idea, explain tradeoffs, and verify your own work.

Use this process for every problem in the repository.

## 1. Restate the Problem

Before solving, say the input, required output, and important rule in your own words.

```text
We receive a list of integers and need two different indexes whose values add
to the target. The problem guarantees one answer, and I should return indexes,
not values.
```

This catches misunderstandings before they become code.

## 2. Clarify What Matters

Ask only questions that could change the solution:

- Can the input be empty?
- Are duplicate values possible?
- May I modify the input?
- Does output order matter?
- Is the graph directed or undirected?
- Are intervals closed, and can a room be reused at an equal endpoint?
- What input size should the solution handle?
- Is a helper class such as `ListNode` or `Node` provided?

When the platform statement already answers a question, state the assumption instead of asking it again.

## 3. Walk Through a Small Example

Choose an example that exposes the main difficulty. Track concrete state such as a dictionary, window, queue, heap, or recursion path.

For edge cases, consider:

- empty or one-item input,
- duplicate values,
- no match or all items matching,
- a prefix that is also a complete word,
- a graph cycle,
- touching intervals,
- negative numbers,
- replacing an existing key.

## 4. Give a Baseline

Briefly describe the direct approach, even when it is slow:

```text
The direct solution checks every pair, which takes O(N^2) time. The repeated
work is searching for a complement, so I can replace that search with a hash
map lookup.
```

Do not spend most of the interview coding a baseline that clearly misses the constraints. Its purpose is to establish correctness and identify the bottleneck.

## 5. Choose the Pattern

Use clues in the question rather than memorizing code:

| Question | Recognition clue | Pattern and key invariant | Target complexity |
| --- | --- | --- | --- |
| Two Sum | Pair reaches a target | Map earlier values to indexes; current item only pairs with earlier items | `O(N)` |
| Group Anagrams | Group equivalent rearrangements | Sorted characters form one immutable group key | `O(N * K log K)` |
| Longest Substring | Longest continuous valid range | Sliding window contains no duplicate; left never moves backward | `O(N)` |
| Number of Islands | Count connected grid regions | Each DFS marks one complete component visited | `O(R * C)` |
| Course Schedule | Directed prerequisites may cycle | Queue zero-in-degree nodes; completed count proves acyclic graph | `O(V + E)` |
| Clone Graph | Deep-copy a cyclic structure | One map entry and one clone per original node | `O(V + E)` |
| Merge Intervals | Combine overlapping ranges | After sorting, compare only with the last merged interval | `O(N log N)` |
| Meeting Rooms II | Maximum simultaneous intervals | Min-heap exposes the earliest reusable room | `O(N log N)` |
| Rotated Array Search | Sorted data, rotation, logarithmic requirement | At least one half around the midpoint is sorted | `O(log N)` |
| Kth Largest | Keep only the best `k` values | Size-`k` min-heap contains the largest values seen | `O(N log K)` |
| Top K Frequent | Rank values by occurrence count | Count first; size-`k` heap keeps highest frequencies | `O(N log K)` |
| Merge K Lists | Merge several sorted streams | Heap holds one smallest available node per list | `O(N log K)` |
| Subarray Sum Equals K | Count continuous sums with negatives | Earlier prefix `current - k` creates a valid subarray | `O(N)` |
| Word Search | Explore board paths without reuse | Mark, explore, and restore each recursive choice | `O(R * C * 4^L)` |
| Implement Trie | Insert, exact lookup, prefix lookup | One node per character; end marker separates word from prefix | `O(L)` per operation |
| Search Suggestions | Top results after every typed prefix | Sorted insertion caches at most three answers per Trie node | `O(N log N + T + M)` |
| Add and Search Words | One-character wildcard | Exact letters take one edge; dot runs DFS over every child | Branching worst case |
| Replace Words | Find shortest saved prefix | First end marker reached is the shortest root | `O(T + S)` |
| Map Sum Pairs | Sum values by key prefix with updates | Each node caches a total; propagate `new - old` on update | `O(L)` insert, `O(P)` sum |

The invariant is the fact that remains true throughout the algorithm. State it before coding; it becomes a guide for both implementation and debugging.

## 6. Present the Optimized Plan

Before typing code, explain the data structure and steps in a few sentences:

```text
I will scan once and keep a map from previous value to index. For each number,
I calculate target minus that number. If the complement is in the map, I return
the saved and current indexes; otherwise I save the current number. The map only
contains earlier indexes, so I cannot reuse the same element.
```

A strong plan answers:

1. What state is stored?
2. What does one loop iteration or recursive call do?
3. When does the algorithm stop or return?
4. Why is the answer correct?
5. What are the time and space costs?

## 7. Code in Logical Blocks

Use the method signature given by the interviewer. Then code in the same order as the plan:

1. Handle a meaningful empty-input case.
2. Initialize state.
3. Traverse or recurse.
4. Update the invariant.
5. Return the result.

Use descriptive names such as `left`, `right`, `in_degree`, `running_sum`, and `needed_prefix`. Explain decisions and invariants aloud; there is no need to narrate every character you type.

## Say These Four Things Aloud

Do not leave important reasoning hidden in your head. During every solution, explicitly cover assumptions, complexity, edge cases, and testing.

### 1. Assumptions

State the facts from the question that your solution relies on:

```text
I am assuming values may repeat, but the two returned indexes must be different.
The problem guarantees one valid answer, and output pair order does not matter.
```

Other useful assumption statements include:

- "I am treating horizontal and vertical cells as connected, but not diagonals."
- "Course prerequisites are directed edges."
- "Array values are distinct, which lets me identify the sorted half."
- "A meeting ending at time `t` frees its room for one starting at time `t`."
- "I may mark the grid temporarily; I will restore it before returning."

If an assumption is not confirmed by the question, ask the interviewer instead of silently choosing it.

### 2. Complexity

Explain why the cost has that Big-O value, not only the final notation:

```text
Let N be the number of values. I scan the list once, and each hash-map lookup
is O(1) on average, so time is O(N). The map may store every value, so extra
space is O(N).
```

For multiple input dimensions, define every symbol. For example, use `V` and `E` for graph nodes and edges, `R` and `C` for grid dimensions, and `K` for heap size or number of lists.

### 3. Edge Cases

Name the cases most likely to break this specific algorithm:

```text
I want to check an empty input, a one-item input, duplicate values, and a case
where the matching pair appears at the end.
```

Avoid saying only "I would test edge cases." Choose concrete inputs and expected results. Prioritize boundaries in the code, such as `left <= right`, missing dictionary keys, equal interval endpoints, graph cycles, stale sliding-window indexes, and repeated Trie updates.

### 4. Testing the Code

Trace variable changes through the code you actually wrote:

```text
For nums [3, 2, 4] and target 6, the map is empty at index 0, then stores
3 -> 0 and 2 -> 1. At index 2, the needed value is 2, which maps to index 1,
so the function returns [1, 2]. Those values add to 6 and the indexes differ.
```

After the normal example, test one boundary case aloud. Point to the exact condition that handles it. If the code mutates shared state, confirm that the state is restored or explain why mutation is allowed.

A useful closing summary is:

```text
The normal example follows the expected path, and the duplicate and missing
cases are handled by these conditions. Time is O(...) and extra space is O(...).
```

## 8. Test Before Declaring Done

Dry-run the code itself, not just the idea. For every solution, test:

1. A normal example.
2. The smallest valid input.
3. A failure or missing-result path when allowed.
4. The special rule that makes the problem interesting.

Examples of the fourth test are duplicate `3` values in Two Sum, an old repeated character outside the sliding window, a prerequisite cycle, equal interval endpoints, equal heap values, a negative number in a prefix sum, a reused board cell, a Trie prefix that is not a word, and a Map Sum key update.

When tracing, watch for:

- off-by-one indexes,
- `<` versus `<=`,
- checking bounds before indexing,
- accidental input mutation,
- adding to visited state too late,
- forgetting to restore backtracking state,
- returning a helper or dummy node instead of the real result.

## 9. Finish With Complexity

Name what each symbol means:

```text
Let N be the number of values and K the requested rank. The heap never contains
more than K items. Each of N values performs O(log K) heap work, so time is
O(N log K) and extra space is O(K).
```

Mention important side effects, such as sorting or modifying a grid, and offer a non-mutating version if the interviewer requires one.

## A Practical Interview Timeline

For a 35-minute coding problem:

| Time | Goal |
| --- | --- |
| 0-3 minutes | Restate and clarify |
| 3-7 minutes | Example and baseline |
| 7-11 minutes | Optimized pattern, invariant, complexity |
| 11-25 minutes | Code in logical blocks |
| 25-32 minutes | Dry run and edge cases |
| 32-35 minutes | Fix issues and summarize tradeoffs |

Do not silently think for a long stretch. If stuck, return to a small example and say what information is missing from the current approach.

## Python Interview Checklist

If any syntax in this checklist feels unfamiliar, complete the [Python 3 Basics course](./python_basics/) first.

- Import standard-library tools before using them: `deque`, `heapq`, and `List`.
- Remember that `=` assigns and `==` compares.
- Use `is None` for `None` checks.
- Check an index is in bounds before reading a list or grid.
- Use `deque.popleft()` for a queue and `list.pop()` for a stack.
- Remember that `heapq` is a min-heap and only `heap[0]` is guaranteed smallest.
- Avoid mutable default arguments such as `neighbors=[]`.
- Say when a solution changes the input with `sort()` or visited markers.
- Restore shared state after recursive backtracking.
- Keep platform-required names such as `startsWith`, even when they are not standard Python style.

## How to Practice This Repository

For each problem:

1. Read only the question summary.
2. Solve aloud without opening the solution.
3. Write the baseline and optimized complexity.
4. Code for at most 30 minutes.
5. Run the file and compare it with the lesson.
6. Explain the invariant and three edge cases without notes.
7. Repeat the problem after one day and again after one week.

A problem is interview-ready when you can recognize the pattern, derive the approach rather than recite code, explain why it works, implement it without hidden gaps, and test it calmly.
