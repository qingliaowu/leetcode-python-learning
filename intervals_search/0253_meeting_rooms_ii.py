"""
LeetCode 253: Meeting Rooms II

Find the minimum number of rooms needed for all meeting intervals.

Beginner lesson:
See 0253_meeting_rooms_ii.md for min-heaps, room reuse, a dry run, and
interview notes.

Complexity:
- time: O(N log N)
- space: O(N) in the worst case
"""

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Return the maximum number of meetings running at once."""
        intervals.sort(key=lambda interval: interval[0])
        end_times = []

        for start, end in intervals:
            # heap[0] is the earliest ending room currently allocated.
            if end_times and end_times[0] <= start:
                heapq.heappop(end_times)

            # Assign this meeting to a reused or newly allocated room.
            heapq.heappush(end_times, end)

        return len(end_times)


if __name__ == "__main__":
    solution = Solution()

    assert solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert solution.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert solution.minMeetingRooms([]) == 0
    assert solution.minMeetingRooms([[1, 5], [5, 8], [5, 10]]) == 2
