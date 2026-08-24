"""
LeetCode 560: Subarray Sum Equals K

Count continuous subarrays whose values add exactly to k.

Beginner lesson:
See 0560_subarray_sum_equals_k.md for prefix-sum math, dictionary counts, a dry
run, and interview notes.

Complexity:
- time: O(N)
- space: O(N)
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Return how many continuous subarrays have sum k."""
        running_sum = 0
        answer = 0

        # One empty prefix with sum 0 exists before the array begins.
        prefix_counts = {0: 1}

        for number in nums:
            running_sum += number
            needed_prefix = running_sum - k

            # Every earlier needed prefix creates one valid subarray ending here.
            answer += prefix_counts.get(needed_prefix, 0)

            prefix_counts[running_sum] = (
                prefix_counts.get(running_sum, 0) + 1
            )

        return answer


if __name__ == "__main__":
    solution = Solution()

    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
    assert solution.subarraySum([1, -1, 0], 0) == 3
    assert solution.subarraySum([], 0) == 0
