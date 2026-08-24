"""
LeetCode 49: Group Anagrams

Group words that contain the same characters with the same counts.

Beginner lesson:
See 0049_group_anagrams.md for sorted keys, tuples, a dry run, and interview
notes.

Complexity:
- time: O(N * K log K), where K is the maximum word length
- space: O(N * K), including the grouped output
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Return groups of words that are anagrams of one another."""
        groups = {}

        for word in strs:
            # sorted(word) returns a list; tuple makes it usable as a dict key.
            key = tuple(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        # values() contains each completed group; list creates the result list.
        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    result = solution.groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    )

    # Group order is not important, so compare normalized sorted groups.
    normalized = sorted(sorted(group) for group in result)
    expected = sorted(
        sorted(group)
        for group in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )
    assert normalized == expected
    assert solution.groupAnagrams([""]) == [[""]]
