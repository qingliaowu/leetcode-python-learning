"""
LeetCode 206: Reverse Linked List

Reverse the direction of every pointer in a singly linked list.

Beginner lesson:
See 0206_reverse_linked_list.md for node references, the three-pointer pattern,
a dry run, and interview notes.

Complexity:
- time: O(N)
- space: O(1)
"""


class ListNode:
    """Singly linked-list node matching the class supplied by LeetCode."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """Reverse the list in place and return its new head."""
        previous = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous


def build_list(values: list[int]) -> ListNode | None:
    """Build a linked list for local assertions."""
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def to_values(head: ListNode | None) -> list[int]:
    """Convert a linked list into values for local assertions."""
    values = []

    while head is not None:
        values.append(head.val)
        head = head.next

    return values


if __name__ == "__main__":
    solution = Solution()

    assert to_values(solution.reverseList(build_list([1, 2, 3, 4, 5]))) == [
        5,
        4,
        3,
        2,
        1,
    ]
    assert to_values(solution.reverseList(build_list([1, 2]))) == [2, 1]
    assert solution.reverseList(None) is None
    assert to_values(solution.reverseList(build_list([7]))) == [7]
