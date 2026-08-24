# 208. Implement Trie

[LeetCode problem](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Python solution](./0208_implement_trie.py)

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
