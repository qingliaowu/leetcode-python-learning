# 739. Daily Temperatures

[LeetCode problem](https://leetcode.com/problems/daily-temperatures/) | [Python solution](./0739_daily_temperatures.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

For every daily temperature, return how many days pass before a strictly warmer
temperature. Return `0` when no warmer future day exists.

```text
temperatures: [73, 74, 75, 71, 69, 72, 76, 73]
waits:        [ 1,  1,  4,  2,  1,  1,  0,  0]
```

## Recognize the Pattern

Look for phrases such as:

- next greater or next smaller value,
- first future item that beats the current item,
- nearest boundary to the left or right.

These often use a **monotonic stack**. The stack keeps unresolved items in a
useful sorted order while the scan moves once through the input.

## Start With a Direct Approach

For each day, scan right until a warmer day appears. In a decreasing list, every
day scans most of the remaining list, so time becomes `O(N^2)`.

The faster idea reverses the question:

```text
Instead of asking each old day to search the future,
let today's temperature resolve all colder days waiting on the stack.
```

## What the Stack Stores

Store **indexes**, not temperatures.

An index gives both pieces of needed information:

```python
temperatures[index]  # the temperature to compare
day - index          # how long that day waited
```

The stack contains days that have not found a warmer future day yet.

## The Monotonic Invariant

From the bottom to the top, unresolved temperatures are non-increasing.

When today's temperature is warmer than the top day:

1. Pop that colder day.
2. Record the index distance.
3. Continue because today may resolve several colder days.

Equal temperatures stay on the stack because the question requires **strictly
warmer**, not warmer or equal.

## Step by Step

1. Create an answer list of zeros.
2. Create an empty stack of unresolved indexes.
3. Scan each `day, temperature` from left to right.
4. While the stack top is colder, pop it and save `day - colder_day`.
5. Push the current day.
6. Leave unresolved days as zero after the scan.

## Dry Run

Use `[73, 74, 75, 71, 72]`:

| Day | Temperature | Stack Before | Action | Waits Changed |
| ---: | ---: | --- | --- | --- |
| 0 | 73 | `[]` | Push 0 | None |
| 1 | 74 | `[0]` | Pop 0, push 1 | `waits[0] = 1` |
| 2 | 75 | `[1]` | Pop 1, push 2 | `waits[1] = 1` |
| 3 | 71 | `[2]` | Push 3 | None |
| 4 | 72 | `[2, 3]` | Pop 3, push 4 | `waits[3] = 1` |

Days 2 and 4 remain unresolved, so their answers stay zero. The result is
`[1, 1, 0, 1, 0]`.

## Python Used Here

```python
waits = [0] * len(temperatures)
```

This creates one zero for every input day.

```python
unresolved[-1]
```

Index `-1` reads the top stack item without removing it. `pop()` removes and
returns the top item.

## Why It Is Correct

A day remains on the stack exactly while no warmer scanned day exists. When a
warmer temperature arrives, the current day is the first such day because the
scan moves chronologically and the old day has survived every earlier check.
The algorithm records that distance and removes the resolved day.

Days left on the stack have no warmer value anywhere to their right, so zero is
correct for them.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Every index is pushed once.
- Every index is popped at most once.
- Total time is `O(N)`, even though a `while` loop is inside a `for` loop.
- The answer and unresolved stack use `O(N)` space. Auxiliary stack space is
  `O(N)` in a decreasing or equal-temperature input.

## Assumptions to Say Aloud

- A warmer day must be strictly greater; equal is not enough.
- The answer is a number of days, not the warmer temperature itself.
- Zero means no qualifying future day.
- Input order represents chronological order and must not be sorted.

## Edge Cases

- Empty input.
- One day.
- Strictly increasing temperatures.
- Strictly decreasing temperatures.
- All temperatures equal.
- One warm day resolves several earlier days.

## Common Mistakes

- Storing only temperatures and losing the distance calculation.
- Popping on `<=` and incorrectly treating equal as warmer.
- Using `if` instead of `while`, so one day resolves only one prior day.
- Sorting the input and destroying chronological order.
- Calling the nested loops `O(N^2)` without counting pushes and pops.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Return the next warmer temperature. | Save today's temperature instead of the index distance. |
| Find the next smaller value. | Reverse the comparison while preserving unresolved indexes. |
| Search toward the left. | Scan left to right and resolve or query previous items according to the requested direction. |
| What if equal counts? | Pop while the saved temperature is `<=` today's value. |
| Process a live stream. | Keep unresolved `(index, temperature)` entries and emit answers when later values resolve them. |

## Interview Explanation

> I keep indexes of days that have not found a warmer future day. Their
> temperatures are non-increasing from the bottom to the top. When today's
> temperature is greater than the stack top, today is the first warmer day for
> that index, so I pop it and record the distance. Each index is pushed and
> popped at most once, giving `O(N)` time and `O(N)` stack space.

## Test Aloud

```text
For [50, 50, 60], the second 50 does not resolve the first because equal is not
warmer. When 60 arrives, it pops both indexes. Their waits are 1 and 2 days, so
the answer is [2, 1, 0].
```

## Check Your Understanding

### Question 1: Next Greater Value

For each number, return the next greater value to its right, or `-1` if none
exists. What is the result for `[2, 1, 2, 4, 3]`?

<details>
<summary>Show answer and explanation</summary>

**Answer:** `[4, 2, 4, -1, -1]`.

The first `2` waits through `1` and the second equal `2`; `4` is its first
strictly greater value. The `1` is resolved by the next `2`. The second `2` is
resolved by `4`. Neither `4` nor the final `3` has a greater value to its right.

Use the same unresolved-index stack, but assign `numbers[current_index]` instead
of an index distance when popping.

**Complexity:** `O(N)` time and `O(N)` extra space.

</details>

### Question 2: Previous Smaller Value

Return the nearest smaller value to the left of every number, or `-1` if none
exists.

<details>
<summary>Show answer and detailed solution</summary>

```python
def previous_smaller(numbers: list[int]) -> list[int]:
    answer = []
    increasing = []

    for number in numbers:
        while increasing and increasing[-1] >= number:
            increasing.pop()

        answer.append(increasing[-1] if increasing else -1)
        increasing.append(number)

    return answer
```

Before answering for `number`, remove values that are not smaller. The remaining
top is the nearest smaller value because nearer unresolved values sit closer to
the top.

For `[4, 5, 2, 10, 8]`, the answer is `[-1, 4, -1, 2, 2]`.

**Complexity:** Each value is pushed and popped at most once, so time is `O(N)`
and stack space is `O(N)`.

</details>
