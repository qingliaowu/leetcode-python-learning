# Arrays, Strings, Hash Maps, and Sliding Window

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md)

These high-priority problems teach patterns that appear constantly in interviews. Study them in order: first dictionary lookup, then dictionary grouping, then a sliding window that tracks positions.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python 3 Basics course](../python_basics/) whenever syntax feels unfamiliar. The course includes a plain-English [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md).

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 1 | [Two Sum](./0001_two_sum.md) | [Code](./0001_two_sum.py) | Hash map lookup |
| 49 | [Group Anagrams](./0049_group_anagrams.md) | [Code](./0049_group_anagrams.py) | Hashable grouping key |
| 3 | [Longest Substring Without Repeating Characters](./0003_longest_substring_without_repeating_characters.md) | [Code](./0003_longest_substring_without_repeating_characters.py) | Sliding window |

## Recognize the Pattern

- A hash map remembers information so later lookup is fast.
- A grouping key turns items that belong together into the same dictionary key.
- A sliding window represents one continuous section of an array or string using `left` and `right` indexes.

For every problem, ask: "What information from earlier input would make the current decision fast?"

## Ready to Move On

You are ready when you can explain what each dictionary value represents, keep a sliding-window invariant, and solve both self-checks for each lesson. Continue to [Stacks and Queues](../stacks_queues/README.md).
