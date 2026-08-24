"""Lesson 10: combine basic Python syntax in LeetCode's class format."""

from collections import deque
import heapq
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return True when any value appears more than once."""
        seen = set()

        for number in nums:
            if number in seen:
                return True
            seen.add(number)

        return False


if __name__ == "__main__":
    solution = Solution()

    assert solution.containsDuplicate([1, 2, 3, 1]) is True
    assert solution.containsDuplicate([1, 2, 3, 4]) is False
    assert solution.containsDuplicate([]) is False

    # Stack: last item added is the first removed.
    stack = []
    stack.append("first")
    stack.append("second")
    assert stack.pop() == "second"

    # Queue: first item added is the first removed.
    queue = deque(["first", "second"])
    assert queue.popleft() == "first"

    # Min-heap: smallest item is removed first.
    heap = []
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 2)
    assert heapq.heappop(heap) == 2

    print("Lesson 10 checks passed.")
