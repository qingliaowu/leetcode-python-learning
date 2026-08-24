"""
LeetCode 677: Map Sum Pairs

Goal:
Store string keys with integer values, then return the sum of all values whose
keys start with a given prefix.

Beginner lesson:
See 0677_map_sum_pairs.md for dict.get, difference updates, a dry run, and an
interview explanation.

Idea:
Keep a dictionary of current key values. When a key is inserted again, calculate
the difference between the new value and old value. Add that difference to every
trie node along the key path.

Complexity:
- insert: O(L), where L is the key length
- sum: O(P), where P is the prefix length
- space: O(total number of characters inserted)
"""


class TrieNode:
    """One prefix position with the sum of all keys below that prefix."""

    def __init__(self):
        self.children = {}
        self.total = 0


class MapSum:
    """Map string keys to values and quickly sum values by key prefix."""

    def __init__(self):
        self.root = TrieNode()
        # This dictionary remembers the current value of each complete key.
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        """Insert a new key or replace an existing key's value."""
        # get(key, 0) returns 0 when this key has not been inserted before.
        old_value = self.values.get(key, 0)
        # Only this change should be applied to the existing prefix totals.
        difference = val - old_value
        self.values[key] = val

        node = self.root
        # += adds the difference to the total already stored on the node.
        node.total += difference

        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.total += difference

    def sum(self, prefix: str) -> int:
        """Return the value total for all keys beginning with prefix."""
        node = self.root

        for char in prefix:
            if char not in node.children:
                # A missing path means no keys have this prefix.
                return 0
            node = node.children[char]

        # The work was done during insert, so the answer is already cached.
        return node.total


if __name__ == "__main__":
    # The final update proves that replacement does not double-count a key.
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    assert map_sum.sum("ap") == 3

    map_sum.insert("app", 2)
    assert map_sum.sum("ap") == 5

    map_sum.insert("apple", 2)
    assert map_sum.sum("ap") == 4
