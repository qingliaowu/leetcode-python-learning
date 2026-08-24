# Trie Interview Practice

This folder is a guided interview course for someone who is new to Python or has not used it recently. Read this page first, then study the problems in the recommended order. Every problem has:

- a plain-English problem summary
- the Python syntax used by the solution
- a step-by-step approach
- a dry run with a small example
- time and space complexity
- interview talking points and common mistakes
- an executable Python solution with assertions

Use the [interview playbook](../INTERVIEW_PLAYBOOK.md) to practice turning these ideas into a clear solve-out-loud interview answer.

## Recommended Order

| Priority | LeetCode | Lesson | Python Solution | Main Idea |
| --- | ---: | --- | --- | --- |
| 5/5 | 208 | [Implement Trie](./0208_implement_trie.md) | [Code](./0208_implement_trie.py) | Build the basic Trie API |
| 5/5 | 1268 | [Search Suggestions System](./1268_search_suggestions_system.md) | [Code](./1268_search_suggestions_system.py) | Save the best three suggestions at each prefix |
| 4/5 | 211 | [Design Add and Search Words](./0211_design_add_and_search_words.md) | [Code](./0211_design_add_and_search_words.py) | Combine a Trie with recursive wildcard search |
| 3/5 | 648 | [Replace Words](./0648_replace_words.md) | [Code](./0648_replace_words.py) | Stop at the shortest complete prefix |
| 3/5 | 677 | [Map Sum Pairs](./0677_map_sum_pairs.md) | [Code](./0677_map_sum_pairs.py) | Store a running total at each prefix |

## 1. Python Refresher

This section is a quick reference. For slower, step-by-step lessons with runnable examples, start with the full [Python 3 Basics course](../python_basics/). Its [time and space complexity lesson](../python_basics/11_time_and_space_complexity.md) explains every common Big-O term without assuming advanced math.

### Variables and basic values

Python creates a variable when a value is assigned with `=`:

```python
word = "apple"       # str: text
score = 3            # int: whole number
is_word = False      # bool: True or False
missing = None       # no value
```

`=` assigns a value. `==` compares two values. `is None` checks specifically for the special value `None`.

### Lists

A list keeps items in order and can be changed:

```python
suggestions = []
suggestions.append("apple")
suggestions.append("app")

print(suggestions[0])  # apple; list indexes start at 0
print(len(suggestions))  # 2
```

This course uses lists to collect answers, build prefixes, and store suggestions.

### Dictionaries

A dictionary maps a key to a value. Lookup is usually `O(1)` on average.

```python
children = {}
children["a"] = "node for a"

if "a" in children:
    next_node = children["a"]
```

A Trie node uses each character as a key and the next `TrieNode` object as its value. For example, `node.children["a"]` means "follow the edge labeled `a`."

Useful dictionary operations in these solutions:

```python
old_value = values.get("apple", 0)  # return 0 if "apple" is missing

for child in children.values():     # loop through values, not keys
    print(child)
```

### Loops and strings

A `for` loop visits each item in a sequence. A string is a sequence of characters:

```python
for char in "cat":
    print(char)  # prints c, then a, then t
```

Two useful string methods are:

```python
words = "the cattle ran".split()
# ["the", "cattle", "ran"]

sentence = " ".join(words)
# "the cattle ran"
```

`sort()` changes a list in place. Python sorts strings in lexicographical (dictionary-like) order:

```python
products = ["mouse", "mobile", "monitor"]
products.sort()
# ["mobile", "monitor", "mouse"]
```

### Classes, objects, and `self`

A class is a blueprint. An object is one value created from that blueprint.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

node = TrieNode()
```

- `class TrieNode:` starts a class definition.
- `__init__` runs when `TrieNode()` creates an object.
- `self` means "this object."
- `self.children` and `self.is_word` are values stored on that object.
- The colon `:` starts an indented block. Indentation is part of Python syntax.

A method is a function inside a class. Python passes the object as the first argument, `self`:

```python
class Counter:
    def add_one(self):
        self.value += 1
```

### Functions, parameters, and return values

```python
def starts_with_a(word: str) -> bool:
    return word[0] == "a"
```

- `def` defines a function.
- `word` is a parameter.
- `word: str` is a type hint saying that `word` should be text.
- `-> bool` says the function should return `True` or `False`.
- Type hints help readers and tools; Python does not enforce them at runtime.
- `return` ends the function and sends a value back to the caller.

Some files import `List` for more detailed type hints:

```python
from typing import List

def suggestedProducts(
    self, products: List[str], searchWord: str
) -> List[List[str]]:
    pass
```

- `List[str]` means a list of strings.
- `List[List[str]]` means a list whose items are also lists of strings.
- `from typing import List` makes the name `List` available to the file.

LeetCode creates the required class and calls its public methods for you. Keep names such as `Solution`, `Trie`, `insert`, and `startsWith` exactly as the question specifies, even when a name does not follow normal Python naming style.

### Recursion

Recursion happens when a function calls itself. It needs:

1. A base case that stops recursion.
2. A recursive case that moves closer to the base case.

Problem 211 uses recursion because `.` can continue through any child. The character index increases on every call, so the base case is eventually reached.

### The test block

Each solution ends with code like this:

```python
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
```

Python sets `__name__` to `"__main__"` when the file is run directly. `assert` checks that an expression is true; Python raises an error if it is false. This gives each file a few lightweight tests without affecting LeetCode.

Run a solution from the repository root with:

```bash
python3 trie/0208_implement_trie.py
```

No output means all assertions passed.

## 2. What Is a Trie?

A Trie (pronounced "try") stores strings one character at a time. Words with the same prefix share nodes.

After inserting `app`, `apple`, and `bat`, the structure is:

```text
(root)
├── a
│   └── p
│       └── p*          app ends here
│           └── l
│               └── e*  apple ends here
└── b
    └── a
        └── t*          bat ends here
```

`*` represents `is_word = True`. The root does not represent a character; it is the shared starting point.

Why is `is_word` necessary? After inserting `apple`, the path for `app` exists, but `app` should not count as a stored word until it is inserted. The path tells us a prefix exists; `is_word` tells us a complete word exists.

## 3. Core Trie Pattern

Most solutions in this folder repeat the same movement:

```python
node = root

for char in word:
    if char not in node.children:
        node.children[char] = TrieNode()
    node = node.children[char]
```

Read it in plain English:

1. Start at the root.
2. Read one character.
3. Create that path if it does not exist.
4. Move to the child for that character.
5. Repeat for the rest of the word.

`node = node.children[char]` does not copy a node. It changes the local variable `node` so it refers to the next object.

## 4. Complexity Vocabulary

Big-O describes how work grows as input grows.

- `O(1)`: constant work; it does not grow with the input.
- `O(L)`: work grows with the length `L` of one word or prefix.
- `O(T)`: work grows with the total number `T` of characters across all words.
- `O(N log N)`: common sorting cost for `N` items.

A Trie usually handles a word in `O(L)` time because it visits each character once. It uses extra memory for nodes. Shared prefixes reuse nodes, but the worst-case space is `O(T)`.

## 5. Interview Checklist

Before coding, explain:

1. What each node stores.
2. What one path from the root represents.
3. Why a Trie helps this particular query.
4. What happens when a character path is missing.
5. What marks a complete word or stores extra state.

While coding, use descriptive names such as `node`, `char`, `prefix`, and `suggestions`. After coding, test an exact word, a prefix, a missing path, and any update or wildcard behavior required by the problem.
