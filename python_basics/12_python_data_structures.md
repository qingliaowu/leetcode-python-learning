# Lesson 12: Python Data Structures Made Simple

[Run this lesson](./12_python_data_structures.py) | [Course home](./README.md) | [Python cheat sheet](../PYTHON_CHEAT_SHEET.md) | [Progress tracker](../PROGRESS_TRACKER.md)

## Goal

Learn how Python stores groups of values and how to choose the right structure
without guessing. By the end, you should be able to explain lists, tuples,
dictionaries, sets, stacks, queues, heaps, counters, and graph adjacency lists
in plain language.

Lessons 4 and 5 teach the syntax of Python's main built-in collections. This
lesson connects them, adds interview structures, and explains the tradeoffs.

## Read This in Three Easy Passes

1. **Fast pass:** Read the one-minute map and the choice table.
2. **Learning pass:** Read one structure at a time and run its code.
3. **Interview pass:** Study operation costs, common mistakes, and knowledge checks.

Do not memorize every method. Remember what job each structure makes easy.

## What Is a Data Structure?

A value stores one piece of data:

```python
score = 95
name = "Maya"
```

A data structure organizes several values so the program can perform certain
jobs efficiently:

```python
scores = [95, 82, 91]              # ordered values
score_by_name = {"Maya": 95}      # name -> score
students_present = {"Maya", "Li"} # unique values
```

There is no best structure for every problem. A list makes position easy. A
dictionary makes key lookup easy. A set makes membership easy. Choosing a data
structure means choosing which operations should be simple and fast.

## One-Minute Choice Map

| You Need To... | Start With | Mental Picture |
| --- | --- | --- |
| Keep values in order and use positions | `list` | A numbered row |
| Store a small fixed record | `tuple` | A sealed row |
| Connect a key to a value | `dict` | Labeled drawers |
| Keep unique values or test membership | `set` | A guest list |
| Remove the newest item first | `list` as a stack | A stack of trays |
| Remove the oldest item first | `deque` as a queue | A waiting line |
| Repeatedly remove the smallest priority | `heapq` | A priority desk |
| Count repeated values | `Counter` | A tally sheet |
| Group values under keys | `defaultdict(list)` | Labeled folders |
| Store relationships between nodes | adjacency-list `dict` | A contact map |

### The Fast Decision Tree

```text
Do I map one key to one value?
    yes -> dictionary
    no
     |
Do I mainly ask "have I seen this value?"
    yes -> set
    no
     |
Must I repeatedly remove by arrival order?
    newest first -> stack
    oldest first -> queue
    smallest priority first -> heap
    no
     |
Do I need an immutable fixed record?
    yes -> tuple
    no -> list
```

This is a starting point. A real solution can combine several structures.

## 1. List: Ordered and Changeable

A Python list stores values in order. Each value has a numeric index.

```python
colors = ["red", "green", "blue"]

first = colors[0]       # "red"
colors[1] = "yellow"   # change one value
colors.append("purple")
last = colors.pop()     # removes "purple"
```

Choose a list when you need:

- position or index,
- order,
- duplicates,
- iteration from left to right,
- adding and removing at the end.

### A List Is a Dynamic Array

Python's list is not a linked list. It behaves like a resizable array of object
references. This explains its important costs:

- Reading `items[index]` is `O(1)`.
- Appending at the end is `O(1)` on average.
- Removing from the end is `O(1)`.
- Inserting or removing at the front is `O(N)` because later items shift.
- Searching `value in items` is `O(N)` because Python may scan every value.

Use a list for a stack. Do not use `pop(0)` repeatedly for a large queue.

## 2. Tuple: Ordered and Fixed

A tuple also stores ordered values, but the tuple cannot be changed after creation.

```python
point = (4, 7)
x = point[0]
y = point[1]
```

This fails:

```python
point[0] = 9  # TypeError: tuples do not support item assignment
```

Choose a tuple when:

