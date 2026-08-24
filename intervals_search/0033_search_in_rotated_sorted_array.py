"""
LeetCode 33: Search in Rotated Sorted Array

Find target in a sorted array rotated at an unknown position.

Beginner lesson:
See 0033_search_in_rotated_sorted_array.md for binary-search boundaries, the
sorted-half test, a dry run, and interview notes.

Complexity:
- time: O(log N)
- space: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Return target's index, or -1 when target is absent."""
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            # At least one side around middle must still be normally sorted.
            if nums[left] <= nums[middle]:
                # The left half is sorted. Is target inside its value range?
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                # The right half is sorted.
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert solution.search([1], 1) == 0
    assert solution.search([3, 1], 1) == 1
