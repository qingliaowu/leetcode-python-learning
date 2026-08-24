# 677. Map Sum Pairs

[LeetCode problem](https://leetcode.com/problems/map-sum-pairs/) | [Python solution](./0677_map_sum_pairs.py)

## What the Question Asks

Store string keys with integer values. Given a prefix, return the sum of values for all keys that start with it.

```text
insert("apple", 3)
sum("ap") -> 3

insert("app", 2)
sum("ap") -> 5
```

Inserting an existing key replaces its old value; it does not create a second copy.

## Python Used Here

### Dictionary lookup with a default

```python
old_value = self.values.get(key, 0)
```

`dict.get(key, default)` returns the stored value when the key exists. Otherwise, it returns the provided default, `0`, without raising an error.

### Updating a number

```python
node.total += difference
```

`+=` is shorthand for:

```python
node.total = node.total + difference
```

The difference may be positive, zero, or negative.

## Main Idea

Every Trie node represents a prefix. Store the sum for that prefix directly on the node:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.total = 0
```

Then `sum(prefix)` only needs to reach one node and return its `total`. It does not need to find every full key below that prefix.

The difficult part is replacing an existing key correctly.

## Why the Difference Is Necessary

Suppose `apple` currently has value `3`, and it is updated to `2`.

Adding `2` again to every prefix would make the `ap` total become `5`, as though both versions existed. The old contribution must be replaced.

Calculate:

```text
difference = new value - old value
           = 2 - 3
           = -1
```

Adding `-1` to every node on the `apple` path changes each total from its old state to the correct new state.

`self.values` remembers the exact current value of every complete key so this difference can be calculated.

## Step-by-Step Approach

### Insert or update a key

1. Read the old key value from `self.values`, using `0` if the key is new.
2. Calculate `difference = val - old_value`.
3. Save the new exact value in `self.values`.
4. Start at the root.
5. Follow or create every node in the key.
6. Add `difference` to the total at every visited node.

The solution also updates the root total. That represents the sum for an empty prefix and does not hurt normal non-empty-prefix queries.

### Sum a prefix

1. Start at the root.
2. Follow each prefix character.
3. Return `0` if a path is missing because no stored key has that prefix.
4. Return the final node's `total` if the whole prefix exists.

## Dry Run

### Insert `apple = 3`

The old value is `0`, so the difference is `3`. Add `3` along:

```text
a -> ap -> app -> appl -> apple
```

Now `sum("ap")` is `3`.

### Insert `app = 2`

The old value is `0`, so the difference is `2`. Add `2` along:

```text
a -> ap -> app
```

The `ap` total becomes `5`, while `appl` remains `3` because `app` does not pass through it.

### Update `apple = 2`

The old value is `3`, so the difference is `-1`. Subtract `1` along the whole `apple` path. The `ap` total becomes `4`, representing:

```text
apple: 2
app:   2
total: 4
```

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `L` be the key length and `P` be the prefix length.

- `insert`: `O(L)` time.
- `sum`: `O(P)` time.
- Space: `O(T)` for Trie nodes plus `O(K)` for exact key values, where `T` is total inserted character count and `K` is the number of distinct keys.

This design makes both operations fast by doing the sum maintenance during insertion.

## Common Mistakes

- Adding the new value again when a key is updated instead of adding the difference.
- Forgetting the separate `values` dictionary needed to find the old value.
- Calculating `old_value - val`, which reverses the update direction.
- Storing totals only on final key nodes; every prefix node needs its own total.
- Searching every descendant during `sum`, which throws away the benefit of cached totals.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| How would you delete a key? | Look up its old value, propagate the negative of that value through its Trie path, remove it from the exact-value map, and optionally prune unused nodes. |
| Do negative values still work? | Yes. The update difference can be positive or negative, and every prefix total changes by that exact difference. |
| How would you return the matching keys as well as their sum? | Walk to the prefix node and DFS through its descendants to collect complete keys. Runtime must include the number and length of returned keys. |
| What if the same key is updated very frequently? | The difference technique already handles this in `O(L)` per update without rescanning other keys. Explain why storing the old exact value is essential. |
| How would wildcard prefix queries work? | Search all Trie branches allowed by each wildcard and add the totals of the matching prefix nodes, taking care not to count one subtree twice. |

## How to Explain It in an Interview

> I will store a running sum at every Trie node, so a prefix query only traverses the prefix and returns one number. To support replacing a key, I keep its current value in a hash map and propagate only `new minus old` along the key path. Both insert and sum are linear in the length of their input string.

## Practice Checks

Work out the totals after these operations:

```text
insert("car", 4)
insert("card", 3)
insert("cat", 2)
sum("ca")       -> 9
sum("car")      -> 7
insert("car", 1)
sum("ca")       -> 6
sum("dog")      -> 0
```

## Check Your Understanding

Try each question before opening its answer. Calculate the update difference before touching any prefix total.

### Question 1: Update an Existing Key

Trace these operations:

```text
insert("apple", 3)
insert("app", 2)
sum("ap")
insert("apple", 1)
sum("ap")
sum("apple")
```

What do the three sums return?

<details>
<summary>Show answer and explanation</summary>

**Answer:** The sums return `5`, `3`, and `1`.

Initially, keys `"apple"` and `"app"` contribute `3 + 2 = 5` below prefix `"ap"`. Updating `"apple"` from `3` to `1` produces a difference of `-2`. Every node on the `"apple"` path subtracts `2`, so prefix `"ap"` becomes `3`. Prefix `"apple"` contains only that exact key and returns `1`.

Adding the new value directly would incorrectly make `"apple"` contribute both its old and new values.

**Complexity:** Insert is `O(L)` for key length `L`; sum is `O(P)` for prefix length `P`.

**Edge case:** Querying a missing prefix returns `0`.

</details>

### Question 2: Build a Simple Baseline Without a Trie

Implement the same behavior with only a dictionary. This solution is slower for prefix queries but helps verify the required semantics.

<details>
<summary>Show answer and detailed solution</summary>

```python
class SimpleMapSum:
    def __init__(self):
        self.values: dict[str, int] = {}

    def insert(self, key: str, value: int) -> None:
        self.values[key] = value

    def sum(self, prefix: str) -> int:
        total = 0
        for key, value in self.values.items():
            if key.startswith(prefix):
                total += value
        return total
```

The dictionary naturally replaces the old value when the same key is inserted again, so update semantics are easy. A prefix query must inspect every stored key, which shows exactly what the Trie optimization avoids.

This baseline is useful in an interview: first establish correct behavior simply, then optimize the expensive operation when constraints require it.

**Complexity:** Insert takes `O(L)` time to hash a key of length `L`, followed by an average `O(1)` dictionary update. A sum query is `O(K * L)` in a simple bound for `K` keys of average length `L`.

**Test:** Insert `("apple", 3)`, then `("apple", 1)`; `sum("app")` returns `1`, not `4`.

</details>