- the values form one small fixed record,
- changing the record would be a mistake,
- the record should be a dictionary key or set item,
- you want to return several values from a function.

```python
distance_by_point = {(4, 7): 11}
```

A tuple is hashable only when every value inside it is hashable. `(4, 7)` can be
a dictionary key. `([4], 7)` cannot because it contains a mutable list.

## 3. Dictionary: Key to Value

A dictionary connects each unique key to a value.

```python
age_by_name = {
    "Maya": 28,
    "Li": 31,
}

age_by_name["Maya"]          # read
age_by_name["Noah"] = 26     # add
age_by_name["Li"] = 32       # update
```

Choose a dictionary when the question sounds like:

- "Find the value for this key."
- "Remember where I saw this value."
- "Count each value."
- "Group items by a property."
- "Connect each graph node to its neighbors."

### Safe Lookup

Square brackets require the key to exist:

```python
age_by_name["Unknown"]  # KeyError
```

`get` can provide a default:

```python
age = age_by_name.get("Unknown", 0)
```

Dictionary key lookup, insertion, and deletion are `O(1)` on average. A
dictionary uses extra memory to make those lookups fast.

## 4. Set: Unique Values and Fast Membership

A set stores each distinct value once.

```python
visited = {2, 5, 8}

5 in visited      # True
visited.add(13)
visited.discard(2)
```

Choose a set when you need:

- fast "have I seen this?" checks,
- duplicate removal,
- unique values,
- union, intersection, or difference.

```python
first_group = {"Maya", "Li"}
second_group = {"Li", "Noah"}

everyone = first_group | second_group       # union
both = first_group & second_group           # intersection
only_first = first_group - second_group     # difference
```

Set membership, insertion, and deletion are `O(1)` on average. Sets do not
support position indexing, and their order should not be used as sorted output.

### Empty Set Syntax

```python
empty_dictionary = {}
empty_set = set()
```

`{}` creates a dictionary, not a set.

## 5. Stack: Newest Item Leaves First

A stack follows last in, first out, often shortened to LIFO.

Use a normal list:

```python
stack = []
stack.append("first")
stack.append("second")

newest = stack.pop()  # "second"
```

Think of browser back history, nested brackets, undo operations, or DFS.

| Stack Action | Python | Typical Time |
| --- | --- | --- |
| Push | `stack.append(value)` | `O(1)` average |
| Read top | `stack[-1]` | `O(1)` |
| Pop | `stack.pop()` | `O(1)` |
| Check empty | `not stack` | `O(1)` |

Only call `pop()` after checking that the stack is not empty when empty input is
possible.

## 6. Queue: Oldest Item Leaves First

A queue follows first in, first out, often shortened to FIFO.

Use `deque` from Python's `collections` module:

```python
from collections import deque

queue = deque()
queue.append("first")
queue.append("second")

oldest = queue.popleft()  # "first"
```

Queues are common in breadth-first search, job processing, and level-order tree
traversal.

| Queue Action | Python | Typical Time |
| --- | --- | --- |
| Add right | `queue.append(value)` | `O(1)` |
| Remove left | `queue.popleft()` | `O(1)` |
| Read oldest | `queue[0]` | `O(1)` |
| Check empty | `not queue` | `O(1)` |

Why not a list?

```python
items.pop(0)
```

Removing index 0 shifts the remaining list items and costs `O(N)`. A deque is
designed for fast work at both ends.

## 7. Heap: Repeatedly Get the Smallest Priority

Python's `heapq` module treats a list as a min-heap.

```python
import heapq

priorities = []
heapq.heappush(priorities, 5)
heapq.heappush(priorities, 2)
heapq.heappush(priorities, 8)

smallest = heapq.heappop(priorities)  # 2
```

A heap guarantees that index 0 is the smallest item. It does not keep the whole
list visibly sorted.

Choose a heap when you repeatedly need:

