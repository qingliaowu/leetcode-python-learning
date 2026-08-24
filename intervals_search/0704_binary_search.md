# 704. Binary Search

[LeetCode problem](https://leetcode.com/problems/binary-search/) | [Python solution](./0704_binary_search.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Given a sorted list of distinct integers, return the target's index. Return `-1` when it is absent. The required time is `O(log N)`.

```text
nums = [-1, 0, 3, 5, 9, 12]
target = 9
answer = 4
```

The sorted-input guarantee is what makes binary search possible.

## The Main Idea

Look at the middle value:

- If it equals the target, return its index.
- If it is smaller than the target, the target can only be to the right.
- If it is larger than the target, the target can only be to the left.

Every comparison discards about half of the remaining indexes.

## Search-Range Meaning

This solution uses an inclusive range:

```text
left and right are both possible target indexes.
```

Initialize:

```python
left = 0
right = len(nums) - 1
```

Continue while at least one index remains:

```python
while left <= right:
```

When `left > right`, the range is empty and the target is missing.

## Find the Middle

```python
middle = (left + right) // 2
```

`//` performs whole-number floor division, so the result is a valid integer index.

For `left = 0` and `right = 5`:

```text
middle = 5 // 2 = 2
```

## Move the Boundaries

If the middle value is too small:

```python
left = middle + 1
```

The middle was already checked, so exclude it.

If the middle value is too large:

```python
right = middle - 1
```

Again, exclude the checked middle.

Using `left = middle` or `right = middle` can leave the same range and cause an infinite loop.

## Dry Run

Search for `9` in `[-1, 0, 3, 5, 9, 12]`:

| Left | Right | Middle | Middle value | Action |
| ---: | ---: | ---: | ---: | --- |
| 0 | 5 | 2 | 3 | Too small; `left = 3` |
| 3 | 5 | 4 | 9 | Match; return `4` |

Search for `2`:

1. Middle value `3` is too large, so keep indexes `0..1`.
2. Middle value `-1` is too small, so keep index `1`.
3. Value `0` is too small, so `left` becomes `2` while `right` is `1`.
4. The range is empty. Return `-1`.

## The Invariant

At the start of every loop:

```text
If target exists, its index must be somewhere from left through right.
```

Comparing with the sorted middle value proves which half cannot contain the target. Removing that half preserves the invariant.

## Why It Is Correct

When the middle is smaller than the target, sorted order guarantees every value left of middle is also smaller. When middle is larger, every value right of middle is also larger. The algorithm only discards indexes that cannot hold the target. It returns on a match or after no possible index remains.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `N` be the number of values.

- Time: `O(log N)` because every iteration keeps at most half the remaining range.
- Extra space: `O(1)` because only `left`, `right`, and `middle` are stored.

For about one million sorted values, binary search needs only about 20 comparisons in the worst case.

## Assumptions to Say Aloud

- The input is sorted in nondecreasing order before the search begins.
- The function returns an index, or `-1` when the target is absent.
- If duplicates are allowed, returning any matching index is acceptable.
- The input list may be empty and is not modified.

## Edge Cases

- One value that matches.
- One value that does not match.
- Target at the first index.
- Target at the last index.
- Target smaller than every value.
- Target larger than every value.
- Empty list returns `-1` in this robust local implementation.

## Common Mistakes

- Using binary search on unsorted input.
- Starting `right` at `len(nums)` while using inclusive-boundary rules.
- Using `while left < right` and failing to check the final candidate.
- Forgetting `+ 1` or `- 1` when removing the checked middle.
- Returning a value instead of its index.
- Returning an insertion position when the question requires `-1`.
- Saying time is `O(N)` instead of recognizing repeated halving.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| Find the first or last occurrence when duplicates exist. | Save a match, then continue searching left for the first occurrence or right for the last occurrence. |
| Return the insertion position when target is missing. | Use a lower-bound search; when the loop ends, `left` is the first index where target can be inserted. |
| What if the array is sorted in descending order? | Reverse the comparison directions while keeping the same range invariant. |
| What if the sorted input has unknown length? | Use exponential search to find a containing range, then binary-search that range. |
| Can you write it recursively? | Pass smaller left/right boundaries recursively; time stays `O(log N)`, but stack space becomes `O(log N)`. |

## Interview Explanation

> I keep an inclusive range of possible indexes. I compare the target with its middle value. Sorted order lets me discard the middle and one entire half, so the range shrinks by about half each iteration. I return the matching index or `-1` when the range becomes empty. Time is `O(log N)` and extra space is `O(1)`.

## Test Aloud

```text
For one value [5], left and right are both 0, so the loop checks index 0. If
target is 5 it returns 0. Otherwise one boundary crosses the other and it
returns -1. This confirms the <= loop condition handles the final candidate.
```

## Check Your Understanding

Try each question before opening its answer. State what the search boundaries mean at every step.

### Question 1: Trace a Missing Target

What does binary search return for `nums = [1, 3, 5, 7]` and `target = 6`? Which candidate values does it inspect?

<details>
<summary>Show answer and explanation</summary>

**Answer:** It returns `-1`.

With the usual lower-middle calculation, it first checks value `3` at index `1`. Since `6` is larger, it keeps indexes `2` through `3`. It then checks value `5` at index `2` and moves left to index `3`. Finally it checks value `7`, moves right to index `2`, and stops because the boundaries crossed.

Every move excludes the middle index because it has already been checked.

**Complexity:** `O(log N)` time and `O(1)` extra space.

**Edge case:** If the input is empty, the initial right boundary is `-1`, so the loop never runs.

</details>

### Question 2: Find an Insertion Position

Return the first index where `target` could be inserted without breaking sorted order. For `[1, 3, 3, 7]`, target `3` returns `1`, and target `4` returns `3`.

<details>
<summary>Show answer and detailed solution</summary>

```python
def lower_bound(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)

    while left < right:
        middle = (left + right) // 2
        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle

    return left
```

The search range is half-open: `[left, right)`. Values strictly smaller than the target cannot be the answer, so `left` moves past them. A value equal to or larger than the target might be the first valid position, so the code keeps `middle` with `right = middle`.

When the boundaries meet, every earlier value is smaller and every later value is at least the target.

**Complexity:** `O(log N)` time and `O(1)` extra space.

**Tests:** `lower_bound([], 5)` returns `0`; `lower_bound([1, 3, 3, 7], 8)` returns `4`.

</details>
