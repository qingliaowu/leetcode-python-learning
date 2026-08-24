# 208. Implement Trie

[LeetCode problem](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Python solution](./0208_implement_trie.py) | [Topic guide](./README.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## What the Question Asks

Create a `Trie` class with three operations:

- `insert(word)`: save a word.
- `search(word)`: return `True` only if the complete word was saved.
- `startsWith(prefix)`: return `True` if any saved word begins with the prefix.

This is the foundation for all the other problems in this folder.

## Python Used Here

```python
if char not in node.children:
    node.children[char] = TrieNode()
```

`node.children` is a dictionary. The condition asks whether the current character is missing. If it is missing, the next Trie node is created and stored under that character.

```python
node = node.children[char]
```

This moves the `node` variable forward by one character. Python variables that refer to objects do not contain a separate copy of the object, so changing `node` does not change `self.root`.

```python
return node is not None and node.is_word
```

`and` evaluates from left to right. If `node is not None` is false, Python stops and returns `False`. This short-circuit behavior prevents an attempt to read `is_word` from `None`.

## Data Stored in Each Node

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
```

- `children` stores the possible next characters.
- `is_word` records whether a word ends at this exact node.

The `Trie` object owns one empty root node:

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
```

Every operation starts at this root.

## Step-by-Step Approach

### Insert

1. Start at the root.
2. Loop through the word one character at a time.
3. Create a child node if the character path is missing.
4. Move to that child.
5. After the loop, mark the final node with `is_word = True`.

The flag is set after the loop because the final node represents the entire word.

### Find a node

`_find_node(text)` contains the shared traversal used by both query methods:

1. Start at the root.
2. Follow every character in `text`.
3. Return `None` immediately if a path is missing.
4. Return the last node if the whole path exists.

The leading underscore in `_find_node` is a Python convention meaning "internal helper." It does not make the method truly private.

### Search versus startsWith

Both methods first check whether the path exists. They differ at the end:

- `search("app")` also requires `is_word = True` on the final node.
- `startsWith("app")` only requires the path to exist.

## Dry Run

Insert `apple`:

```text
root -> a -> p -> p -> l -> e*
```

Now consider three queries:

| Query | Path exists? | Final `is_word` | Result |
| --- | --- | --- | --- |
| `search("apple")` | Yes | `True` | `True` |
| `search("app")` | Yes | `False` | `False` |
| `startsWith("app")` | Yes | Not required | `True` |

After inserting `app`, its final `p` node is marked, so `search("app")` becomes `True`. No nodes need to be rebuilt.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `L` be the length of the word or prefix.

- `insert`: `O(L)` time because every character is visited once.
- `search`: `O(L)` time.
- `startsWith`: `O(L)` time.
- Space: `O(T)`, where `T` is the total number of inserted characters in the worst case.

Shared prefixes reduce the number of nodes in practice. For example, `app` and `apple` share the first three character nodes.

## Common Mistakes

- Forgetting to set `is_word = True` after insertion.
- Returning `True` from `search` just because a prefix path exists.
- Starting each operation from the current node instead of `self.root`.
- Creating nodes during `search`; query methods should only follow existing nodes.
- Returning `False` too early during insertion when one child already exists.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| How would you delete a word? | Follow its path, unmark the final `is_word`, and remove nodes from the end only while they have no children and do not end another word. The work is `O(L)`. |
| How would you count words that start with a prefix? | Store a `prefix_count` in every node and update it during insert and delete. A query then takes `O(P)`, where `P` is the prefix length. |
| How would you return autocomplete suggestions? | Reach the prefix node, then run DFS below it and collect complete words. The time includes the prefix walk plus the characters in the returned results. |
| What changes for Unicode or a very large alphabet? | A dictionary of children still works because it creates entries only for characters that appear. A fixed 26-slot list is faster only when the alphabet is known and small. |
| How could you reduce memory for long paths with no branches? | Use a compressed Trie, also called a radix tree, which stores a whole string segment on one edge instead of one node per character. |

## How to Explain It in an Interview

> I will use a Trie node with a dictionary of children and a boolean end marker. Insert follows or creates one node per character, then marks the last node as a complete word. Search and prefix search share the same traversal, but exact search also checks the end marker. Each operation takes linear time in the input string length.

## Practice Checks

Before moving on, explain why each result is correct:

```python
trie = Trie()
trie.insert("car")
trie.insert("card")

trie.search("car")       # True
trie.search("ca")        # False
trie.startsWith("ca")    # True
trie.search("care")      # False
```

## Check Your Understanding

Try each question before opening its answer. Draw one node per character and mark complete words clearly.

### Question 1: Path Versus Complete Word

After inserting `"app"` and `"apple"`, what should these calls return?

```text
search("app")
search("ap")
startsWith("ap")
search("apple")
startsWith("applepie")
```

<details>
<summary>Show answer and explanation</summary>

**Answer:** `True`, `False`, `True`, `True`, and `False`.

The characters `a -> p -> p` form a path whose final node is marked as a word. The shorter path `a -> p` exists but has no word marker, so exact search for `"ap"` is false while prefix search is true. `"apple"` has both a complete path and an end marker. The path fails when `"applepie"` reaches its first character beyond `"apple"`.

This is the central Trie distinction: a path proves a prefix exists; an end marker proves a whole inserted word exists.

**Complexity:** Every call takes `O(L)` time for an input string of length `L`.

**Edge case:** The behavior of an empty string depends on whether inserting it is allowed and whether the root can be marked as a word.

</details>

### Question 2: Count Words Under a Prefix

Using the lesson's Trie node structure, count how many stored words begin with a prefix. This version traverses the matching subtree instead of storing counters.

<details>
<summary>Show answer and detailed solution</summary>

```python
def count_words_with_prefix(trie: "Trie", prefix: str) -> int:
    node = trie.root

    for character in prefix:
        if character not in node.children:
            return 0
        node = node.children[character]

    def count_words(current: "TrieNode") -> int:
        total = 1 if current.is_word else 0
        for child in current.children.values():
            total += count_words(child)
        return total

    return count_words(node)
```

The first loop reaches the node representing the requested prefix. If that path does not exist, no word can match. DFS then counts every end marker in the subtree, including the prefix node itself when the prefix is also a complete word.

**Complexity:** `O(P + S)` time, where `P` is the prefix length and `S` is the number of Trie nodes visited below it. Recursion uses up to the subtree height in stack space.

**Test:** After inserting `"app"`, `"apple"`, and `"apt"`, prefix `"ap"` returns `3`, while `"apple"` returns `1`.

</details>
