# 300. Longest Increasing Subsequence

[LeetCode problem](https://leetcode.com/problems/longest-increasing-subsequence/) | [Python solution](./0300_longest_increasing_subsequence.py) | [DP guide](./README.md)

## What the Question Asks

Return the length of the longest strictly increasing subsequence.

- A subsequence keeps the original order but may skip values.
- Strictly increasing means every next value must be larger, not equal.
- Return the length, not the subsequence itself.

```text
[10, 9, 2, 5, 3, 7, 101, 18]
one longest subsequence is [2, 3, 7, 18]
answer = 4
```

## Substring Versus Subsequence

A substring or subarray must be continuous. A subsequence may skip elements.

```text
Original:    2, 5, 3, 7
Subsequence: 2,    3, 7
```

The order remains the same.

## The DP State

Define:

```text
dp[i] = the longest increasing subsequence that ends exactly at index i
```

"Ends exactly at index `i`" is important. It gives each state a clear final value that earlier states can connect to.

## Base Case

```python
dp = [1] * len(nums)
```

Every single number forms an increasing subsequence of length `1`, even if it cannot connect to an earlier value.

## Transition

For each `current` index, inspect every earlier `previous` index.

If:

```python
nums[previous] < nums[current]
```

then the current value can extend a subsequence ending at `previous`:

```text
candidate length = dp[previous] + 1
```

Keep the largest candidate:

```python
dp[current] = max(dp[current], dp[previous] + 1)
```

## Why the Final Answer Is max(dp)

The longest increasing subsequence may end before the final array index. `dp[-1]` only describes subsequences ending at the last value.

Therefore:

```python
return max(dp)
```

## Python Used Here

```python
for current in range(len(nums)):
    for previous in range(current):
```

For each current position, `range(current)` produces all earlier indexes from `0` through `current - 1`.

```python
if not nums:
    return 0
```

An empty list is falsy, so this handles it before calling `max` on an empty `dp` list.

## Dry Run

For `[2, 5, 3, 7]`:

| Current value | Earlier smaller endings | Best subsequence ending here | `dp` value |
| ---: | --- | --- | ---: |
| 2 | none | `[2]` | 1 |
| 5 | 2 | `[2, 5]` | 2 |
| 3 | 2 | `[2, 3]` | 2 |
| 7 | 2, 5, 3 | `[2, 5, 7]` or `[2, 3, 7]` | 3 |

Final `dp` is `[1, 2, 2, 3]`, so the answer is `3`.

For equal values `[7, 7, 7]`, no earlier value is strictly smaller. Every state remains `1`.

## Why It Is Correct

Any increasing subsequence ending at `current` either contains only the current value or has some earlier final index `previous` with a smaller value. The algorithm checks every possible earlier ending and extends its already best subsequence. Therefore, it finds the best subsequence ending at every index.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the number of values.

- Time: `O(N²)` because every current index may inspect every earlier index.
- Extra space: `O(N)` for one `dp` value per array index.

There is an `O(N log N)` solution using a `tails` list and binary search. It is an excellent follow-up optimization, but the `O(N²)` version here makes the dynamic-programming state and recurrence easier to learn and is accepted for the standard problem constraints.

## Edge Cases

- Empty list: return `0`.
- One value: return `1`.
- All values equal: return `1` because increase must be strict.
- Strictly decreasing values: return `1`.
- Strictly increasing values: return `N`.
- The best subsequence may not end at the final index.

## Common Mistakes

- Confusing subsequence with a continuous subarray.
- Using `<=` and incorrectly allowing equal values.
- Initializing states to zero instead of one.
- Returning `dp[-1]` instead of `max(dp)`.
- Checking later indexes and breaking the calculation order.
- Calling the nested loops `O(N)` instead of `O(N²)`.

## Interview Explanation

> I define `dp[i]` as the longest increasing subsequence ending exactly at index `i`. Every state starts at one. For each index, I inspect earlier smaller values and extend their best saved lengths. I return the maximum state. The nested scan takes `O(N²)` time and the table uses `O(N)` space.

## Follow-up: O(N log N)

If the interviewer asks for faster time, describe a `tails` list where `tails[length - 1]` stores the smallest ending value found for an increasing subsequence of that length. Use binary search to replace the first tail greater than or equal to each number. The length of `tails` is the LIS length.

That optimized list does not necessarily contain an actual subsequence, so explain its invariant carefully. Learn the `O(N²)` DP first, then practice the binary-search follow-up separately.

## Test Aloud

For `[7, 7, 7]`, say:

```text
Every state begins at 1. The strict comparison is previous value less than
current value, so equal sevens never extend one another. max(dp) is 1.
```
