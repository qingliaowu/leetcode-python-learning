# 560. Subarray Sum Equals K

[LeetCode problem](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python solution](./0560_subarray_sum_equals_k.py)

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

## Complexity

- Time: `O(N)` average because each element performs constant-time dictionary work.
- Space: `O(N)` for prefix sums in the worst case.

## Common Mistakes

- Using a sliding window even though negative values can decrease the sum.
- Forgetting the initial `{0: 1}` entry.
- Storing only whether a prefix occurred rather than how many times.
- Looking up `k - running_sum` instead of `running_sum - k`.
- Recording the current prefix before counting.

## Interview Explanation

> A subarray sum is the difference between two prefix sums. At each position, I need an earlier prefix equal to the current sum minus `k`. A hash map stores how many times each earlier sum occurred, so I can count all matching starts in constant average time and finish in `O(N)`.
