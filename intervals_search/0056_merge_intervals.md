# 56. Merge Intervals

[LeetCode problem](https://leetcode.com/problems/merge-intervals/) | [Python solution](./0056_merge_intervals.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

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

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Time: `O(N log N)` for sorting, followed by an `O(N)` scan.
- Space: `O(N)` for the result and sorting storage.

## Common Mistakes

- Trying to merge without sorting first.
- Using `start >= previous_end` as the gap condition and failing to merge touching endpoints.
- Replacing the previous end with `end` instead of `max(previous_end, end)`.
- Comparing only with the original previous input interval rather than the last merged interval.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Insert one interval into already sorted non-overlapping intervals. | Append intervals before it, merge every overlap with the new interval, then append the remainder in `O(N)` time. |
| Preserve the input list and inner intervals. | Use `sorted` and create new `[start, end]` lists instead of sorting or updating input objects in place. |
| Find intersections between two interval lists. | Use two pointers; record overlap and advance the interval that ends first. |
| Return total covered length. | Merge first, then sum `end - start`, clarifying whether integer endpoints or continuous ranges are intended. |
| What if intervals arrive online? | A balanced interval tree or ordered map can locate nearby overlaps without sorting the entire history again. |

## Interview Explanation

> I sort by start time, which makes all overlapping ranges adjacent. I keep a result of already merged intervals. Each new interval either starts after the last result ends, so it is appended, or overlaps, so I extend the last end. Sorting dominates at `O(N log N)`.

## Check Your Understanding

Try each question before opening its answer. State whether touching endpoints count as overlap.

### Question 1: Merge by Hand

What is the merged result for `[[1, 4], [4, 5], [8, 10], [2, 3]]` when touching endpoints overlap?

<details>
<summary>Show answer and explanation</summary>

**Answer:** `[[1, 5], [8, 10]]`.

Sorting by start gives `[[1, 4], [2, 3], [4, 5], [8, 10]]`. Interval `[2, 3]` is contained inside `[1, 4]`, so the end stays `4`. Interval `[4, 5]` touches the current end and therefore extends it to `5`. Interval `[8, 10]` begins after `5`, so it starts a new merged interval.

Using `max(current_end, next_end)` is important because an interval may be completely contained inside the current one.

**Complexity:** `O(N log N)` time for sorting and up to `O(N)` output space.

**Edge case:** An empty input returns an empty list.

</details>

### Question 2: Insert One New Interval

The existing intervals are already sorted and non-overlapping. Insert one interval and merge where needed. For `[[1, 2], [5, 7]]` and `[2, 6]`, return `[[1, 7]]`.

<details>
<summary>Show answer and detailed solution</summary>

```python
def insert_interval(
    intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    result = []
    index = 0
    start, end = new_interval

    while index < len(intervals) and intervals[index][1] < start:
        result.append(intervals[index])
        index += 1

    while index < len(intervals) and intervals[index][0] <= end:
        start = min(start, intervals[index][0])
        end = max(end, intervals[index][1])
        index += 1

    result.append([start, end])
    result.extend(intervals[index:])
    return result
```

The first loop copies intervals completely before the new one. The second loop combines every overlap into one growing `[start, end]`. Once an interval starts after the merged end, all remaining intervals are also later because the input is sorted.

No new sort is needed.

**Complexity:** `O(N)` time and `O(N)` output space.

**Tests:** Inserting `[2, 6]` into `[[1, 2], [5, 7]]` returns `[[1, 7]]`; inserting `[3, 4]` returns `[[1, 2], [3, 4], [5, 7]]`.

</details>
