# 300. Longest Increasing Subsequence

[LeetCode problem](https://leetcode.com/problems/longest-increasing-subsequence/) | [Python solution](./0300_longest_increasing_subsequence.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

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

## Assumptions to Say Aloud

- Increasing means strictly increasing, so equal values cannot extend a
  subsequence.
- A subsequence preserves order but does not need to be continuous.
- The answer is a length, not the sequence itself.
- This lesson intentionally uses the beginner-friendly `O(N^2)` DP solution.

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

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Can you improve the time to `O(N log N)`? | Maintain `tails`, where each position stores the smallest ending value for a subsequence of that length, and use binary search to replace the first value greater than or equal to the current number. |
| How would you return an actual subsequence? | Store each index's predecessor and track the ending index of the best length, then follow predecessors backward and reverse the result. |
| What if the subsequence may be non-decreasing? | Allow equal values. In the quadratic DP use `<=`; in the `tails` method replace the first value strictly greater than the current number. |
| How would you count how many longest subsequences exist? | Store both the best length and the number of ways to reach that length at every index, combining counts when equal best lengths are found. |
| What if numbers arrive one at a time? | Maintain the `tails` structure as the stream arrives. Each new value updates it in `O(log N)` and its length gives the current LIS length. |

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

## Check Your Understanding

Try each question before opening its answer. Say what `dp[i]` means before calculating any values.

### Question 1: Find One Increasing Subsequence

What is the LIS length for `[10, 9, 2, 5, 3, 7, 101, 18]`? Give one valid subsequence of that length.

<details>
<summary>Show answer and explanation</summary>

**Answer:** The length is `4`. Examples include `[2, 3, 7, 18]` and `[2, 5, 7, 101]`.

For each index, `dp[i]` means the longest increasing subsequence ending exactly at that value. Value `7` can extend a subsequence ending at `2`, `5`, or `3`. Value `18` can then extend a length-three subsequence ending at `7`, producing length four.

The answer is `max(dp)`, not necessarily a state chosen in advance, because the best subsequence may end at any index.

**Complexity:** The beginner DP uses `O(N^2)` time and `O(N)` extra space.

**Edge case:** Equal values do not extend a strictly increasing subsequence.

</details>

### Question 2: Longest Non-Decreasing Subsequence

Change the rule so equal neighboring choices are allowed. Return the longest non-decreasing subsequence length. For `[1, 2, 2, 1]`, return `3` for `[1, 2, 2]`.

<details>
<summary>Show answer and detailed solution</summary>

```python
def longest_non_decreasing_subsequence(nums: list[int]) -> int:
    if not nums:
        return 0

    dp = [1] * len(nums)

    for current in range(len(nums)):
        for previous in range(current):
            if nums[previous] <= nums[current]:
                dp[current] = max(dp[current], dp[previous] + 1)

    return max(dp)
```

The state remains “best valid subsequence ending exactly at `current`.” The only transition change is `<=` instead of `<`, because an equal current value may now extend the earlier sequence.

Every state starts at one because a value by itself is a valid non-decreasing subsequence.

**Complexity:** `O(N^2)` time and `O(N)` extra space.

**Tests:** `[1, 2, 2, 1]` returns `3`; `[7, 7, 7]` now returns `3`; an empty list returns `0`.

</details>
