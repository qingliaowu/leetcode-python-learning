# Lesson 11: Time and Space Complexity

[Run this lesson](./11_time_and_space_complexity.py) | [Course home](./README.md)

## Goal

Understand Big-O without difficult mathematics. You will learn how to look at code and explain how its running work and extra memory grow.

## Read This in Three Easy Passes

There is no need to learn the whole page at once:

1. First pass: read from "The One Big Idea" through "See the Growth." Learn what the common time complexities look like.
2. Second pass: start at "How to Read Time Complexity From Code" and continue through "Time-Space Tradeoff."
3. Third pass: use the Python cost table, interview wording, and practice questions as a reference while solving problems.

After each pass, run the example file and explain one row of its output in your own words.

## The One Big Idea

Complexity asks:

> If the input becomes much bigger, how does the work or memory grow?

It does not try to predict exact seconds or bytes. Those depend on the computer, Python version, and data. Big-O describes the growth pattern.

Imagine searching for a name in a list:

- With 10 names, you may inspect 10.
- With 100 names, you may inspect 100.
- With 1,000 names, you may inspect 1,000.

The work grows with the number of names. We call this `O(N)` time.

## What Is N?

`N` means input size. Always say what it represents.

```text
For an array problem, N may be the number of values.
For a string problem, N may be the number of characters.
For a grid, use R rows and C columns.
For a graph, use V nodes and E edges.
```

`N` is not a Python variable unless your code creates one. It is a name used while explaining growth.

## Time Complexity

Time complexity counts how running work grows. Think "rough number of important steps," not clock time.

### O(1): Constant Time

```python
first = numbers[0]
```

This reads one item. Whether the list contains 10 or one million values, this line still does one direct lookup.

```text
N = 10       -> about 1 step
N = 1,000    -> about 1 step
N = 1,000,000 -> about 1 step
```

`O(1)` does not mean the code has exactly one operation. It means the amount of work does not grow with `N`.

Common `O(1)` average operations:

- read a list item by index,
- read or write a dictionary key,
- check membership in a set,
- append to the end of a list.

### O(log N): Cut the Work in Half

```python
while remaining > 1:
    remaining //= 2
```

Each step removes half of what remains:

```text
16 -> 8 -> 4 -> 2 -> 1
```

Only four cuts handle 16 items. Ten cuts handle about 1,000 items. Twenty cuts handle about one million items.

This is `O(log N)`. Binary search is the most common example.

You do not need to calculate logarithms during an interview. Look for repeated doubling or halving.

### O(N): Visit Every Item

```python
for number in numbers:
    print(number)
```

The loop runs once per item:

```text
10 items    -> 10 repetitions
100 items   -> 100 repetitions
1,000 items -> 1,000 repetitions
```

This is `O(N)` time. Two Sum and sliding-window solutions scan their input this way.

### O(N log N): Sort or Divide and Process

```python
numbers.sort()
```

Comparison-based sorting in Python takes `O(N log N)` time in the general case.

This grows faster than `O(N)` but much slower than `O(N²)`. Merge Intervals and Meeting Rooms II sort before scanning.

### O(N²): Compare Many Pairs

```python
for first in numbers:
    for second in numbers:
        print(first, second)
```

The outer loop runs `N` times. For each outer repetition, the inner loop also runs `N` times:

```text
N * N = N²
```

```text
10 items    -> 100 pairs
100 items   -> 10,000 pairs
1,000 items -> 1,000,000 pairs
```

This is why replacing nested pair checks with a hash map can be a large improvement.

Not every nested loop is `O(N²)`. If two pointers only move forward a total of `N` times, the overall work can still be `O(N)`.

### O(2^N): Try Every Choice Combination

Some recursive problems make two choices for every item:

```text
include item / do not include item
```

The number of paths can double with every new item. This is exponential growth and becomes large very quickly.

Backtracking problems often have exponential worst cases. Pruning invalid paths early makes actual runs faster but may not change the worst-case Big-O.

## See the Growth

The numbers below are rough operation counts, not exact runtime:

| `N` | `O(1)` | `O(log N)` | `O(N)` | `O(N log N)` | `O(N²)` |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 1 | about 4 | 10 | about 40 | 100 |
| 100 | 1 | about 7 | 100 | about 700 | 10,000 |
| 1,000 | 1 | about 10 | 1,000 | about 10,000 | 1,000,000 |
| 1,000,000 | 1 | about 20 | 1,000,000 | about 20,000,000 | 1,000,000,000,000 |

This table is the reason interviewers care about growth. A small difference at `N = 10` can become enormous at `N = 1,000,000`.

