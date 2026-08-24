# Intervals, Sorting, and Binary Search

These high-priority problems use ordering to reveal structure. Sorting places related intervals together, while binary search repeatedly discards half of the remaining search space.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) when needed. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 56 | [Merge Intervals](./0056_merge_intervals.md) | [Code](./0056_merge_intervals.py) | Sort, then merge overlaps |
| 253 | [Meeting Rooms II](./0253_meeting_rooms_ii.md) | [Code](./0253_meeting_rooms_ii.py) | Sort starts and track end times |
| 33 | [Search in Rotated Sorted Array](./0033_search_in_rotated_sorted_array.md) | [Code](./0033_search_in_rotated_sorted_array.py) | Modified binary search |

## Pattern Summary

- Sorting often changes a global comparison problem into a neighboring comparison problem.
- A min-heap exposes the smallest current value, such as the earliest ending meeting.
- Binary search needs a rule that proves which half can be discarded.
