# Arrays, Strings, Hash Maps, and Sliding Window

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Pattern map](../ALGORITHM_PATTERN_MAP.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md) | [FDE track](../fde_interview/README.md) | [AI engineering](../ai_engineering/README.md)

These high-priority problems teach patterns that appear constantly in interviews. Study them in order: dictionary lookup, dictionary grouping, a sliding window that tracks positions, then two pointers on sorted values.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) whenever syntax feels unfamiliar. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 1 | [Two Sum](./0001_two_sum.md) | [Code](./0001_two_sum.py) | Hash map lookup |
| 49 | [Group Anagrams](./0049_group_anagrams.md) | [Code](./0049_group_anagrams.py) | Hashable grouping key |
| 3 | [Longest Substring Without Repeating Characters](./0003_longest_substring_without_repeating_characters.md) | [Code](./0003_longest_substring_without_repeating_characters.py) | Sliding window |
| 15 | [3Sum](./0015_3sum.md) | [Code](./0015_3sum.py) | Sort, fix one value, and use two pointers |

## Recognize the Pattern

- A hash map remembers information so later lookup is fast.
- A grouping key turns items that belong together into the same dictionary key.
- A sliding window represents one continuous section of an array or string using `left` and `right` indexes.
- Two pointers on sorted values move inward according to whether a total is too small or too large.

For every problem, ask: "What information from earlier input would make the current decision fast?"

## Ready to Move On

You are ready when you can explain what each dictionary value represents, keep a sliding-window invariant, justify two-pointer movement from sorted order, and solve both self-checks for each lesson. Continue to [Stacks and Queues](../stacks_queues/README.md).
