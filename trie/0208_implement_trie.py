"""
LeetCode 208: Implement Trie

Goal:
Design a trie with insert, search, and startsWith.

Beginner lesson:
See 0208_implement_trie.md for a Python refresher, diagram, dry run, and
interview explanation.

Idea:
Each node stores its next characters in a dictionary. A boolean flag marks
whether the current node is the end of a complete word.

Complexity:
- insert: O(L), where L is the length of the word
- search: O(L)
- startsWith: O(L)
- space: O(total number of characters inserted)
"""


class TrieNode:
    """One point in the Trie and all paths available from that point."""

    def __init__(self):
        # A dictionary maps each next character to another TrieNode object.
        self.children = {}
        # A path may exist as a prefix without being a complete saved word.
        self.is_word = False


class Trie:
    """Store words and answer exact-word and prefix queries."""

    def __init__(self):
        # The empty root is the starting point for every operation.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Add one complete word to the Trie."""
        node = self.root

        # A Python string can be visited one character at a time.
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move the local variable to the node for this character.
            node = node.children[char]

        # The loop has consumed every character, so this node ends the word.
        node.is_word = True

    def search(self, word: str) -> bool:
        """Return True only when the exact word was previously inserted."""
        node = self._find_node(word)
        # `and` stops early when node is None, so accessing is_word is safe.
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """Return True when at least one inserted word has this prefix."""
        return self._find_node(prefix) is not None

    def _find_node(self, text: str):
        """Follow text from the root; return its last node or None."""
        node = self.root

        for char in text:
            if char not in node.children:
                return None
            node = node.children[char]

        return node


if __name__ == "__main__":
    # These assertions run only when this file is executed directly.
    trie = Trie()
    trie.insert("apple")

    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True

    trie.insert("app")
    assert trie.search("app") is True
