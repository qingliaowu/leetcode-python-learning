# Arrays, Strings, Hash Maps, and Sliding Window

These high-priority problems teach patterns that appear constantly in interviews. Study them in order: first dictionary lookup, then dictionary grouping, then a sliding window that tracks positions.

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) for the solve-out-loud process. Review the [Python refresher](../trie/README.md#1-python-refresher) whenever syntax feels unfamiliar.

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 1 | [Two Sum](./0001_two_sum.md) | [Code](./0001_two_sum.py) | Hash map lookup |
| 49 | [Group Anagrams](./0049_group_anagrams.md) | [Code](./0049_group_anagrams.py) | Hashable grouping key |
| 3 | [Longest Substring Without Repeating Characters](./0003_longest_substring_without_repeating_characters.md) | [Code](./0003_longest_substring_without_repeating_characters.py) | Sliding window |

## Pattern Summary

- A hash map remembers information so later lookup is fast.
- A grouping key turns items that belong together into the same dictionary key.
- A sliding window represents one continuous section of an array or string using `left` and `right` indexes.

For every problem, ask: "What information from earlier input would make the current decision fast?"
