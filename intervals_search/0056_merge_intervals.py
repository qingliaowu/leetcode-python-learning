"""
LeetCode 56: Merge Intervals

Combine all overlapping [start, end] intervals.

Beginner lesson:
See 0056_merge_intervals.md for sorting, lambda, overlap rules, a dry run,
and interview notes.

Complexity:
- time: O(N log N), caused by sorting
- space: O(N) for the output (and sorting storage)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Return non-overlapping intervals covering the same ranges."""
        # Sort by each interval's start value at index 0.
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        merged = []

        for start, end in sorted_intervals:
            # No previous range, or a gap after the previous range.
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                # The ranges overlap; extend the previous end if necessary.
                merged[-1][1] = max(merged[-1][1], end)

        return merged


if __name__ == "__main__":
    solution = Solution()

    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.merge([]) == []
