"""
LeetCode 1: Two Sum

Find two different indexes whose values add to target.

Beginner lesson:
See 0001_two_sum.md for the hash map idea, Python syntax, a dry run, and
interview notes.

Complexity:
- time: O(N), because each number is visited once
- space: O(N), for values remembered in the dictionary
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return the indexes of two numbers that add up to target."""
        # Map a number already visited to its index in nums.
        seen = {}

        # enumerate gives both the index and the value at that index.
        for index, number in enumerate(nums):
            needed = target - number

            # If needed was seen earlier, the two indexes are different.
            if needed in seen:
                return [seen[needed], index]

            # Save this number only after checking for its partner.
            seen[number] = index

        # The problem guarantees one answer, so normal inputs never reach here.
        return []


if __name__ == "__main__":
    solution = Solution()

    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
