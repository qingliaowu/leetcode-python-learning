# 146. LRU Cache

[LeetCode problem](https://leetcode.com/problems/lru-cache/) | [Python solution](./0146_lru_cache.py) | [Design guide](./README.md)

## What the Question Asks

Create a fixed-capacity cache with:

- `get(key)`: return the value or `-1` when missing.
- `put(key, value)`: insert or update a value.

Both operations must run in `O(1)` average time. When a new key exceeds capacity, remove the least recently used key.

Using a key with either `get` or `put` makes it the most recently used key.

## Why One Data Structure Is Not Enough

A dictionary gives `O(1)` average key lookup, but it does not directly give `O(1)` movement and eviction in usage order.

A doubly linked list gives `O(1)` removal and insertion when a node is already known, but finding a key by scanning it would be `O(N)`.

Combine them:

```text
dictionary: key -> linked-list node
linked list: least recent -> ... -> most recent
```

The dictionary finds a node. The list maintains order.

## The Invariant

After every public operation:

```text
1. The dictionary and list contain exactly the same real cache entries.
2. Entries run from least recently used on the left to most recently used on
   the right.
3. The number of entries never exceeds capacity.
```

## Doubly Linked List Refresher

Each node stores links in both directions:

```text
previous <- node -> next
```

To remove `node`, connect its neighbors directly:

```python
before.next = after
after.previous = before
```

This is `O(1)` because no list scan or item shifting is needed.

## Why Use Sentinel Nodes?

The cache keeps permanent empty nodes at both ends:

```text
least_recent sentinel <-> real entries <-> most_recent sentinel
```

Sentinels are not cache data. They remove special cases for an empty list, first node, or last node. Every real node always has both a previous and next node.

## Get Step by Step

1. Return `-1` if the key is absent from the dictionary.
2. Get its node from the dictionary.
3. Remove the node from its current list position.
4. Add it beside the most-recent sentinel.
5. Return its value.

Reading a key counts as use, so its position must change.

## Put Step by Step

For an existing key:

1. Update its node value.
2. Move that node to the most-recent end.

For a new key:

1. Create a node.
2. Add it to the dictionary.
3. Add it at the most-recent end.

After either path, if size exceeds capacity, remove `least_recent.next`, which is the least recently used real node. Delete the same key from the dictionary.

## Dry Run

Capacity is `2`:

```text
put(1, 1)   order: [1]
put(2, 2)   order: [1, 2]
get(1)      order: [2, 1]  because 1 was just used
put(3, 3)   order: [1, 3]  because 2 was least recent and is evicted
get(2)      returns -1
```

The rightmost real key is most recent.

## Python Used Here

```python
del self.nodes[node_to_remove.key]
```

`del` removes one dictionary entry.

Assignments such as `before.next = node` change object references. They do not copy nodes.

Helper methods begin with `_` to signal that they are internal implementation details rather than public cache operations.

## Why It Is Correct

Every successful `get` and every `put` moves its node to the most-recent end, so list order always matches usage order. The leftmost real node is therefore the correct eviction target. The dictionary and list are updated together, so every stored key has exactly one reachable node.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `C` be cache capacity.

- `get`: `O(1)` average dictionary lookup plus constant pointer changes.
- `put`: `O(1)` average lookup, insertion, movement, and at most one eviction.
- Space: `O(C)` for at most `C` dictionary entries and real nodes.

## Edge Cases

- Missing key returns `-1` without changing order.
- Updating an existing key changes its value and recency but not cache size.
- Reading a key changes recency.
- Capacity `1` evicts the previous key whenever a different key is inserted.
- Repeatedly reading one key protects it from being least recent.

## Common Mistakes

- Using only a dictionary and trying to find the oldest key by scanning.
- Forgetting that `get` changes recency.
- Creating a second node when updating an existing key.
- Removing a node from the list but not the dictionary, or the reverse.
- Evicting the most recent node instead of the least recent node.
- Mishandling first or last nodes by not using sentinels.

## Interview Explanation

> I need constant-time key lookup and constant-time ordering updates, so I combine a hash map with a doubly linked list. The map points keys to nodes. The list runs from least to most recent, and sentinels simplify pointer changes. Every get or put moves one node to the recent end, and overflow removes the leftmost real node. Both operations are `O(1)` average time with `O(capacity)` space.

## Test Aloud

```text
With capacity 2, after putting keys 1 and 2, getting key 1 moves it to most
recent. Putting key 3 must therefore evict key 2. A later get(2) returns -1.
```
