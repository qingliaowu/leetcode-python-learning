# 198. House Robber

[LeetCode problem](https://leetcode.com/problems/house-robber/) | [Python solution](./0198_house_robber.py) | [DP guide](./README.md)

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

## Interview Explanation

> At each house I either take it, which adds its money to the best result two houses back, or skip it, which keeps the best result through the previous house. I store only those two earlier answers. Each house is processed once, so time is `O(N)` and extra space is `O(1)`.

## Test Aloud

For `[1, 2, 3, 1]`, say:

```text
The best totals after each house are 1, 2, 4, and 4. At the third house,
taking 3 plus the best two houses back gives 4. The final house is skipped
because taking it would also give only 3. I return 4.
```
