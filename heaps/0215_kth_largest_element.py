"""
LeetCode 215: Kth Largest Element in an Array

Return the kth largest value without requiring the values to be distinct.

Beginner lesson:
See 0215_kth_largest_element.md for heapq basics, the size-k invariant, a dry
run, and interview notes.

Complexity:
- time: O(N log K)
- space: O(K)
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the smallest value among the array's k largest values."""
        min_heap = []

        for number in nums:
            heapq.heappush(min_heap, number)

            # Remove the smallest whenever more than k values are stored.
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Exactly the k largest remain; heap[0] is the smallest of them.
        return min_heap[0]


if __name__ == "__main__":
    solution = Solution()

    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert solution.findKthLargest([1], 1) == 1
