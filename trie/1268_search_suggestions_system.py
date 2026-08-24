"""
LeetCode 1268: Search Suggestions System

Goal:
After each character of searchWord is typed, return up to three product names
with that prefix in lexicographical order.

Beginner lesson:
See 1268_search_suggestions_system.md for Python syntax, a dry run, and an
interview explanation.

Idea:
Sort products first. Then insert them into a trie. Since the products are
inserted in sorted order, each trie node only needs to keep the first three
products that pass through it.

Complexity:
- sorting: O(N log N), where N is the number of products
- building trie: O(T), where T is the total number of product characters
- searching: O(M), where M is the length of searchWord
- space: O(T)
"""

from typing import List


class TrieNode:
    """A prefix node with child paths and up to three cached products."""

    def __init__(self):
        self.children = {}
        # A list keeps the products in their sorted insertion order.
        self.suggestions = []


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        """Return up to three sorted product suggestions for every prefix."""
        # sort() changes the list in place. Earlier products are inserted first.
        products.sort()
        root = TrieNode()

        # Build the Trie and cache the best answers at every prefix node.
        for product in products:
            node = root

            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

                # Sorted insertion means the first three are the correct top 3.
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        answer = []
        node = root

        # Each typed character creates one list in the final answer.
        for char in searchWord:
            if node is not None and char in node.children:
                node = node.children[char]
                answer.append(node.suggestions)
            else:
                # A longer prefix cannot match after a shorter one has failed.
                node = None
                answer.append([])

        return answer


if __name__ == "__main__":
    # The expected value contains one inner list for each letter in "mouse".
    solution = Solution()
    result = solution.suggestedProducts(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        "mouse",
    )

    assert result == [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
    assert solution.suggestedProducts([], "hi") == [[], []]
    assert solution.suggestedProducts(["apple"], "az") == [["apple"], []]
    assert solution.suggestedProducts(["a", "ab"], "") == []
