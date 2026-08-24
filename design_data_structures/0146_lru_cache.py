"""
LeetCode 146: LRU Cache

Store key-value pairs with O(1) get and put, evicting the least recently used
key when capacity is exceeded.

Beginner lesson:
See 0146_lru_cache.md for the hash map, doubly linked list, sentinels, dry run,
complexity, edge cases, and interview explanation.

Complexity:
- get: O(1) average
- put: O(1) average
- space: O(capacity)
"""


class ListNode:
    """One cache entry and its links in usage order."""

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}

        # Sentinels stay at both ends and are never real cache entries.
        self.least_recent = ListNode()
        self.most_recent = ListNode()
        self.least_recent.next = self.most_recent
        self.most_recent.previous = self.least_recent

    def get(self, key: int) -> int:
        """Return a value and mark its key as most recently used."""
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self._remove(node)
        self._add_most_recent(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Insert or update a key, then evict if capacity is exceeded."""
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._remove(node)
            self._add_most_recent(node)
        else:
            node = ListNode(key, value)
            self.nodes[key] = node
            self._add_most_recent(node)

        if len(self.nodes) > self.capacity:
            node_to_remove = self.least_recent.next
            self._remove(node_to_remove)
            del self.nodes[node_to_remove.key]

    def _remove(self, node: ListNode) -> None:
        """Disconnect one real node from the linked list."""
        before = node.previous
        after = node.next
        before.next = after
        after.previous = before

    def _add_most_recent(self, node: ListNode) -> None:
        """Insert one node immediately before the right sentinel."""
        before = self.most_recent.previous
        before.next = node
        node.previous = before
        node.next = self.most_recent
        self.most_recent.previous = node


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)
    assert cache.get(2) == -1

    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    one_item_cache = LRUCache(1)
    one_item_cache.put(1, 10)
    one_item_cache.put(1, 20)
    assert one_item_cache.get(1) == 20
    one_item_cache.put(2, 30)
    assert one_item_cache.get(1) == -1
