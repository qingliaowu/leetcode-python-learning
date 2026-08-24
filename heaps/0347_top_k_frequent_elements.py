"""
LeetCode 347: Top K Frequent Elements

Return the k values that occur most often.

Beginner lesson:
See 0347_top_k_frequent_elements.md for frequency maps, tuple heaps, a dry
run, and interview notes.

Complexity:
- time: O(N log K)
- space: O(U + K), where U is the number of unique values
"""

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return any order containing the k most frequent values."""
        frequencies = {}

        for number in nums:
            frequencies[number] = frequencies.get(number, 0) + 1

        min_heap = []

        for number, frequency in frequencies.items():
            # Tuples compare by frequency first, then number for a tie.
            heapq.heappush(min_heap, (frequency, number))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Tuple unpacking ignores frequency and keeps each number.
        return [number for frequency, number in min_heap]


if __name__ == "__main__":
    solution = Solution()

    assert set(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert solution.topKFrequent([1], 1) == [1]
    assert set(solution.topKFrequent([4, 4, 5, 5, 6], 2)) == {4, 5}
