# 1. Two Sum

[LeetCode problem](https://leetcode.com/problems/two-sum/) | [Python solution](./0001_two_sum.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Given a list of integers and a target, return the indexes of two different elements whose values add to the target. The problem guarantees exactly one valid answer.

```text
nums = [2, 7, 11, 15], target = 9
answer = [0, 1] because nums[0] + nums[1] = 2 + 7 = 9
```

The answer contains indexes, not the numbers themselves.

## Python Used Here

`enumerate` gives an index and value together:

```python
for index, number in enumerate([2, 7]):
    print(index, number)
# 0 2
# 1 7
```

A dictionary stores key-value pairs:

```python
seen = {}
seen[2] = 0

if 2 in seen:
    print(seen[2])  # 0
```

Here, the dictionary key is a number from `nums`, and its value is that number's index.

## From Brute Force to a Hash Map

A direct solution tries every pair. With `N` numbers, that can take `O(N^2)` time.

Instead, when the current number is `number`, calculate its required partner:

```text
needed = target - number
```

If `needed` appeared earlier, the answer is ready. A dictionary checks this in `O(1)` average time.

## Step-by-Step Approach

1. Create an empty dictionary named `seen`.
2. Visit each number with its index.
3. Calculate `needed = target - number`.
4. If `needed` is already in `seen`, return its saved index and the current index.
5. Otherwise, save the current number and index for later.

Check before saving. This prevents one element from being paired with itself, while still allowing two equal values at different indexes.

## Dry Run

For `[3, 2, 4]` with target `6`:

| Index | Number | Needed | `seen` before check | Action |
| ---: | ---: | ---: | --- | --- |
| 0 | 3 | 3 | `{}` | Save `3: 0` |
| 1 | 2 | 4 | `{3: 0}` | Save `2: 1` |
| 2 | 4 | 2 | `{3: 0, 2: 1}` | Return `[1, 2]` |

For `[3, 3]`, the first `3` is saved. The second `3` finds it, so the answer correctly uses two different indexes.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Time: `O(N)` because the list is scanned once.
- Space: `O(N)` in the worst case for the dictionary.

## Common Mistakes

- Returning values instead of indexes.
- Saving the current value before checking and accidentally using one index twice.
- Looking for `number - target` instead of `target - number`.
- Using nested loops without discussing the `O(N^2)` cost.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| What if the input is already sorted? | Use left and right pointers. Move the pointer whose value makes the sum too small or too large. Time stays `O(N)` and extra space becomes `O(1)`. |
| What if you must return every unique pair? | Continue after a match, store normalized value pairs in a set, and define how duplicate indexes or values should be handled. |
| What if numbers arrive as a stream? | Keep the same complement map. Each new number can pair only with values already seen. |
| What if the same array receives many target queries? | Discuss sorting once for repeated two-pointer queries or precomputing pair sums, trading preprocessing time and memory for faster queries. |

## Interview Explanation

> As I scan the array, I keep a hash map from each previous value to its index. For the current value, I compute the complement needed to reach the target. If that complement is already stored, I return the two indexes. This uses linear time and linear extra space.

## Check Your Understanding

Try each question before opening its answer. Say the approach, complexity, and one edge case aloud.

### Question 1: Trace Duplicate Values

For `nums = [3, 3]` and `target = 6`, which indexes are returned? Why does the algorithm not reuse index `0` twice?

<details>
<summary>Show answer and explanation</summary>

**Answer:** `[0, 1]`.

At index `0`, the needed complement is `3`, but the map is still empty. The algorithm then stores `3 -> 0`. At index `1`, the complement is again `3`, and the map contains index `0`, so the two different indexes form the answer.

Checking before storing the current number prevents one element from matching itself. Duplicate values are still allowed because they occupy different indexes.

**Complexity:** `O(N)` time and `O(N)` extra space in the worst case.

**Edge case:** An input with fewer than two numbers cannot contain a valid pair.

</details>

### Question 2: Does Any Pair Exist?

Write a function that returns `True` when any two different elements add to `target`. It does not need to return their indexes.

<details>
<summary>Show answer and detailed solution</summary>

```python
def has_pair_with_sum(nums: list[int], target: int) -> bool:
    seen = set()

    for number in nums:
        complement = target - number
        if complement in seen:
            return True
        seen.add(number)

    return False
```

The set stores values from earlier indexes. For each new number, the function asks whether the value needed to complete the target has already appeared. It checks first and inserts second, so one index is never used twice.

For `[4, 1, 7]` and target `8`, the function stores `4`, then `1`. When it reaches `7`, it finds the needed `1` and returns `True`.

**Complexity:** `O(N)` average time and `O(N)` extra space.

**Tests:** `has_pair_with_sum([3, 3], 6)` is `True`; `has_pair_with_sum([3], 6)` is `False`.

</details>
