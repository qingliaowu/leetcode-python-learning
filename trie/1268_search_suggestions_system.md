# 1268. Search Suggestions System

[LeetCode problem](https://leetcode.com/problems/search-suggestions-system/) | [Python solution](./1268_search_suggestions_system.py)

## What the Question Asks

Given product names and a search word, return suggestions after each typed character. Each result contains at most three products that:

1. start with the characters typed so far, and
2. come first in lexicographical (dictionary-like) order.

For `searchWord = "mouse"`, the prefixes are `"m"`, `"mo"`, `"mou"`, `"mous"`, and `"mouse"`. The answer therefore contains five lists.

## Python Used Here

### Sorting a list

```python
products.sort()
```

`sort()` changes the original list and returns `None`. After sorting, products that come first lexicographically are inserted into the Trie first.

### A list containing lists

```python
answer = []
answer.append(node.suggestions)
```

The final answer is a list in which each item is another list of strings. The type hint `List[List[str]]` describes this shape.

### Checking list length

```python
if len(node.suggestions) < 3:
    node.suggestions.append(product)
```

`len(...)` returns the number of items. `append(...)` adds one item to the end of a list.

## Main Idea

Each Trie node represents one prefix. Add a `suggestions` list to every node:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
```

Sort all products first. As each product passes through a node, save it only if that node has fewer than three suggestions.

Why does this give the correct top three? Products are inserted in sorted order. Therefore, the first three products reaching a prefix node are exactly the first three lexicographical matches. Later products cannot be better, so they do not need to be stored there.

This is an example of precomputation: do more work while building the Trie so each later query is simple.

## Step-by-Step Approach

### Build the Trie

1. Sort `products`.
2. Create an empty root.
3. Insert each product one character at a time.
4. At every visited character node, save the product if fewer than three suggestions are present.

Suggestions are added after moving to the child because that child represents the prefix including the current character.

### Read the search word

1. Start at the root.
2. Follow each typed character.
3. If the path exists, append that node's saved suggestions.
4. If the path is missing, append an empty list.
5. Keep appending empty lists for all later characters because a longer prefix cannot recover from an already missing shorter prefix.

The code represents a permanently missing path with `node = None`.

## Dry Run

Products after sorting:

```text
mobile, moneypot, monitor, mouse, mousepad
```

What gets stored:

| Prefix node | First three products that pass through it |
| --- | --- |
| `m` | `mobile`, `moneypot`, `monitor` |
| `mo` | `mobile`, `moneypot`, `monitor` |
| `mou` | `mouse`, `mousepad` |
| `mous` | `mouse`, `mousepad` |
| `mouse` | `mouse`, `mousepad` |

Reading `"mouse"` simply visits these nodes and returns their saved lists.

If the next typed character were `"z"`, the `mousez` path would be missing. That result and every longer result would be `[]`.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let:

- `N` be the number of products,
- `T` be the total number of characters across all products,
- `M` be the length of `searchWord`.

Then:

- Sorting: commonly written as `O(N log N)` comparisons.
- Building the Trie: `O(T)` time.
- Searching: `O(M)` time because suggestions are already stored.
- Space: `O(T)` Trie nodes. Each node saves at most three product references, so this is still `O(T)`.

String comparisons during sorting can inspect multiple characters, but `O(N log N)` is the usual interview-level statement unless the interviewer requests a tighter analysis.

## Common Mistakes

- Forgetting to sort before keeping the first three products.
- Saving suggestions only at the final product node instead of every prefix node.
- Saving every matching product at every node, which uses unnecessary memory.
- Stopping the answer when a prefix is missing; the result still needs one list per typed character.
- Re-sorting every node's suggestions during the search.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| What if products can be added or removed often? | Update every node on that product's path. Each node may need an ordered set or a larger candidate collection so its top three can be repaired after deletion. |
| What if suggestions are ranked by popularity? | Store each product's score and cache the three highest-ranked products at every prefix node. A score change must update all nodes on that product's path. |
| What if the interviewer asks for the top `K` suggestions? | Keep up to `K` suggestions per node. Queries remain fast, but cached memory grows from three references per node to as many as `K`. |
| Can you avoid caching suggestions in every node? | Walk to the prefix node, then perform lexicographic DFS until three words are found. This saves cached lists but makes each query do more traversal work. |
| How would you support one typing mistake? | Combine Trie traversal with edit-distance state, or use dynamic programming while exploring branches. First clarify whether insertion, deletion, replacement, or all three edits are allowed. |

## How to Explain It in an Interview

> I will sort the products first and build a Trie. Every Trie node represents a prefix and stores at most the first three products that pass through it. Since insertion happens in sorted order, those are already the correct three suggestions. Querying then follows the search word one character at a time and reads the cached list at each node.

## Practice Checks

Think through these cases:

- Fewer than three products match a prefix.
- No product matches the first character.
- One product is itself a prefix of another product.
- All products share a long prefix.

## Check Your Understanding

Try each question before opening its answer. Sort the products first, then write the prefix after every typed character.

### Question 1: Produce Suggestions by Hand

Products are `["bags", "baggage", "banner", "box"]` and the search word is `"bag"`. What suggestion list is returned after each typed character when at most three lexicographically smallest products are shown?

<details>
<summary>Show answer and explanation</summary>

**Answer:**

```text
"b"   -> ["baggage", "bags", "banner"]
"ba"  -> ["baggage", "bags", "banner"]
"bag" -> ["baggage", "bags"]
```

Sorted order is `"baggage"`, `"bags"`, `"banner"`, `"box"`. All four match `"b"`, but only the first three are kept. `"box"` stops matching at prefix `"ba"`. At prefix `"bag"`, `"banner"` also stops matching.

Because products enter the Trie in sorted order, the first three saved at a node are already that prefix's correct suggestions.

**Complexity:** With cached node suggestions, querying a search word of length `M` takes `O(M)` after preprocessing.

**Edge case:** Once a prefix has no Trie path, that prefix and every longer prefix produce an empty list.

</details>

### Question 2: A Simple Sorted-Scan Version

Write a beginner-friendly version that returns at most `limit` suggestions per prefix by scanning sorted products instead of building a Trie.

<details>
<summary>Show answer and detailed solution</summary>

```python
def suggested_products_simple(
    products: list[str], search_word: str, limit: int = 3
) -> list[list[str]]:
    ordered_products = sorted(products)
    answer = []
    prefix = ""

    for character in search_word:
        prefix += character
        matches = []

        for product in ordered_products:
            if product.startswith(prefix):
                matches.append(product)
                if len(matches) == limit:
                    break

        answer.append(matches)

    return answer
```

Sorting once guarantees that the first matching products are lexicographically smallest. For each typed prefix, the function scans until it collects enough matches or reaches the end. This version is easy to verify but repeats work across prefixes.

**Complexity:** Sorting costs `O(N log N)` comparisons. The repeated scan can inspect all `N` products for each of `M` prefixes, with prefix comparisons adding character work. The sorted copy uses `O(N)` references, and the suggestion lists use output-sized space.

**Test:** The input from Question 1 produces the three listed suggestion lists; a search word starting with `"z"` produces empty lists.

</details>
