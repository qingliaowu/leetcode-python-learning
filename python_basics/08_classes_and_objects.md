# Lesson 8: Classes and Objects

[Run this lesson](./08_classes_and_objects.py) | [Course home](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Create your own value type and understand the node objects used by linked lists, trees, graphs, and Tries.

## Class and Object

A class is a blueprint. An object is one value built from that blueprint.

```python
class Counter:
    pass

first = Counter()
second = Counter()
```

`pass` is a placeholder meaning "do nothing yet." It lets this tiny class example run before behavior is added below.

`first` and `second` are different objects of the same class.

## Initialize an Object

```python
class Counter:
    def __init__(self, start=0):
        self.value = start
```

`__init__` runs automatically when `Counter()` creates an object.

```python
first = Counter()     # value starts at 0
second = Counter(10)  # value starts at 10
```

`self` means "this object." `self.value` stores a value on that particular object.

## Methods

A method is a function inside a class:

```python
class Counter:
    def add_one(self):
        self.value += 1

counter = Counter()
counter.add_one()
```

Python passes `counter` into the `self` parameter automatically. You do not write `counter.add_one(counter)`.

## Objects Remember Separate State

```python
first = Counter()
second = Counter()

first.add_one()
```

Only `first.value` changes. Every object has its own attributes.

## Linked-List Node

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Build `1 -> 2`:

```python
second = ListNode(2)
first = ListNode(1, second)
```

`first.next` refers to the `second` object. `first.next.val` is `2`.

Tree nodes and Trie nodes use the same idea: one object stores a value and references to other objects.

[Python Data Structures Made Simple](./12_python_data_structures.md#10-linked-lists-and-trees-nodes-connected-by-references)
later compares node structures with lists, dictionaries, sets, queues, and heaps.

## Object References

```python
alias = first
```

This does not clone the object. `alias` and `first` refer to the same object. A deep-copy problem such as Clone Graph must explicitly create new objects.

## LeetCode Classes

LeetCode often provides helper classes such as `ListNode`, `TreeNode`, or `Node`. Use their attributes rather than redefining them in the submitted solution.

Other questions ask you to design the class itself, such as `Trie`, `WordDictionary`, or `MapSum`.

## Try It

What is `box.value`?

```python
class Box:
    def __init__(self, value):
        self.value = value

box = Box(5)
box.value += 2
```

<details>
<summary>Show answer and explanation</summary>

`box.value` is `7`.

`Box(5)` creates one object and `__init__` stores `5` in that object's `value`
attribute. The `+= 2` update reads `5`, adds `2`, and stores `7` back on the
same object.

</details>

## Common Mistakes

- Forgetting `self` as the first method parameter.
- Writing `value = start` instead of `self.value = start` when state must remain on the object.
- Thinking two calls to a class create the same object.
- Thinking assignment creates a deep copy.
- Calling `__init__` directly instead of calling the class.

## Remember

A class defines behavior and stored attributes. An object is one instance. `self` refers to the current instance.

---

[Previous: Lesson 7, Functions](./07_functions.md) | [Next: Lesson 9, Recursion](./09_recursion.md)