- the next smallest priority,
- the next earliest event,
- the largest or smallest K values,
- the next item among several sorted sources.

| Heap Action | Python | Typical Time |
| --- | --- | --- |
| Build from N values | `heapq.heapify(items)` | `O(N)` |
| Read smallest | `items[0]` | `O(1)` |
| Add | `heapq.heappush(items, value)` | `O(log N)` |
| Remove smallest | `heapq.heappop(items)` | `O(log N)` |

For LeetCode on Python 3.10, a common max-heap technique stores negative numbers:

```python
max_heap = []
heapq.heappush(max_heap, -10)
largest = -heapq.heappop(max_heap)
```

Use this only when the values are numeric. For records, use a priority tuple such
as `(priority, sequence_number, value)` and explain what each field means.

## 8. Counter: A Dictionary Made for Counting

`Counter` is a dictionary subclass from `collections`.

```python
from collections import Counter

counts = Counter(["red", "blue", "red"])

counts["red"]      # 2
counts["missing"]  # 0
```

It is useful for frequencies, anagrams, voting, and top-k frequency problems.

The beginner version with a normal dictionary is still important:

```python
counts = {}

for color in colors:
    counts[color] = counts.get(color, 0) + 1
```

Understand that pattern even when `Counter` makes the final code shorter.

## 9. defaultdict: Create a Default Value Automatically

`defaultdict` creates a missing value by calling the function supplied at creation.

```python
from collections import defaultdict

words_by_length = defaultdict(list)

for word in ["cat", "tree", "sun"]:
    words_by_length[len(word)].append(word)
```

The first time key `3` appears, `defaultdict(list)` creates an empty list, then
the code appends to it.

Use it for grouping or building adjacency lists. Be careful: reading a missing
key can create that key. Use a normal dictionary with `get` when that side effect
would be confusing.

## 10. Linked Lists and Trees: Nodes Connected by References

Some structures are built from class objects rather than one built-in collection.

### Linked-List Node

```python
class ListNode:
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node
```

Each node stores a value and a reference to the next node.

```text
[value: 4] -> [value: 9] -> None
```

### Binary-Tree Node

```python
class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

Each node stores a value and up to two child references.

```text
        8
       / \
      3   10
```

The object is the node. Variables such as `current`, `left`, and `right` hold
references to objects. Reassigning a reference is how linked-list and tree
algorithms change connections.

Return to [Classes and Objects](./08_classes_and_objects.md) when `self`,
constructors, or node references feel unclear.

## 11. Graph: Store Each Node's Neighbors

An adjacency list is the most common interview graph representation:

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": [],
}
```

Read it aloud:

```text
A has edges to B and C.
B has an edge to D.
C has an edge to D.
D has no outgoing edge.
```

The dictionary finds a node's neighbor list. The list stores its neighbors.
A BFS usually adds a queue and a visited set:

```python
from collections import deque

queue = deque(["A"])
visited = {"A"}
```

This shows why interview solutions often combine structures. The graph,
visited state, and work order have different jobs.

## 12. Nested Structures: Read From the Outside In

Interview data structures often contain other structures:

```python
groups: dict[str, list[str]] = {
    "short": ["cat", "sun"],
    "long": ["elephant"],
}
```

Read the type hint from the outside:

```text
dictionary
    keys are strings
    values are lists of strings
```

More examples:

| Type Hint | Plain English |
| --- | --- |
| `list[int]` | A list of integers |
| `set[str]` | A set of strings |
| `dict[str, int]` | String key to integer value |
| `list[tuple[int, int]]` | A list of integer pairs |
| `dict[int, list[int]]` | Integer node to list of neighboring nodes |
| `deque[TreeNode]` | A queue of tree-node references |

Type hints explain intended contents. Python usually does not enforce them while
the program runs.

## 13. Mutable Values, Aliases, and Copies

Lists, dictionaries, sets, and most class objects are mutable. They can change.
Strings, numbers, and tuples are immutable.