## The Usual Order From Fastest Growth to Slowest Performance

For large inputs:

```text
O(1) -> O(log N) -> O(N) -> O(N log N) -> O(N²) -> O(2^N)
```

Earlier is usually more scalable. This does not mean an `O(N)` solution is always better in real life than every `O(N log N)` solution. Big-O ignores constants and small-input details.

## Ignore Constants and Smaller Terms

Big-O keeps the part that grows fastest.

```text
O(2N) becomes O(N)
O(N + 10) becomes O(N)
O(N² + N) becomes O(N²)
```

Why? When `N` becomes very large, multiplying by two or adding ten does not change the growth category. `N²` eventually dominates `N`.

Do not erase different input variables:

```text
O(N + M)
```

If `N` and `M` describe two independent inputs, keep both.

## How to Read Time Complexity From Code

### Rule 1: One fixed operation is O(1)

```python
answer = numbers[0]
```

### Rule 2: One full loop is usually O(N)

```python
for number in numbers:
    total += number
```

### Rule 3: Nested full loops multiply

```python
for left in numbers:
    for right in numbers:
        check(left, right)
```

`N` outer repetitions times `N` inner repetitions gives `O(N²)`.

### Rule 4: Consecutive loops add, then simplify

```python
for number in numbers:
    work(number)

for number in numbers:
    more_work(number)
```

`O(N) + O(N) = O(2N)`, simplified to `O(N)`.

### Rule 5: Repeated halving is O(log N)

```python
while left <= right:
    middle = (left + right) // 2
    # Keep only one half.
```

### Rule 6: Sorting is usually O(N log N)

```python
sorted_numbers = sorted(numbers)
```

If an `O(N)` scan follows sorting, total time is:

```text
O(N log N) + O(N) = O(N log N)
```

Keep the fastest-growing term.

### Rule 7: For recursion, count calls and work per call

Ask:

1. How many recursive calls can one call create?
2. How deep can calls go?
3. How much work happens inside one call?

A tree DFS that visits each node once is `O(N)`. A backtracking search that branches four ways for `L` levels may be `O(4^L)` in the worst case.

## Space Complexity

Space complexity asks:

> How much extra memory grows as the input grows?

Usually, interviews ask for auxiliary space: memory created by the algorithm, not the input that was already provided.

Say what you are counting. Sometimes required output is also excluded, so clarify when it matters.

### O(1) Extra Space

```python
left = 0
right = len(numbers) - 1
best = 0
```

Only a few variables are stored. Their count does not grow with the input, so extra space is `O(1)`.

### O(N) Extra Space

```python
seen = set()

for number in numbers:
    seen.add(number)
```

The set may store all `N` values, so extra space is `O(N)`.

### O(K) Extra Space

```python
min_heap = []
```

If the algorithm deliberately keeps at most `K` heap items, space is `O(K)`, not `O(N)`. Kth Largest uses this idea.

### Recursion Uses Stack Space

Every unfinished recursive call needs memory on the call stack.

```text
depth 1 -> one call stored
depth N -> up to N calls stored
```

A recursive linked-list traversal can use `O(N)` stack space even if it creates no list, dictionary, or set.

### Modifying Input Can Save Extra Space

Number of Islands changes visited `"1"` cells to `"0"` instead of creating a visited set. It still may use `O(R * C)` stack space in the worst case, but the grid itself stores visited state.

Always say when your solution modifies the input.

## Time-Space Tradeoff

Faster code often stores more information.

Two Sum examples:

- Nested loops: `O(N²)` time and `O(1)` extra space.
- Hash map: `O(N)` time and `O(N)` extra space.

The hash map spends memory to avoid repeated searching. This is a time-space tradeoff.

## Common Python Operation Costs

These are the usual interview assumptions:

| Python operation | Typical time |
| --- | --- |
| `items[index]` | `O(1)` |
| `items.append(value)` | `O(1)` average |
| `items.pop()` from end | `O(1)` |
| `items.pop(0)` from front | `O(N)` because items shift |
| `value in a_list` | `O(N)` |
| `key in a_dict` | `O(1)` average |
| `value in a_set` | `O(1)` average |
| `dict[key] = value` | `O(1)` average |
| `sorted(items)` | `O(N log N)` |
| `text[start:stop]` | `O(K)` for a slice of length `K` |
| `deque.popleft()` | `O(1)` |
| `heapq.heappush` / `heappop` | `O(log K)` for heap size `K` |

Dictionary and set operations are `O(1)` on average, not an absolute guarantee for every possible internal collision.

## Complexity in This Repository

