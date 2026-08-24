# 211. Design Add and Search Words

[LeetCode problem](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | [Python solution](./0211_design_add_and_search_words.py)

## What the Question Asks

Create a data structure that can add words and search for patterns. A lowercase letter matches itself, while `.` matches any one character.

Examples after adding `bad`, `dad`, and `mad`:

```text
search("bad") -> True
search("pad") -> False
search(".ad") -> True
search("b..") -> True
```

The wildcard represents exactly one character, not zero or many characters.

## Python Used Here

### Indexing a string

```python
char = word[index]
```

An index is a numeric position starting at `0`. For `word = "bad"`, `word[0]` is `"b"`, `word[1]` is `"a"`, and `word[2]` is `"d"`.

### Looping through dictionary values

```python
for child in node.children.values():
```

`children.values()` provides the child node objects. The character keys are not needed when `.` can match every child.

### Recursion and short-circuit return

```python
if self._dfs(word, index + 1, child):
    return True
```

The method calls itself for the next character. As soon as any branch finds a complete match, it returns `True` and no other branches need to be explored.

## Why Normal Trie Search Is Not Enough

For a letter such as `b`, there is only one possible next edge. For `.`, there may be many possible edges. The algorithm must explore each possibility until one succeeds or all fail.

This is depth-first search (DFS): follow one possible path forward, then try another path if the first one fails.

## Step-by-Step Approach

Adding a word is identical to problem 208:

1. Start at the root.
2. Follow or create one node per character.
3. Mark the final node as a complete word.

Searching uses `_dfs(word, index, node)`. Its three cases are:

### Case 1: The pattern is finished

```python
if index == len(word):
    return node.is_word
```

This is the recursion base case. Matching every pattern character is not enough by itself; the current node must also end a saved word.

### Case 2: The current character is `.`

Try the next pattern position from every child. Return `True` if any child succeeds. Return `False` only after every child fails.

### Case 3: The current character is a letter

Return `False` if that child path is absent. Otherwise, recurse into the matching child with `index + 1`.

Increasing `index` is important: every recursive call gets closer to the base case.

## Dry Run: `.ad`

Assume the Trie stores `bad`, `dad`, and `mad`.

1. At index `0`, the pattern is `.`. Try root children `b`, `d`, and `m`.
2. Follow `b`. At index `1`, the required character is `a`, and that child exists.
3. At index `2`, the required character is `d`, and that child exists.
4. The index becomes `3`, equal to the pattern length.
5. The final node has `is_word = True`, so the search returns `True`.

Because one branch succeeded, DFS does not need to try `dad` or `mad`.

For `.at`, DFS may try several first letters, but every branch eventually fails because no matching final path is stored.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let `L` be the word or pattern length.

- `addWord`: `O(L)` time.
- Search with no wildcard: `O(L)` time.
- Search with wildcards: may explore many branches. With `D` dots and up to 26 children per dot, a useful worst-case description is `O(26^D * L)`.
- Space for stored words: `O(T)`, where `T` is the total number of inserted characters.
- Recursive call stack: up to `O(L)` during a search.

The actual search is usually smaller because the Trie contains only paths for saved words.

## Common Mistakes

- Treating `.` as a literal dictionary key.
- Returning `False` when the first wildcard branch fails instead of trying all children.
- Returning `True` when the pattern ends without checking `is_word`.
- Forgetting `index + 1`, which causes recursion never to progress.
- Using slicing such as `word[1:]` on every recursive call; an index avoids repeatedly creating new strings.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| What if `*` means zero or more characters? | At `*`, either advance the pattern without moving in the Trie, or move to a child without advancing the pattern. Memoize `(node, pattern_index)` states to avoid repeating work. |
| How would you delete a word? | Traverse to the word, clear its end marker, and prune childless nodes that no other word needs. This takes `O(L)`. |
| How would you return every matching word? | Carry the built prefix during DFS, collect instead of returning after the first match, and include the output size in the complexity. |
| Can wildcard search avoid repeated recursive work? | Memoize each `(node, index)` result. It helps when richer wildcard rules reach the same state more than once, although one `.` can still branch widely. |
| Can you write the search without recursion? | Use a stack of `(node, index)` pairs. Push one next state for a letter or one state per child for a dot. |

## How to Explain It in an Interview

> I will store words in a normal Trie. Exact letters follow one child. A dot can match any child, so search becomes DFS from that position. The base case checks both that the pattern is consumed and that the current node marks a complete word. Exact search is linear, while wildcard search can branch exponentially in the number of dots.

## Practice Checks

After adding `a`, `at`, and `and`, determine these results:

```text
search(".")    -> True
search("a.")   -> True
search("a..")  -> True
search("..")   -> True
search("....") -> False
```
