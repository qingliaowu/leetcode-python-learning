# LeetCode Python Learning

A practical Python learning repository for solving LeetCode problems, reviewing data structures and algorithms, and building consistent problem-solving habits. Explanations are written for beginners and returning Python learners, so important syntax is reviewed instead of assumed.

## Goal

This repository is intended to become a personal LeetCode study guide focused on clear Python solutions. Each solution should explain the approach, analyze complexity, and keep code easy to read.

## Start Here: Python 3 Basics

New to Python or returning after a long break? Begin with [Python 3 Basics for Complete Beginners](./python_basics/). The eleven short lessons start with `print` and variables, then build gently toward collections, loops, functions, classes, recursion, LeetCode's `Solution` format, and an easy introduction to time and space complexity.

Every lesson includes:

- plain-language explanations,
- runnable examples,
- expected results,
- a small prediction exercise,
- common beginner mistakes,
- links to the next interview material.

## Interview Preparation

Start with the [Interview Problem-Solving Playbook](./INTERVIEW_PLAYBOOK.md). It explains what to do from the moment a problem is presented: clarify the requirements, show a brute-force baseline, recognize the pattern, state an invariant, code, test, and analyze complexity.

Practice rule: explain your assumptions, complexity, edge cases, and code testing aloud. Correct code matters, but the interviewer also needs to hear why the approach is correct and how you verified it.

Run every included example with one command:

```bash
python3 verify_solutions.py
```

The repository uses only the Python standard library.

## Suggested Structure

As problems are added, organize them by topic or difficulty:

```text
.
├── arrays_strings/
├── heaps/
├── intervals_search/
├── prefix_recursion/
├── python_basics/
├── trie/
├── linked_lists/
├── trees_graphs/
├── dynamic_programming/
├── INTERVIEW_PLAYBOOK.md
├── verify_solutions.py
└── README.md
```

Each problem folder or file can include:

- Problem title and LeetCode link
- Python solution
- Explanation of the approach
- Time and space complexity
- Notes about edge cases

## Learning Workflow

1. Read the problem carefully and identify the input, output, and constraints.
2. Write down a brute-force idea first.
3. Improve the approach using the right data structure or algorithm.
4. Implement the solution in Python.
5. Test with sample cases and edge cases.
6. Record the final complexity and any lessons learned.

## Python Solution Template

```python
class Solution:
    def solve(self, *args):
        # Implement the solution here.
        pass
```

## Topics To Cover

- Arrays and strings
- Hash maps and sets
- Two pointers and sliding window
- Stack and queue
- Linked lists
- Trees and graphs
- Binary search
- Trie
- Backtracking
- Dynamic programming
- Greedy algorithms

## Interview Practice Sets

### Trie

Start here if you are learning prefix trees for Python interviews:

| Priority | LeetCode | Title | Focus |
| --- | ---: | --- | --- |
| 5/5 | 208 | Implement Trie | Core trie operations |
| 5/5 | 1268 | Search Suggestions System | Prefix search with top 3 results |
| 4/5 | 211 | Design Add and Search Words | Trie with wildcard DFS |
| 3/5 | 648 | Replace Words | Shortest prefix lookup |
| 3/5 | 677 | Map Sum Pairs | Trie with stored prefix totals |

The [Trie learning guide](./trie/) starts with a Python refresher, then provides a full lesson and an executable Python solution for every problem.

### Core Interview Roadmap

| Priority | Topics | Questions | Guide |
| --- | --- | --- | --- |
| High | Arrays, strings, hash maps, sliding window | Two Sum; Group Anagrams; Longest Substring Without Repeating Characters | [Start](./arrays_strings/) |
| High | Trees and graphs | Number of Islands; Course Schedule; Clone Graph | [Start](./trees_graphs/) |
| High | Intervals, sorting, binary search | Merge Intervals; Meeting Rooms II; Search in Rotated Sorted Array | [Start](./intervals_search/) |
| High | Dynamic programming | Coin Change; House Robber; Longest Increasing Subsequence | [Start](./dynamic_programming/) |
| Medium | Heaps and top-k | Kth Largest Element; Top K Frequent Elements; Merge K Sorted Lists | [Start](./heaps/) |
| Medium | Prefix sums and recursion | Subarray Sum Equals K; Word Search | [Start](./prefix_recursion/) |

## Progress

Use this section to track solved problems as the repository grows.

| Topic | Solved | Notes |
| --- | ---: | --- |
| Python 3 basics | 11 lessons | Beginner course complete |
| Arrays, strings, and hash maps | 3 | Core interview set added |
| Trie | 5 | Interview practice set added |
| Trees and graphs | 3 | Core interview set added |
| Intervals, sorting, and binary search | 3 | Core interview set added |
| Heaps and top-k | 3 | Core interview set added |
| Prefix sums and recursion | 2 | Core interview set added |
| Dynamic programming | 3 | Core interview set added |

## Contributing

When adding a new solution, prefer readable Python code, descriptive filenames, and a short explanation of the reasoning behind the solution.