### Two Names Can Refer to One List

```python
original = [1, 2]
alias = original

alias.append(3)
print(original)  # [1, 2, 3]
```

No copy was made. `original` and `alias` point to the same list.

### Make a Shallow Copy

```python
original = [1, 2]
copied = original.copy()

copied.append(3)
print(original)  # [1, 2]
```

A shallow copy creates a new outer collection. Nested mutable objects can still
be shared:

```python
original = [[1], [2]]
copied = original.copy()
copied[0].append(9)

print(original)  # [[1, 9], [2]]
```

Use `copy.deepcopy` only when an independent recursive copy is truly required.
In interviews, state whether your algorithm mutates the input.

## 14. Hashable Keys in Dictionaries and Sets

Dictionary keys and set items must be hashable. A beginner-friendly rule is:

```text
stable immutable values usually work
mutable containers usually do not
```

| Value | Can Be a Dictionary Key? | Reason |
| --- | :---: | --- |
| `7` | Yes | Integer is immutable |
| `"cat"` | Yes | String is immutable |
| `(2, 5)` | Yes | Tuple contents are hashable |
| `[2, 5]` | No | List can change |
| `{2, 5}` | No | Set can change |
| `frozenset({2, 5})` | Yes | Frozen set cannot change |

This is why grid coordinates are often stored as tuples:

```python
visited = {(row, column)}
```

## 15. Common Combinations in Interviews

| Problem Need | Structures | Why They Work Together |
| --- | --- | --- |
| Two Sum | list + dictionary | Scan ordered input; remember value to index |
| Longest unique substring | string + dictionary or set | Window has order; map/set tracks membership |
| Valid parentheses | string + stack | Close the most recently opened bracket first |
| Number of Islands | grid + stack/queue or recursion | Store cells; control traversal work |
| Graph BFS | adjacency list + queue + set | Store edges, FIFO work, and visited nodes |
| Top K Frequent | Counter + heap | Count first; keep best priorities |
| Merge K Lists | node references + heap | Keep the smallest current node from each list |
| LRU Cache | dictionary + doubly linked list | Fast key lookup and fast order updates |
| Trie | dictionary inside each node | Map each next character to a child node |

Before coding, assign one job to each structure. If two structures appear to do
the same job, check whether one is unnecessary.

## 16. Operation Costs You Should Know

Let `N` be the number of stored items.

| Structure and Operation | Typical Time | Easy Reason |
| --- | --- | --- |
| List read by index | `O(1)` | Go directly to one position |
| List append | `O(1)` average | Add at the end |
| List pop from end | `O(1)` | Remove at the end |
| List insert/pop at front | `O(N)` | Remaining items shift |
| List membership | `O(N)` | May inspect every item |
| Tuple read by index | `O(1)` | Go directly to one position |
| Dictionary get/set/delete | `O(1)` average | Hash finds a key's location |
| Set membership/add/remove | `O(1)` average | Hash finds a value's location |
| Deque append/popleft | `O(1)` | Structure is designed for both ends |
| Heap read smallest | `O(1)` | Smallest value stays at index 0 |
| Heap push/pop | `O(log N)` | Repair one path through heap levels |
| Sort N items | `O(N log N)` | General comparison sorting cost |

Dictionary and set costs are average-case interview assumptions, not a promise
that every possible operation always takes exactly the same time.

### Space Complexity

If a structure stores up to `N` new items, it usually needs `O(N)` extra space.

Examples:

- A `seen` set containing every input value uses `O(N)` extra space.
- A frequency dictionary with up to `U` unique values uses `O(U)` extra space.
- A heap deliberately limited to K items uses `O(K)` extra space.
- An adjacency list uses `O(V + E)` space for V nodes and E edges.
- A queue in BFS can hold up to the traversal's widest frontier.

Read [Time and Space Complexity](./11_time_and_space_complexity.md) whenever the
letters or growth rules feel unfamiliar.

