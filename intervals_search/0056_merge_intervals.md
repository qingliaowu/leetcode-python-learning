# 56. Merge Intervals

[LeetCode problem](https://leetcode.com/problems/merge-intervals/) | [Python solution](./0056_merge_intervals.py)

## What the Question Asks

Each interval `[start, end]` covers all values from start through end. Combine overlapping intervals and return the resulting non-overlapping ranges.

```text
[[1, 3], [2, 6], [8, 10]]
->
[[1, 6], [8, 10]]
```

Intervals touching at an endpoint overlap: `[1, 4]` and `[4, 5]` become `[1, 5]`.

## Python Used Here

Sort with a key function:

```python
sorted_intervals = sorted(
    intervals,
    key=lambda interval: interval[0],
)
```

`sorted` returns a new list. `lambda interval: interval[0]` is a small unnamed function that returns each interval's start for sorting.

Negative indexing accesses from the end:

```python
merged[-1]     # last interval
merged[-1][1]  # end of the last interval
```

`for start, end in sorted_intervals` unpacks each two-item interval.

## Why Sorting Helps

Before sorting, an interval could overlap any later item. After sorting by start, all possible overlaps with the current merged range appear next to it.

Only compare the next interval with the last interval in `merged`:

- If `start > previous_end`, there is a gap. Add a new interval.
- Otherwise, they overlap. Keep the previous start and use the larger end.

## Step-by-Step Approach

1. Sort intervals by start.
2. Create an empty result list.
3. For each interval, add it if the result is empty or it starts after the last result ends.
4. Otherwise, update the last result end to the maximum of both ends.
5. Return the result.

The code appends a new `[start, end]` list, so extending the result does not modify an original interval object.

## Dry Run

Input after sorting: `[[1, 3], [2, 6], [8, 10], [15, 18]]`

| Current | Last merged | Action | Result |
| --- | --- | --- | --- |
| `[1,3]` | none | Add | `[[1,3]]` |
| `[2,6]` | `[1,3]` | Overlap; end becomes 6 | `[[1,6]]` |
| `[8,10]` | `[1,6]` | Gap; add | `[[1,6],[8,10]]` |
| `[15,18]` | `[8,10]` | Gap; add | `[[1,6],[8,10],[15,18]]` |

For a contained interval such as `[2, 3]` after `[1, 10]`, `max(10, 3)` keeps the end at `10`.

## Complexity

- Time: `O(N log N)` for sorting, followed by an `O(N)` scan.
- Space: `O(N)` for the result and sorting storage.

## Common Mistakes

- Trying to merge without sorting first.
- Using `start >= previous_end` as the gap condition and failing to merge touching endpoints.
- Replacing the previous end with `end` instead of `max(previous_end, end)`.
- Comparing only with the original previous input interval rather than the last merged interval.

## Interview Explanation

> I sort by start time, which makes all overlapping ranges adjacent. I keep a result of already merged intervals. Each new interval either starts after the last result ends, so it is appended, or overlaps, so I extend the last end. Sorting dominates at `O(N log N)`.
