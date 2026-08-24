# 33. Search in Rotated Sorted Array

[LeetCode problem](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python solution](./0033_search_in_rotated_sorted_array.py)

## What the Question Asks

A sorted array with distinct values was rotated at an unknown position:

```text
sorted:  [0, 1, 2, 4, 5, 6, 7]
rotated: [4, 5, 6, 7, 0, 1, 2]
```

Return the target index in `O(log N)` time, or `-1` if it is absent.

## Python Used Here

```python
middle = (left + right) // 2
```

`//` is integer floor division, so `middle` is a valid list index.

Python allows combined comparisons:

```python
nums[left] <= target < nums[middle]
```

This means both `nums[left] <= target` and `target < nums[middle]`.

## Binary Search Boundaries

`left` and `right` are both included in the remaining search area, so the loop uses `left <= right`.

After checking `middle`, exclude it from the next range:

- Search left with `right = middle - 1`.
- Search right with `left = middle + 1`.

These updates guarantee progress and prevent an infinite loop.

## Rotated-Array Insight

The entire remaining range may not be sorted, but at least one half around `middle` is normally sorted.

- If `nums[left] <= nums[middle]`, the left half is sorted.
- Otherwise, the right half is sorted.

Once the sorted half is known, check whether the target value fits inside that half's endpoint values. Keep that half if it does; otherwise keep the other half.

## Dry Run

Search for `0` in `[4, 5, 6, 7, 0, 1, 2]`:

1. `left=0`, `right=6`, `middle=3`, value `7`.
2. Left half `[4,5,6,7]` is sorted, but `0` is not between `4` and `7`. Move `left` to `4`.
3. `left=4`, `right=6`, `middle=5`, value `1`.
4. Left half `[0,1]` is sorted, and `0` is in its range. Move `right` to `4`.
5. `middle=4`, value `0`. Return index `4`.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Time: `O(log N)` because every iteration discards about half the range.
- Space: `O(1)` because only a few index variables are stored.

The distinct-values condition makes the sorted-half decision unambiguous.

## Common Mistakes

- Performing a linear scan and missing the required `O(log N)` time.
- Checking whether the target is in a half before proving that half is sorted.
- Using incorrect `<` versus `<=` endpoint comparisons.
- Setting a boundary to `middle` instead of excluding the checked index.
- Forgetting the single-element case.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| What if duplicate values are allowed? | When left, middle, and right values are equal, sorted-side detection is ambiguous. Move boundaries inward; worst-case time can become `O(N)`. |
| Find the rotation index or minimum value. | Compare middle with the right endpoint and keep the half containing the rotation point. |
| Return the first target occurrence with duplicates. | Continue after a match and account for ambiguity; logarithmic worst-case time may no longer be possible. |
| What if the target is queried many times? | Find the pivot once, then binary-search the appropriate sorted section for each query. |

## Interview Explanation

> I use binary search. Rotation breaks global ordering, but one side of the midpoint is always sorted. I identify that side, test whether the target lies in its value range, and keep either that half or the other half. Each step discards half the candidates, so the time is logarithmic.

## Check Your Understanding

Try each question before opening its answer. Name the sorted half before deciding which boundary to move.

### Question 1: Trace a Successful Search

For `nums = [6, 7, 0, 1, 2, 4, 5]` and `target = 4`, which index is returned? What does the first midpoint tell you?

<details>
<summary>Show answer and explanation</summary>

**Answer:** Index `5` is returned.

The first midpoint is index `3`, whose value is `1`. The right half `[1, 2, 4, 5]` is sorted, and target `4` lies in its value range, so the search discards indexes `0` through `3`. Binary search then narrows the remaining range until it reaches index `5`.

The important order is: identify a sorted side, check whether the target belongs in that side, and only then move a boundary.

**Complexity:** `O(log N)` time and `O(1)` extra space.

**Edge case:** For one element, the loop must still inspect that final candidate.

</details>

### Question 2: Find the Minimum Rotated Value

Given a non-empty sorted array of distinct values that may be rotated, return its minimum value. For `[4, 5, 6, 1, 2, 3]`, return `1`.

<details>
<summary>Show answer and detailed solution</summary>

```python
def find_rotated_minimum(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        middle = (left + right) // 2

        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle

    return nums[left]
```

The right endpoint provides a sorted-array reference. If the middle value is greater than the right value, the rotation point and minimum must be strictly to the right of `middle`. Otherwise, `middle` may itself be the minimum, so the code keeps it with `right = middle`.

The loop stops when both boundaries point to the only possible minimum.

**Complexity:** `O(log N)` time and `O(1)` extra space.

**Tests:** `[4, 5, 1, 2, 3]` returns `1`; `[1, 2, 3]` returns `1`; `[7]` returns `7`.

</details>
