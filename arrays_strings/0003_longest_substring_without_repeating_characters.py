"""
LeetCode 3: Longest Substring Without Repeating Characters

Find the length of the longest continuous part of a string with unique chars.

Beginner lesson:
See 0003_longest_substring_without_repeating_characters.md for sliding-window
basics, an index trace, and interview notes.

Complexity:
- time: O(N)
- space: O(U), where U is the number of distinct characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the longest duplicate-free substring length."""
        # The current window is s[left:right + 1].
        left = 0
        best_length = 0
        last_seen = {}

        for right, char in enumerate(s):
            # Move left only if this copy is inside the current window.
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            window_length = right - left + 1
            best_length = max(best_length, window_length)

        return best_length


if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("abba") == 2