## 17. How to Choose Aloud in an Interview

Use this sentence pattern:

```text
I need to __________.
A __________ makes that operation __________.
It stores __________, so the extra space is __________.
```

Example:

```text
I need to know whether I have already visited a node.
A set makes membership O(1) on average.
It may store every node, so the extra space is O(V).
```

Another example:

```text
I need to process nodes in the order I discover them.
A deque gives FIFO removal from the left in O(1) time.
It may hold one graph frontier, so I will include the queue in space analysis.
```

The explanation matters more than naming a structure quickly.

## 18. Common Beginner Mistakes

- Using `list.pop(0)` for a large queue instead of `deque.popleft()`.
- Expecting a set to preserve sorted order or support indexes.
- Using a mutable list as a dictionary key.
- Forgetting that `alias = original` does not copy a list.
- Calling `stack.pop()` or `queue.popleft()` without handling empty input.
- Assuming a heap list is fully sorted.
- Forgetting that Python's heap is a min-heap for the supported Python version.
- Using `defaultdict` without noticing that a missing read can create a key.
- Choosing a dictionary when only unique membership is needed.
- Choosing a list for membership checks inside a large loop when a set fits.
- Ignoring the memory used by maps, sets, queues, heaps, or node references.
- Memorizing a data structure without stating the job it performs.

## Fast Knowledge Checks

Answer in one sentence before opening each explanation.

### Check 1: Ordered Scores With Duplicates

You must preserve score order, allow duplicate scores, and read by numeric index.
Which structure fits first?

<details>
<summary>Show answer and easy explanation</summary>

Use a **list**. Lists preserve order, allow duplicates, and support `scores[index]`
in `O(1)` time. A set would remove duplicates and has no numeric indexing.

</details>

### Check 2: Have I Seen This ID?

You repeatedly ask whether an ID has appeared before, but you do not need a value
connected to the ID. Which structure fits?

<details>
<summary>Show answer and easy explanation</summary>

Use a **set**. It stores unique IDs and gives average `O(1)` membership checks.
A dictionary could work, but its value field has no job here.

</details>

### Check 3: Employee ID to Name

You need to find an employee name from an employee ID. Which structure fits?

<details>
<summary>Show answer and easy explanation</summary>

Use a **dictionary** from ID to name. The ID is the key, the name is the value,
and lookup is `O(1)` on average.

</details>

### Check 4: Undo the Latest Action

An editor must undo the most recently recorded action first. Which structure and
operations fit?

<details>
<summary>Show answer and easy explanation</summary>

Use a **list as a stack**. Record with `append` and undo with `pop`. Both operate
at the end and take `O(1)` time on average.

</details>

### Check 5: Process the Oldest Job

Jobs must run in arrival order. Which structure fits?

<details>
<summary>Show answer and easy explanation</summary>

Use a **deque as a queue**. Add with `append` and remove the oldest job with
`popleft`. Both are `O(1)`.

</details>

### Check 6: Repeatedly Remove the Smallest Deadline

You repeatedly need the task with the smallest deadline. Which structure fits?

<details>
<summary>Show answer and easy explanation</summary>

Use a **min-heap**. The smallest item is at index 0, and each removal or insertion
takes `O(log N)`. Sorting after every new task would repeat unnecessary work.

</details>

### Check 7: Count Every Word

You need the frequency of every word. What are two suitable choices?

<details>
<summary>Show answer and easy explanation</summary>

Use a normal **dictionary** with `counts[word] = counts.get(word, 0) + 1`, or use
`Counter(words)`. `Counter` is convenient, but the dictionary pattern explains
what the counting operation does.

</details>

### Check 8: Why Did the Original List Change?

After `backup = values`, the code appends to `backup` and `values` also changes.
Why?

<details>
<summary>Show answer and easy explanation</summary>

