# Lesson 5: Dictionaries and Sets

[Run this lesson](./05_dictionaries_and_sets.py) | [Course home](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Use fast lookup to map keys to values, count items, and store unique values.

## Dictionaries

A dictionary maps each unique key to one value:

```python
scores = {
    "Ada": 10,
    "Grace": 8,
}
```

Think of it as a real dictionary: find a word (key) to get its definition (value).

## Read, Add, and Update

```python
scores["Ada"]          # read 10
scores["Linus"] = 9   # add a new key
scores["Ada"] = 11    # replace an existing value
```

Reading a missing key with `scores["Missing"]` raises `KeyError`.

Use `get` when a key may be missing:

```python
scores.get("Missing", 0)  # returns 0
```

## Membership

```python
if "Ada" in scores:
    print("Ada has a score")
```

For a dictionary, `in` checks keys, not values. Dictionary lookup is `O(1)` on average, which is why hash maps solve many interview problems.

## Counting Pattern

The `for` loop below means "repeat once for every character." Loops are explained fully in Lesson 6; for now, focus on the dictionary update inside it.

```python
counts = {}

for letter in "apple":
    counts[letter] = counts.get(letter, 0) + 1
```

Result:

```python
{"a": 1, "p": 2, "l": 1, "e": 1}
```

Read the update as: "get the old count, use zero if missing, then add one."

## Loop Through a Dictionary

```python
for key in scores:
    print(key)

for key, value in scores.items():
    print(key, value)

for value in scores.values():
    print(value)
```

`.items()` provides key-value pairs. `.values()` provides only values.

## Sets

A set stores unique values:

```python
numbers = {1, 2, 2, 3}
# {1, 2, 3}

numbers.add(4)
numbers.remove(2)
```

Sets are useful when only membership matters, not an attached value.

```python
seen = set()
seen.add("a")

if "a" in seen:
    print("Already seen")
```

Create an empty set with `set()`. `{}` creates an empty dictionary.

## Dictionary or Set?

| Need | Use |
| --- | --- |
| Map a number to its index | Dictionary |
| Count each character | Dictionary |
| Remember only whether something appeared | Set |
| Remove duplicate values | Set |

## Try It

What is `counts`?

```python
counts = {}
for number in [2, 2, 3]:
    counts[number] = counts.get(number, 0) + 1
```

Answer: `{2: 2, 3: 1}`.

## Common Mistakes

- Reading a missing key without checking or using `get`.
- Thinking `in dictionary` checks values.
- Using `{}` when you need an empty set.
- Expecting a set to keep duplicate values or support indexing.
- Overwriting a count with `1` every time instead of adding one.

## Remember

A dictionary stores key-value relationships. A set stores unique values. Both provide fast average membership lookup.
