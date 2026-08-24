"""
LeetCode 394: Decode String

Expand encoded patterns such as 3[a2[c]] using a stack.

Beginner lesson:
See 0394_decode_string.md for stack state, multi-digit counts, nesting, dry run,
complexity, edge cases, and interview explanation.

Complexity:
- time: O(N + D * H) safe worst case for encoded length N, decoded length D,
  and nesting depth H; commonly described as O(N + D)
- space: O(N + D) for stack buffers and decoded characters
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """Return the fully decoded version of s."""
        stack = []
        current_characters = []
        repeat_count = 0

        for character in s:
            if character.isdigit():
                # Build a multi-digit number: 12 means 1 * 10 + 2.
                repeat_count = repeat_count * 10 + int(character)
            elif character == "[":
                # Pause the outer text and count while decoding the inside.
                stack.append((current_characters, repeat_count))
                current_characters = []
                repeat_count = 0
            elif character == "]":
                previous_characters, saved_count = stack.pop()
                current_characters = (
                    previous_characters
                    + current_characters * saved_count
                )
            else:
                current_characters.append(character)

        return "".join(current_characters)


if __name__ == "__main__":
    solution = Solution()

    assert solution.decodeString("3[a]2[bc]") == "aaabcbc"
    assert solution.decodeString("3[a2[c]]") == "accaccacc"
    assert solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert solution.decodeString("10[a]") == "aaaaaaaaaa"
    assert solution.decodeString("plain") == "plain"
