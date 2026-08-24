"""
LeetCode 211: Design Add and Search Words

Goal:
Support adding words and searching words. The search pattern may contain `.`,
which can match any single character.

Beginner lesson:
See 0211_design_add_and_search_words.md for recursion basics, a DFS dry run,
and an interview explanation.

Idea:
Use a normal trie for addWord. For search, use DFS. When the current character
is `.`, try every child node.

Complexity:
- addWord: O(L), where L is the word length
- search without wildcard: O(L)
- search with wildcards: can branch to many trie paths in the worst case
- space: O(total number of characters inserted)
"""


class TrieNode:
    """One Trie position, its next character paths, and an end marker."""

    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    """Store words and search them with optional single-character wildcards."""

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Insert a word using the same process as a basic Trie."""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    def search(self, word: str) -> bool:
        """Search a pattern in which each dot matches one character."""
        # Begin DFS at character index 0 and at the Trie root.
        return self._dfs(word, 0, self.root)

    def _dfs(self, word: str, index: int, node: TrieNode) -> bool:
        """Try to match word[index:] starting from node."""
        # Base case: every pattern character has been consumed.
        if index == len(word):
            return node.is_word

        char = word[index]

        if char == ".":
            # values() gives the child nodes without their character keys.
            for child in node.children.values():
                # Return immediately when any possible path is successful.
                if self._dfs(word, index + 1, child):
                    return True
            # Every possible child path failed.
            return False

        if char not in node.children:
            return False

        # An exact letter has only one possible next path.
        return self._dfs(word, index + 1, node.children[char])


if __name__ == "__main__":
    # Add a few words, then test missing, exact, and wildcard patterns.
    word_dictionary = WordDictionary()
    word_dictionary.addWord("bad")
    word_dictionary.addWord("dad")
    word_dictionary.addWord("mad")

    assert word_dictionary.search("pad") is False
    assert word_dictionary.search("bad") is True
    assert word_dictionary.search(".ad") is True
    assert word_dictionary.search("b..") is True
