# 981. Time Based Key-Value Store

[LeetCode problem](https://leetcode.com/problems/time-based-key-value-store/) | [Python solution](./0981_time_based_key_value_store.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Create a `TimeMap` class with two operations:

- `set(key, value, timestamp)` saves a value at a time.
- `get(key, timestamp)` returns the value with the largest saved timestamp that is less than or equal to the requested timestamp.

Return an empty string when no saved value is old enough.

```text
set("foo", "bar", 1)
set("foo", "bar2", 4)

get("foo", 3) -> "bar"
get("foo", 4) -> "bar2"
get("foo", 9) -> "bar2"
```

## Clarify the Important Guarantee

The problem guarantees that timestamps passed to `set` are strictly increasing. Therefore, appending entries keeps every key's history sorted by time. No sorting is needed later.

## Stored State

Use one dictionary:

```python
self.history = {}
```

Each key maps to a list of `(timestamp, value)` tuples:

```text
"foo" -> [(1, "bar"), (4, "bar2"), (8, "bar3")]
```

The list is sorted because entries arrive in time order.

## The Invariant

```text
For every key, history[key] is sorted from smallest timestamp to largest.
```

`set` preserves this invariant by appending. `get` relies on it for binary search.

## Python Used Here

```python
self.history[key].append((timestamp, value))
```

The parentheses create a tuple containing two related values. The list stores these tuples in order.

```python
entries = self.history.get(key, [])
```

If the key is missing, `get` returns a new empty list instead of raising `KeyError`.

Tuple unpacking gives both saved values names:

```python
saved_time, saved_value = entries[middle]
```

## Why Binary Search Is Slightly Different Here

Normal binary search looks for an exact value. This search wants the rightmost timestamp that is at most the request.

When `saved_time <= timestamp`:

1. The current entry is a valid answer.
2. Save its value.
3. Search to the right for a newer valid entry.

When `saved_time > timestamp`, the entry is too new. Search left.

## Dry Run

History for `"foo"`:

```text
index:      0          1           2
entry:   (1,bar)    (4,bar2)    (8,bar3)
```

Get timestamp `6`:

1. Middle timestamp is `4`. It is valid, so save `"bar2"` and search right.
2. Next middle timestamp is `8`. It is too new, so search left.
3. The range is empty. Return the last saved valid answer, `"bar2"`.

## Why It Is Correct

The history is sorted. Whenever the middle timestamp is valid, every entry to its left is older, so the middle value is at least as good; the search keeps it and looks for something newer on the right. When the middle is too new, every entry to its right is also too new, so that half can be discarded.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `M` be the number of values stored for the requested key and `S` the total number of saved entries.

- `set`: `O(1)` average time because it performs a dictionary lookup and list append.
- `get`: `O(log M)` time because binary search halves one key's history.
- Extra stored space: `O(S)` across all keys.

## Assumptions to Say Aloud

- Timestamps supplied to `set` are strictly increasing for each key, so each
  history list stays sorted without insertion work.
- `get` returns the value at the greatest timestamp less than or equal to the
  query timestamp.
- A missing key or a query earlier than its first value returns `""`.
- Different keys have independent histories.

## Edge Cases

- Missing key: return `""`.
- Requested time before the key's first timestamp: return `""`.
- Exact timestamp: return that entry.
- Time between entries: return the earlier entry.
- Time after every entry: return the newest entry.
- Different keys keep independent histories.

## Common Mistakes

- Returning only exact timestamp matches.
- Searching all entries linearly and missing the intended binary search.
- Searching right after finding an entry that is too new.
- Forgetting to save a valid middle value before continuing right.
- Mixing histories from different keys.
- Sorting on every `set` despite the increasing-timestamp guarantee.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| What if timestamps arrive out of order? | Plain append no longer preserves sorting. Insert with `bisect` in `O(M)` list time or use an ordered-tree data structure. |
| Return every value in a timestamp range. | Use two binary searches to find the first and last relevant indexes, then return that slice. |
| How would deletion work? | Define whether deletion removes history or adds a timestamped tombstone. A tombstone preserves historical queries. |
| How would you make it persistent or thread-safe? | Store histories in durable storage and protect each read-update sequence with appropriate locking or transactional operations. |

## Interview Explanation

> I map each key to a list of timestamp-value pairs. Set timestamps arrive in increasing order, so appending keeps each list sorted in constant average time. Get runs a modified binary search for the rightmost timestamp no greater than the request. It takes `O(log M)` time for `M` values under that key.

## Test Aloud

```text
For history [(1, bar), (4, bar2)] and request 3, timestamp 1 is the newest
valid entry. Timestamp 4 is too new, so the method returns bar.
```

## Check Your Understanding

Try each question before opening its answer. State the binary-search condition in plain English.

### Question 1: Query Several Times

After `set("mode", "day", 1)` and `set("mode", "night", 4)`, what should `get` return at timestamps `0`, `1`, `3`, `4`, and `8`?

<details>
<summary>Show answer and explanation</summary>

**Answer:** The results are `""`, `"day"`, `"day"`, `"night"`, and `"night"`.

The query wants the value with the greatest stored timestamp that is less than or equal to the requested time. There is no valid entry at time `0`. Times `1` and `3` use the entry from time `1`. Starting at time `4`, the newer value is valid.

This is a rightmost-valid binary search, not a search for an exact timestamp.

**Complexity:** Each query takes `O(log M)` time for `M` versions of that key and `O(1)` extra space.

**Edge case:** A missing key or a time before its first value returns the required empty default.

</details>

### Question 2: Look Up Historical Prices

Complete a function that receives one sorted history of `(timestamp, price)` pairs and returns the newest price at or before `query_time`, or `None` if there is none.

<details>
<summary>Show answer and detailed solution</summary>

```python
def price_at_or_before(
    history: list[tuple[int, float]], query_time: int
) -> float | None:
    left = 0
    right = len(history) - 1
    answer = None

    while left <= right:
        middle = (left + right) // 2
        timestamp, price = history[middle]

        if timestamp <= query_time:
            answer = price
            left = middle + 1
        else:
            right = middle - 1

    return answer
```

Whenever `timestamp <= query_time`, that price is valid, but a newer valid price may exist to the right. The function saves the candidate and continues right. If the middle timestamp is too new, every timestamp to its right is also too new, so it searches left.

**Complexity:** `O(log M)` time and `O(1)` extra space.

**Tests:** For `[(2, 10.0), (5, 12.5)]`, time `4` returns `10.0`, time `5` returns `12.5`, and time `1` returns `None`.

</details>
