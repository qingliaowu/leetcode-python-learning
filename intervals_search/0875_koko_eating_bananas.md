# 875. Koko Eating Bananas

[LeetCode problem](https://leetcode.com/problems/koko-eating-bananas/) | [Python solution](./0875_koko_eating_bananas.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

There are piles of bananas. At an integer speed of `k` bananas per hour, one
hour is spent on one pile, even if fewer than `k` bananas remain in that pile.

Find the smallest speed that finishes every pile within `h` hours.

```text
piles = [3, 6, 7, 11]
h = 8
answer = 4
```

At speed `4`, the piles take `1 + 2 + 2 + 3 = 8` hours.

## Recognize the Pattern

The input piles are not the sorted search target. The possible **answers** are
ordered:

```text
speed 1, 2, 3, ... largest pile
```

For each speed, ask a yes/no question:

```text
Can this speed finish within h hours?
```

Feasibility is monotonic:

- A speed that works means every faster speed also works.
- A speed that fails means every slower speed also fails.

That makes this **binary search on the answer space**.

## Start With a Direct Approach

Try speed `1`, then `2`, then `3`, until one works. If the largest pile contains
one billion bananas, that may require nearly one billion trials.

Binary search discards half the speed range after every feasibility check.

## Search Boundaries

- Minimum possible speed is `1`.
- Maximum needed speed is the largest pile. At that speed, every pile takes one
  hour, and the problem guarantees enough hours for at least one hour per pile.

The invariant is:

```text
The smallest feasible speed is somewhere inside [left, right].
```

## Ceiling Division

A pile of `7` at speed `3` takes `3` hours, not `2.333` hours.

For positive integers:

```python
hours = (pile + speed - 1) // speed
```

This is integer ceiling division. It avoids floating-point rounding.

## Step by Step

1. Set `left = 1` and `right = max(piles)`.
2. While the range contains more than one speed, choose its middle.
3. Sum the ceiling-divided hours for every pile.
4. If the speed works, keep it as a candidate by setting `right = speed`.
5. If it fails, remove it and every slower speed with `left = speed + 1`.
6. When `left == right`, return that smallest feasible speed.

## Dry Run

Use piles `[3, 6, 7, 11]`, `h = 8`:

| Range | Speed | Needed Hours | Decision |
| --- | ---: | ---: | --- |
| `[1, 11]` | 6 | `1 + 1 + 2 + 2 = 6` | Works; keep 6 and search left |
| `[1, 6]` | 3 | `1 + 2 + 3 + 4 = 10` | Fails; discard 1 through 3 |
| `[4, 6]` | 5 | `1 + 2 + 2 + 3 = 8` | Works; keep 5 and search left |
| `[4, 5]` | 4 | `1 + 2 + 2 + 3 = 8` | Works; keep 4 |

The range becomes `[4, 4]`, so the minimum speed is `4`.

## Python Used Here

```python
speed = (left + right) // 2
```

`//` performs integer floor division.

```python
right = speed
```

The working speed stays in the search range because it might be the first one.
This differs from classic exact-target search, where a checked middle can often
be returned or removed immediately.

## Why It Is Correct

The initial range contains every possible minimum speed. If a middle speed
fails, monotonicity proves all slower speeds fail, so moving `left` past it loses
no answer. If it works, all faster speeds also work, but the middle might be the
smallest working speed, so setting `right` to it preserves the answer.

The range shrinks until one speed remains. Because the invariant always keeps
the smallest feasible speed inside, that remaining speed is the answer.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the pile count and `M` the largest pile.

- One feasibility check scans all piles in `O(N)` time.
- Binary search performs `O(log M)` checks.
- Total time is `O(N log M)`.
- The algorithm uses `O(1)` extra space.

## Assumptions to Say Aloud

- Piles are non-empty and contain positive integers.
- `h` is at least the number of piles, so a solution exists.
- Only one pile can be eaten during an hour.
- Speed must be a positive integer.

## Edge Cases

- One pile and one hour requires the entire pile as speed.
- Many extra hours make speed `1` sufficient.
- `h` equals the number of piles, requiring the largest pile speed.
- Very large pile values should use integer arithmetic.
- Several piles have the same size.

## Common Mistakes

- Binary-searching the unsorted pile list instead of possible speeds.
- Using `pile // speed` and forgetting the partial final hour.
- Setting `right = speed - 1` after a working speed and accidentally discarding
  the answer under this lower-bound template.
- Searching from zero and dividing by zero.
- Returning the first speed tested that happens to work.
- Saying `O(log N)` without including the `O(N)` feasibility scan.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| What if speed may be fractional? | Integer monotonic search no longer applies directly; define required precision and use a bounded numerical search. |
| What if two piles can be processed at once? | The feasibility function changes into a scheduling problem; confirm whether workers are identical and whether a pile can be split. |
| Why not use `math.ceil(pile / speed)`? | It works for moderate values, but integer ceiling division avoids floating-point conversion. |
| Return total hours at the chosen speed. | Run the feasibility calculation once more for the returned speed. |
| Name another answer-space search. | Minimum ship capacity, maximum minimum distance, and smallest threshold satisfying a count are common forms. |

## Interview Explanation

> I am not searching the pile values. I search speeds from one through the
> largest pile. The predicate "finishes within h hours" is monotonic: once a
> speed works, every faster speed works. A failing middle removes the lower half;
> a working middle remains a candidate while I search lower. Each check is
> `O(N)`, and there are `O(log M)` checks, so time is `O(N log M)` with constant
> extra space.

## Test Aloud

```text
For [1, 1, 1, 1] with 10 hours, speed 1 needs four hours and is feasible. Since
1 is the minimum allowed speed, the answer is 1.
```

## Check Your Understanding

### Question 1: Find the Boundary

Suppose a predicate over integers 1 through 10 is:

```text
False False False False True True True True True True
```

What value should this lower-bound binary search return?

<details>
<summary>Show answer and explanation</summary>

**Answer:** `5`, the first `True` value.

When a middle is false, move `left` to `middle + 1`. When it is true, keep it
with `right = middle`. The final equal boundaries identify the transition from
impossible to possible.

This is the abstract structure behind Koko: each integer represents a speed and
each boolean says whether that speed finishes on time.

</details>

### Question 2: Minimum Shipping Capacity

Packages must ship in order within `days`. A ship carries up to one integer
capacity per day. Return the minimum capacity.

<details>
<summary>Show answer and detailed solution</summary>

```python
def minimum_capacity(weights: list[int], days: int) -> int:
    left = max(weights)
    right = sum(weights)

    while left < right:
        capacity = (left + right) // 2
        used_days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                used_days += 1
                current_load = 0
            current_load += weight

        if used_days <= days:
            right = capacity
        else:
            left = capacity + 1

    return left
```

Capacity cannot be below the heaviest package and never needs to exceed the sum
of all packages. A larger capacity never uses more days, so feasibility is
monotonic.

**Complexity:** If `S` is the sum of weights and `L` is the largest weight, time
is `O(N log(S - L + 1))`; extra space is `O(1)`.

**Tests:** Weights `[1, 2, 3, 1, 1]` in 4 days need capacity `3`. One day needs
capacity equal to the total sum.

</details>