| Problem pattern | Time | Extra space | Plain-English reason |
| --- | --- | --- | --- |
| Two Sum | `O(N)` | `O(N)` | Scan once; map may remember every value |
| Sliding window | `O(N)` | `O(U)` | Right and left only move forward; map stores unique characters |
| Decode String | Output-dependent | `O(N + D)` | Read encoded text and store paused plus decoded characters |
| TimeMap get | `O(log M)` | Stored history | Binary search one key's M timestamped values |
| LRU Cache operation | `O(1)` average | `O(C)` total cache | Map lookup and a fixed number of linked-list pointer changes |
| Grid DFS | `O(R * C)` | `O(R * C)` worst case | Visit each cell; stack may hold a large island |
| Course Schedule | `O(V + E)` | `O(V + E)` | Process each course and prerequisite edge once |
| Merge Intervals | `O(N log N)` | `O(N)` output | Sort, then scan once |
| Binary Search | `O(log N)` | `O(1)` | Keep half the sorted range and store only indexes |
| Rotated binary search | `O(log N)` | `O(1)` | Discard half each step; keep only indexes |
| Size-K heap | `O(N log K)` | `O(K)` | N items each do heap work on at most K values |
| Prefix sum map | `O(N)` | `O(N)` | Scan once; map may store each running sum |
| House Robber | `O(N)` | `O(1)` | Process each house; keep only two previous answers |
| Coin Change | `O(A * C)` | `O(A)` | Try C coins for each amount; save one answer per amount |
| Longest Increasing Subsequence DP | `O(N²)` | `O(N)` | Each index checks earlier indexes; save one answer per index |
| Trie operation | `O(L)` | Depends on stored nodes | Follow one node for every input character |
| Word Search | `O(R * C * 4^L)` worst case | `O(L)` | Try starts and branching paths; recursion depth is word length |

Letters can mean different things in different problems. Always define them before using the formula.

## How to Explain Complexity Aloud

Use this four-sentence pattern:

```text
Let N be the number of input values.
I visit each value once, and each dictionary lookup is O(1) on average.
Therefore, time complexity is O(N).
The dictionary may store all N values, so extra space is O(N).
```

For a heap:

```text
Let N be the number of values and K the requested rank.
The heap stores at most K items, and each push or pop costs O(log K).
I process N values, so time is O(N log K) and extra space is O(K).
```

Do not only say "It is linear." Explain what is visited, how often, and what is stored.

## Practice: Name the Time Complexity

### Example 1

```python
return numbers[0]
```

Answer: `O(1)`. One direct access does not grow with list length.

### Example 2

```python
for number in numbers:
    print(number)
```

Answer: `O(N)`. Every number is visited once.

### Example 3

```python
for first in numbers:
    for second in numbers:
        print(first, second)
```

Answer: `O(N²)`. There are `N * N` ordered pairs.

### Example 4

```python
numbers.sort()
for number in numbers:
    print(number)
```

Answer: `O(N log N)`. Sorting dominates the later `O(N)` loop.

### Example 5

```python
while size > 1:
    size //= 2
```

Answer: `O(log N)`. The remaining size is cut in half each time.

## Practice: Name the Extra Space

### Example 1

```python
total = 0
for number in numbers:
    total += number
```

Answer: `O(1)` extra space. Only one total and one loop variable are needed, regardless of `N`.

### Example 2

```python
copied = []
for number in numbers:
    copied.append(number)
```

Answer: `O(N)` extra space. The new list grows to contain `N` items.

### Example 3

```python
def visit(node):
    if node is None:
        return
    visit(node.next)
```

Answer: `O(N)` call-stack space in the worst case for a chain of `N` nodes.

## Common Beginner Mistakes

- Measuring one run in seconds and calling that Big-O.
- Calling every loop `O(N)` without asking how many total iterations occur.
- Calling every nested loop `O(N²)` even when pointers never restart.
- Forgetting that sorting adds `O(N log N)` time.
- Ignoring a dictionary, set, queue, stack, heap, or recursion stack in space analysis.
- Saying `O(N)` without defining `N`.
- Multiplying consecutive loops instead of adding them.
- Counting required input memory as newly created auxiliary space without explaining that choice.
- Thinking `O(1)` means exactly one machine instruction.

## Final Checklist

When asked for complexity:

1. Define each input-size letter.
2. Find the operation that repeats.
3. Count how often it can repeat.
4. Include sorting, helper calls, and recursive branches.
5. List memory that can grow: collections, output, and call stack.
6. Simplify constants and smaller terms.
7. Explain the reason in plain English.

You do not need advanced math. You need a clear count of what grows.
