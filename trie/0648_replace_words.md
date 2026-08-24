# 648. Replace Words

[LeetCode problem](https://leetcode.com/problems/replace-words/) | [Python solution](./0648_replace_words.py)

## What the Question Asks

A dictionary contains short roots such as `cat`, `bat`, and `rat`. Replace each word in a sentence with the shortest root that is its prefix.

```text
"the cattle was rattled by the battery"
->
"the cat was rat by the bat"
```

Words with no matching root stay unchanged.

## Python Used Here

### Splitting a sentence

```python
for word in sentence.split():
```

`split()` without an argument separates text on whitespace and returns a list of words.

### Building a result list

```python
replaced_words = []
replaced_words.append(replacement)
```

The output words are collected in order. Building a list and joining once is clearer and more efficient than repeatedly adding strings.

### Joining strings

```python
return " ".join(replaced_words)
```

`join` places one space between each list item and returns a single string.

The same method converts prefix characters into a word:

```python
return "".join(prefix)
```

An empty separator joins characters with nothing between them.

## Why a Trie Fits

For every sentence word, the question asks about prefixes from shortest to longest. A Trie follows those prefixes naturally one character at a time.

As soon as traversal reaches a node with `is_word = True`, the shortest matching root has been found. There is no reason to continue.

## Step-by-Step Approach

### Build the Trie

Insert every root from `dictionary`. Each final root node gets `is_word = True`.

### Replace one word

`_find_shortest_root(root, word)` does the following:

1. Start at the root with an empty `prefix` list.
2. Read one character from `word`.
3. If its child path is missing, no dictionary root can match; return the original word.
4. Add the character to `prefix` and move to the child.
5. If that node ends a root, return the joined prefix immediately.
6. If the loop finishes without finding a root, return the original word.

### Rebuild the sentence

Split the sentence, replace each word, then join all replacement results with spaces.

## Dry Run: `cattle`

Assume `cat` is in the root dictionary.

| Character read | Prefix | Trie path exists? | Complete root? |
| --- | --- | --- | --- |
| `c` | `c` | Yes | No |
| `a` | `ca` | Yes | No |
| `t` | `cat` | Yes | Yes |

Return `cat` immediately. The remaining letters `tle` do not matter.

Now try `dog`. If root child `d` is missing, return `dog` immediately.

If both `cat` and `c` are dictionary roots, traversal reaches `c` first and returns it. This correctly chooses the shortest root regardless of dictionary insertion order.

## Complexity

Let:

- `T` be the total characters in all dictionary roots,
- `S` be the total characters in the sentence.

Then:

- Building the Trie: `O(T)` time.
- Replacing all words: `O(S)` time in the worst case.
- Trie space: `O(T)`.
- Output and temporary word storage also use space proportional to the sentence.

The search often stops before reading a whole word because it finds a root or missing path early.

## Common Mistakes

- Continuing after finding a complete root and accidentally returning a longer root.
- Replacing a word when the Trie path exists but no `is_word` marker was reached.
- Returning the partial prefix when a path becomes missing.
- Forgetting to preserve words with no matching root.
- Joining output words without spaces or returning the list instead of a string.

## How to Explain It in an Interview

> I will insert all dictionary roots into a Trie. For each sentence word, I traverse from its first character and return as soon as I reach a complete-root marker, which guarantees the shortest root. If a path is missing or no marker is reached, I keep the original word. Building and querying are linear in the total characters processed.

## Practice Checks

Think through these cases:

```text
dictionary = ["a", "aa", "aaa"]
sentence = "a aa aaaa b"
result = "a a a b"
```

The first complete marker always wins.
