"""
LeetCode 23: Merge K Sorted Lists

Merge several sorted linked lists into one sorted linked list.

Beginner lesson:
See 0023_merge_k_sorted_lists.md for linked-list references, tuple heap entries,
the dummy-node pattern, a dry run, and interview notes.

Complexity:
- time: O(N log K), for N total nodes across K lists
- space: O(K) for the heap
"""

import heapq


class ListNode:
    """Singly linked-list node matching the class supplied by LeetCode."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        """Return one sorted list containing all input nodes."""
        min_heap = []

        for list_index, node in enumerate(lists):
            if node is not None:
                # list_index safely breaks ties between equal node values.
                heapq.heappush(min_heap, (node.val, list_index, node))

        dummy = ListNode()
        tail = dummy

        while min_heap:
            value, list_index, node = heapq.heappop(min_heap)
            tail.next = node
            tail = node

            if node.next is not None:
                next_node = node.next
                heapq.heappush(
                    min_heap,
                    (next_node.val, list_index, next_node),
                )

        return dummy.next


def build_list(values):
    """Build a linked list for the local examples."""
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def to_values(node):
    """Convert a linked list to Python values for an easy assertion."""
    values = []

    while node is not None:
        values.append(node.val)
        node = node.next

    return values


if __name__ == "__main__":
    solution = Solution()
    lists = [
        build_list([1, 4, 5]),
        build_list([1, 3, 4]),
        build_list([2, 6]),
    ]

    assert to_values(solution.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert solution.mergeKLists([]) is None
    assert solution.mergeKLists([None, None]) is None
    assert to_values(solution.mergeKLists([build_list([1, 2, 3])])) == [1, 2, 3]
