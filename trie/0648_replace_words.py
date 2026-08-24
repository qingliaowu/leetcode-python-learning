"""
LeetCode 648: Replace Words

Goal:
Replace each word in a sentence with the shortest dictionary root that is a
prefix of that word.

Beginner lesson:
See 0648_replace_words.md for split/join examples, a dry run, and an interview
explanation.

Idea:
Build a trie from dictionary roots. For each word in the sentence, walk through
the trie. The first node marked as a complete word is the shortest root.

Complexity:
- building trie: O(T), where T is the total number of dictionary characters
- replacing sentence: O(S), where S is the total number of sentence characters
- space: O(T)
"""

from typing import List


class TrieNode:
    """One prefix position and a marker for a complete dictionary root."""

    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """Replace each sentence word with its shortest matching root."""
        root = TrieNode()

        # First store all possible replacement roots.
        for word in dictionary:
            self._insert(root, word)

        replaced_words = []

        # split() turns the sentence into words separated by whitespace.
        for word in sentence.split():
            replaced_words.append(self._find_shortest_root(root, word))

        # join() rebuilds one string with a space between every word.
        return " ".join(replaced_words)

    def _insert(self, root: TrieNode, word: str) -> None:
        """Insert one dictionary root into the Trie."""
        node = root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    def _find_shortest_root(self, root: TrieNode, word: str) -> str:
        """Return the shortest matching root, or the original word."""
        node = root
        # A list is used to collect characters efficiently.
        prefix = []

        for char in word:
            if char not in node.children:
                # No longer root can match after this path is missing.
                return word

            prefix.append(char)
            node = node.children[char]

            if node.is_word:
                # The first complete root reached is always the shortest.
                return "".join(prefix)

        # The path existed, but no complete dictionary root was found.
        return word


if __name__ == "__main__":
    # The assertion checks matching and non-matching words in one sentence.
    solution = Solution()
    result = solution.replaceWords(
        ["cat", "bat", "rat"],
        "the cattle was rattled by the battery",
    )

    assert result == "the cat was rat by the bat"
    assert solution.replaceWords([], "keep every word") == "keep every word"
    assert solution.replaceWords(["a", "aa"], "aaaa") == "a"
    assert solution.replaceWords(["cat"], "cat") == "cat"
