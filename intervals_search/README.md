# Intervals, Sorting, and Binary Search

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md) | [FDE track](../fde_interview/README.md) | [AI engineering](../ai_engineering/README.md)

These high-priority problems use ordering to reveal structure. Sorting places related intervals together, while binary search discards half of a sorted input or a monotonic range of possible answers.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) when needed. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 56 | [Merge Intervals](./0056_merge_intervals.md) | [Code](./0056_merge_intervals.py) | Sort, then merge overlaps |
| 253 | [Meeting Rooms II](./0253_meeting_rooms_ii.md) | [Code](./0253_meeting_rooms_ii.py) | Sort starts and track end times |
| 704 | [Binary Search](./0704_binary_search.md) | [Code](./0704_binary_search.py) | Discard half of a sorted array |
| 33 | [Search in Rotated Sorted Array](./0033_search_in_rotated_sorted_array.md) | [Code](./0033_search_in_rotated_sorted_array.py) | Modified binary search |
| 875 | [Koko Eating Bananas](./0875_koko_eating_bananas.md) | [Code](./0875_koko_eating_bananas.py) | Binary search on a monotonic answer range |

## Recognize the Pattern

- Sorting often changes a global comparison problem into a neighboring comparison problem.
- A min-heap exposes the smallest current value, such as the earliest ending meeting.
- Binary search needs a rule that proves which half can be discarded.
- Binary search on an answer asks whether each candidate is feasible, then finds the first or last feasible boundary.

## Ready to Move On

You are ready when you can state binary-search boundaries precisely, prove a feasibility predicate is monotonic, explain why sorting makes interval comparisons local, and handle touching endpoints deliberately. Continue to [Data Structure Design](../design_data_structures/README.md).
