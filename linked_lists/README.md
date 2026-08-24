# Linked Lists for Beginners

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md) | [FDE track](../fde_interview/README.md) | [AI engineering](../ai_engineering/README.md)

A linked list stores values in separate node objects connected by references.
Unlike a Python list, it has no constant-time index lookup. Its strength is
changing known links without shifting every later value.

## Recommended Order

| LeetCode | Lesson | Python Solution | Main Pattern |
| ---: | --- | --- | --- |
| 206 | [Reverse Linked List](./0206_reverse_linked_list.md) | [Code](./0206_reverse_linked_list.py) | Save, reverse, and advance three references |

Before starting, review [Classes and Objects](../python_basics/08_classes_and_objects.md). The [Merge K Sorted Lists](../heaps/0023_merge_k_sorted_lists.md) lesson later combines linked nodes with a heap.

## Node Vocabulary

```text
head     reference to the first node
next     reference from one node to the following node
tail     final node, whose next is None
None     marks an empty list or the end
```

## Recognize the Pattern

Linked-list questions often require:

- preserving a next reference before changing it,
- a dummy node to simplify first-node changes,
- slow and fast references for a middle or cycle,
- reconnecting a segment at both boundaries,
- comparing node identity rather than repeated values.

Draw nodes and arrows. Pointer code becomes much easier when every reference has
one sentence meaning.

## Ready to Move On

You are ready when you can trace `previous`, `current`, and `next_node` without
losing the remaining list; explain mutation versus copying; and test empty, one-
node, and two-node lists. Continue to [Intervals, Sorting, and Binary Search](../intervals_search/README.md).
