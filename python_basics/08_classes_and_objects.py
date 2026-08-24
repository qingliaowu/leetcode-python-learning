"""Lesson 8: create classes and store data on objects."""


class Counter:
    """A small object that remembers a number."""

    def __init__(self, start: int = 0):
        self.value = start

    def add_one(self) -> None:
        self.value += 1

    def current(self) -> int:
        return self.value


first_counter = Counter()
second_counter = Counter(10)

first_counter.add_one()
first_counter.add_one()
second_counter.add_one()

assert first_counter.current() == 2
assert second_counter.current() == 11


class ListNode:
    """One node in a singly linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


second = ListNode(2)
first = ListNode(1, second)

assert first.val == 1
assert first.next is second
assert first.next.val == 2

print("Lesson 8 checks passed.")
