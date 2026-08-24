# 198. House Robber

[LeetCode problem](https://leetcode.com/problems/house-robber/) | [Python solution](./0198_house_robber.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Each number is the money in one house. You cannot choose two neighboring houses. Return the largest total you can take.

```text
houses = [1, 2, 3, 1]
choose 1 and 3
answer = 4
```

You are choosing values, not returning their indexes.

## Start With the Decision

At each house, there are two choices:

1. Take this house. Then the previous house cannot be taken.
2. Skip this house. Keep the best answer already found.

This creates the recurrence:

```text
best through current house = max(
    best through two houses back + current money,
    best through previous house
)
```

## The DP State

Imagine a list `dp` where:

```text
dp[i] = the most money possible using houses from 0 through i
```

Then:

```text
dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
```

- `dp[i - 2] + nums[i]` means take the current house.
- `dp[i - 1]` means skip the current house.

## Why the Code Uses Two Variables

The recurrence only reads the previous two answers. The entire `dp` list is unnecessary.

```python
best_two_back = 0
best_one_back = 0
```

For each house:

```python
take_current = best_two_back + money
skip_current = best_one_back
best_current = max(take_current, skip_current)
```

Then move the saved answers forward.

This is still dynamic programming. The saved table has simply been compressed from `O(N)` values to two values.

## Python Used Here

```python
best_current = max(take_current, skip_current)
```

`max` returns the larger value.

The update order matters:

```python
best_two_back = best_one_back
best_one_back = best_current
```

`best_current` is calculated before either old value changes.

## Dry Run

For `[2, 7, 9, 3, 1]`:

| House money | Take current | Skip current | Best current |
| ---: | ---: | ---: | ---: |
| 2 | `0 + 2 = 2` | 0 | 2 |
| 7 | `0 + 7 = 7` | 2 | 7 |
| 9 | `2 + 9 = 11` | 7 | 11 |
| 3 | `7 + 3 = 10` | 11 | 11 |
| 1 | `11 + 1 = 12` | 11 | 12 |

The answer is `12`, from houses containing `2`, `9`, and `1`.

## Why It Is Correct

Every valid best solution through the current house must do exactly one of two things:

- include the current house, forcing it to combine with the best answer two houses back, or
- exclude the current house, leaving the best answer through the previous house.

Taking the larger result covers every valid possibility.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the number of houses.

- Time: `O(N)` because each house is processed once.
- Extra space: `O(1)` because only a fixed number of variables is stored.

An explicit `dp` list would use `O(N)` space. The two-variable version keeps the same time and answer with less memory.

## Edge Cases

- Empty list: return `0`.
- One house: take its value.
- Two houses: take the larger value.
- Values where skipping a large middle section is best.
- `[2, 1, 1, 2]`: answer is `4`, not `3`.

## Common Mistakes

- Adding every other index without considering a better changing pattern.
- Taking the current house plus the previous answer, which may include an adjacent house.
- Updating the previous variables before calculating `best_current`.
- Returning the last house value instead of the best result.
- Building a full table without explaining that only two states are needed.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| What if the houses form a circle? | The first and last houses cannot both be used. Solve twice: once without the last house and once without the first, then take the larger answer. |
| How would you return the indexes of the robbed houses? | Keep the full DP table and backtrack through the take-or-skip decisions. This changes extra space from `O(1)` to `O(N)`. |
| What if house values can be negative? | Allow skipping every house, so the answer never has to drop below zero. The current zero-valued base state already supports that rule. |
| What if robbing a house blocks the next `D` houses? | Taking index `i` adds its value to the best result at index `i - D - 1`; skipping keeps the result from `i - 1`. |
| What if the houses are arranged as a binary tree? | Use tree DP. For each node, return two values: the best total when taking that node and the best total when skipping it. |

## Interview Explanation

> At each house I either take it, which adds its money to the best result two houses back, or skip it, which keeps the best result through the previous house. I store only those two earlier answers. Each house is processed once, so time is `O(N)` and extra space is `O(1)`.

## Test Aloud

For `[1, 2, 3, 1]`, say:

```text
The best totals after each house are 1, 2, 4, and 4. At the third house,
taking 3 plus the best two houses back gives 4. The final house is skipped
because taking it would also give only 3. I return 4.
```

## Check Your Understanding

Try each question before opening its answer. At every house, calculate both “take” and “skip.”

### Question 1: Trace the DP Decisions

What is the maximum amount for houses `[2, 7, 9, 3, 1]`? Give one set of values that produces it.

<details>
<summary>Show answer and explanation</summary>

**Answer:** `12`, produced by taking values `2`, `9`, and `1`.

The best totals through each position are `2`, `7`, `11`, `11`, and `12`. At value `9`, taking it adds to the best result two positions back: `2 + 9 = 11`. At value `3`, taking gives `7 + 3 = 10`, so skipping keeps `11`. At value `1`, taking gives `11 + 1 = 12`.

The saved state is not “money from the previous house.” It is the best legal total through that earlier position.

**Complexity:** `O(N)` time and `O(1)` extra space with two rolling values.

**Edge case:** An empty list returns `0`; one house returns that house's value under the usual non-negative constraint.

</details>

### Question 2: Houses in a Circle

Solve the version where the first and last houses are adjacent. For `[2, 3, 2]`, the answer is `3` because the two `2` values cannot both be taken.

<details>
<summary>Show answer and detailed solution</summary>

```python
def rob_circular_houses(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def rob_range(start: int, end: int) -> int:
        best_two_back = 0
        best_one_back = 0

        for index in range(start, end):
            take = best_two_back + nums[index]
            skip = best_one_back
            best_current = max(take, skip)
            best_two_back = best_one_back
            best_one_back = best_current

        return best_one_back

    skip_last = rob_range(0, len(nums) - 1)
    skip_first = rob_range(1, len(nums))
    return max(skip_last, skip_first)
```

Every valid answer must exclude at least one of the two adjacent endpoint houses. The function therefore solves two ordinary linear cases: indexes `0` through `N - 2`, and indexes `1` through `N - 1`. The better result covers every legal possibility.

The one-house case is handled separately because excluding either endpoint would otherwise leave an empty range.

**Complexity:** `O(N)` time and `O(1)` extra space.

**Tests:** `[2, 3, 2]` returns `3`; `[1, 2, 3, 1]` returns `4`; `[5]` returns `5`.

</details>
