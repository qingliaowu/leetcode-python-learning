# 560. Subarray Sum Equals K

[LeetCode problem](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python solution](./0560_subarray_sum_equals_k.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Count continuous, non-empty subarrays whose values sum to `k`.

```text
nums = [1, 1, 1], k = 2
valid subarrays: indexes [0..1] and [1..2]
answer = 2
```

Negative values are allowed, so a normal grow-and-shrink sliding window does not work reliably.

## Prefix Sum Idea

A prefix sum is the total from the start through the current position.

If:

```text
current prefix sum - earlier prefix sum = k
```

then the values between those two prefix positions sum to `k`. Rearrange the equation:

```text
earlier prefix sum = current prefix sum - k
```

Therefore, at each position, look up how many earlier prefixes equal `running_sum - k`.

## Python Used Here

```python
prefix_counts = {0: 1}
```

This dictionary literal starts with key `0` having count `1`.

```python
answer += prefix_counts.get(needed_prefix, 0)
```

`+=` adds to the current answer. `get` returns zero when the needed sum has not appeared.

Multiple earlier positions can have the same prefix sum, especially when zeros or negative numbers exist. Store a count, not just a boolean.

## Why `{0: 1}` Is Necessary

The initial entry represents one empty prefix before index `0`.

If the running sum itself equals `k`, then:

```text
needed prefix = running_sum - k = 0
```

The initial zero lets the algorithm count a valid subarray that starts at index `0`.

## Step-by-Step Approach

1. Set running sum and answer to zero.
2. Start prefix counts with `{0: 1}`.
3. Add each number to the running sum.
4. Calculate `needed_prefix = running_sum - k`.
5. Add the number of earlier needed prefixes to the answer.
6. Record the current running sum after counting.
7. Return the answer.

Record after counting so the current position is not incorrectly used as an earlier prefix for an empty subarray.

## Dry Run

For `[1, 1, 1]`, `k = 2`:

| Number | Running sum | Needed | Earlier count | Answer | Counts after |
| ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 1 | -1 | 0 | 0 | `{0:1, 1:1}` |
| 1 | 2 | 0 | 1 | 1 | add `2:1` |
| 1 | 3 | 1 | 1 | 2 | add `3:1` |

For `[1, -1, 0]` and `k = 0`, prefix sum `0` appears multiple times. Its stored count lets the algorithm count all three valid subarrays.

## Why It Is Correct

For a subarray ending at the current index to sum to `k`, its earlier prefix
must equal `running_sum - k`. `prefix_counts` stores how many such earlier
prefixes exist, so adding that count includes every valid start for the current
end. The current prefix is saved only afterward, which prevents counting an
empty subarray. Summing this contribution at every ending index counts every
valid continuous subarray exactly once.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Time: `O(N)` average because each element performs constant-time dictionary work.
- Space: `O(N)` for prefix sums in the worst case.

## Assumptions to Say Aloud

- A subarray is continuous and may contain negative values or zeros.
- The answer is the number of index ranges, not the ranges themselves.
- Different ranges count separately even when they contain equal values.
- The input list is not modified.

## Edge Cases

- An empty list.
- `k = 0`.
- Negative numbers, which prevent a normal sliding-window solution.
- Several zero-sum ranges end at the same index.
- The entire array is one valid subarray.

## Common Mistakes

- Using a sliding window even though negative values can decrease the sum.
- Forgetting the initial `{0: 1}` entry.
- Storing only whether a prefix occurred rather than how many times.
- Looking up `k - running_sum` instead of `running_sum - k`.
- Recording the current prefix before counting.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Return the actual subarrays instead of only the count. | Map each prefix sum to all indexes where it occurred, then emit ranges from each matching earlier index. Output can be `O(N²)`. |
| Find the longest subarray summing to `K`. | Store the earliest index for each prefix sum and maximize the distance to an earlier `current_sum - K`. |
| All values are positive. | A sliding window can grow and shrink monotonically in `O(N)` time with `O(1)` extra space. |
| Answer many different `K` queries for the same array. | Prefix sums help calculate any one range quickly, but counting all ranges for many targets needs extra preprocessing or `O(N²)` pair sums. |
| Process numbers as a stream. | Keep the running sum, prior prefix counts, and answer; each new number adds the count of new valid subarrays ending there. |

## Interview Explanation

> A subarray sum is the difference between two prefix sums. At each position, I need an earlier prefix equal to the current sum minus `k`. A hash map stores how many times each earlier sum occurred, so I can count all matching starts in constant average time and finish in `O(N)`.

## Test Aloud

For `[1, -1, 0]` and `k = 0`, prefix sum `0` is initially recorded once.
After `1`, no range is added. After `-1`, the running sum is `0`, so one range
is found. At the final `0`, prefix sum `0` has appeared twice, adding two more
ranges. The result is `3`. An empty list performs no updates and returns `0`.

## Check Your Understanding

Try each question before opening its answer. Write the running prefix sum after every number.

### Question 1: Count Overlapping Answers

How many subarrays sum to `1` in `nums = [1, -1, 1]`? List them by index range.

<details>
<summary>Show answer and explanation</summary>

**Answer:** `3` subarrays: indexes `0..0`, `0..2`, and `2..2`.

The running prefix sums are `1`, `0`, and `1`. At each position, the algorithm looks for an earlier prefix equal to `running_sum - 1`. The initial prefix sum `0` before the array is essential: it allows ranges beginning at index `0` to be counted.

The prefix sum `0` occurs twice by the time the final `1` is read, so that final position completes two valid subarrays. This is why the map stores frequencies rather than only whether a sum appeared.

**Complexity:** `O(N)` average time and `O(N)` extra space.

**Edge case:** Negative numbers are allowed, so a normal shrinking sliding window is not reliable.

</details>

### Question 2: Find the Longest Matching Subarray

Return the length of the longest subarray summing to `k`. For `[1, -1, 5, -2, 3]` and `k = 3`, return `4` for indexes `0..3`.

<details>
<summary>Show answer and detailed solution</summary>

```python
def longest_subarray_sum(nums: list[int], k: int) -> int:
    earliest_index = {0: -1}
    running_sum = 0
    best = 0

    for index, number in enumerate(nums):
        running_sum += number
        needed = running_sum - k

        if needed in earliest_index:
            length = index - earliest_index[needed]
            best = max(best, length)

        if running_sum not in earliest_index:
            earliest_index[running_sum] = index

    return best
```

If two prefix sums differ by `k`, the elements between them sum to `k`. To maximize the range length, the dictionary keeps only the earliest index for each prefix sum. Replacing it with a later index could only create a shorter future range.

The entry `0: -1` represents the empty prefix before index `0`.

**Complexity:** `O(N)` average time and `O(N)` extra space.

**Tests:** The example returns `4`; `longest_subarray_sum([], 0)` returns `0`.

</details>