Both variables refer to the same list. Assignment copied the reference, not the
collection. Use `backup = values.copy()` for a new outer list, and remember that
nested mutable objects are still shared by a shallow copy.

</details>

### Check 9: Coordinate as a Set Item

Should a grid coordinate be stored as `[row, column]` or `(row, column)` inside
a set?

<details>
<summary>Show answer and easy explanation</summary>

Use the tuple `(row, column)`. A tuple of integers is immutable and hashable. A
list can change, so Python does not allow it as a set item.

</details>

### Check 10: BFS Through a Graph

Which three structures commonly work together for graph BFS?

<details>
<summary>Show answer and easy explanation</summary>

Use an **adjacency-list dictionary** for neighbors, a **deque** for FIFO work,
and a **set** for visited nodes. Each structure has one clear job: relationships,
processing order, and duplicate prevention.

</details>

### Score Your Check

| Correct Without Notes | Next Step |
| ---: | --- |
| 9-10 | Explain the choice and complexity for three interview problems |
| 6-8 | Review the missed structure and rerun its code example |
| 0-5 | Repeat the one-minute choice map, then retry tomorrow |

## Runnable Practice

Open [the lesson file](./12_python_data_structures.py), predict every assertion,
then run:

```bash
python3 python_basics/12_python_data_structures.py
```

The file demonstrates:

- built-in list, tuple, dictionary, and set behavior,
- stack, queue, and heap removal order,
- `Counter` and `defaultdict`,
- graph BFS with an adjacency list, deque, and set,
- aliasing versus copying.

Change one value in each example and predict the new result before rerunning it.

### Complexity of the Runnable Functions

| Function | Time | Extra Space | Plain-English Reason |
| --- | --- | --- | --- |
| `first_repeated` | `O(N)` | `O(N)` | Scan once; the set may store every value |
| `group_by_length` | `O(N)` | `O(N)` | Visit every word; grouping stores every word reference |
| `k_largest` | `O(N log K)` | `O(K)` | Process N values with a heap that holds at most K |
| `breadth_first_order` | `O(V + E)` | `O(V)` | Visit each reachable node and edge; queue, set, and output store nodes |

The `k_largest` row assumes `1 <= K <= N`. Its final sort of K values costs
`O(K log K)` and does not exceed the stated bound. If `K > N`, use N in place of
K. Required returned output may be counted separately in some interviews, so say
what your space analysis includes.

### Assumptions and Edge Cases to Say Aloud

- `first_repeated` returns the first value whose second occurrence is encountered.
- An empty input or an input with no duplicate returns `None`.
- `group_by_length` preserves the input order within each group.
- `k_largest` returns an empty list when `K <= 0`; when `K` exceeds the number
  of values, it returns every value in descending order.
- Duplicate numbers are separate values in `k_largest`.
- `breadth_first_order` returns an empty list when the start node is absent.
- The graph example assumes every listed neighbor also has a dictionary entry.
- The examples copy data before heap mutation when the original order must survive.
- The examples do not require any external Python package.

Testing aloud means checking a normal case, empty case, duplicate case, missing
case, and boundary value when they apply. The runnable assertions include each
of those categories.

## Final Checklist

You are ready when you can:

- choose list, tuple, dictionary, or set from the required operation,
- explain LIFO, FIFO, and priority order,
- use `deque` for a queue and `heapq` for a min-heap,
- explain how `Counter` and `defaultdict` relate to dictionaries,
- read a nested type such as `dict[int, list[int]]`,
- explain aliases, shallow copies, mutable values, and hashable keys,
- name the typical cost of lookup, membership, append, queue removal, and heap work,
- assign one clear job to each structure in a combined solution.

Do not aim to remember every method. Aim to recognize the job, choose a structure,
and explain why its operations fit.

---

[Previous: Lesson 11, Time and Space Complexity](./11_time_and_space_complexity.md) | [Next: Algorithm Pattern Map](../ALGORITHM_PATTERN_MAP.md)
