# Dynamic Programming for Beginners

[Repository home](../README.md) | [Study plans](../INTERVIEW_STUDY_PLANS.md) | [Interview playbook](../INTERVIEW_PLAYBOOK.md) | [Pattern map](../ALGORITHM_PATTERN_MAP.md) | [Progress tracker](../PROGRESS_TRACKER.md) | [System design](../system_design/README.md) | [FDE track](../fde_interview/README.md) | [AI engineering](../ai_engineering/README.md)

Dynamic programming sounds advanced, but its central idea is simple:

> Solve a smaller problem once, save its answer, and reuse that answer.

Use the [Python 3 Basics course](../python_basics/) if syntax feels unfamiliar. Read [Time and Space Complexity](../python_basics/11_time_and_space_complexity.md) for plain-English Big-O help, and use the [Interview Playbook](../INTERVIEW_PLAYBOOK.md) to practice explaining solutions aloud.

## Recommended Order

| Priority | LeetCode | Lesson | Python Solution | Main Pattern |
| --- | ---: | --- | --- | --- |
| High | 198 | [House Robber](./0198_house_robber.md) | [Code](./0198_house_robber.py) | Choose the better of take or skip |
| High | 322 | [Coin Change](./0322_coin_change.md) | [Code](./0322_coin_change.py) | Minimum answer for every amount |
| High | 300 | [Longest Increasing Subsequence](./0300_longest_increasing_subsequence.md) | [Code](./0300_longest_increasing_subsequence.py) | Best sequence ending at each index |

House Robber comes first because its recurrence has only two choices. Coin Change adds an inner loop over choices. Longest Increasing Subsequence asks each position to look at every earlier position.

## Why Save Answers?

Suppose a recursive solution needs the answer for the same smaller input many times. Recalculating it wastes work. Dynamic programming stores that answer in a list or dictionary.

```text
Without saving: solve the same smaller question again and again.
With DP:       solve it once, then look up the saved answer.
```

## The Five DP Questions

Before coding, answer these in order.

### 1. What does one state mean?

Write one exact sentence:

```text
dp[x] is the minimum number of coins needed to make amount x.
```

If this sentence is unclear, the code will probably be unclear too.

### 2. What is the smallest known answer?

This is the base case:

```text
Making amount 0 needs 0 coins.
With no houses considered, the maximum money is 0.
One value by itself forms an increasing subsequence of length 1.
```

### 3. How does a larger answer use smaller answers?

This is the transition or recurrence:

```text
current answer = best result among valid previous states
```

### 4. In what order should states be calculated?

Every smaller state must be ready before it is used. Bottom-up solutions usually fill a list from left to right.

### 5. Where is the final answer?

It may be:

- the final state,
- the maximum of all states,
- or a small group of final variables.

Do not assume it is always `dp[-1]`.

## Two Ways to Write DP

### Top-down: recursion plus memoization

Start with the full question, recursively ask smaller questions, and cache their answers.

### Bottom-up: tabulation

Start with base cases and fill a table toward the full answer.

The solutions in this folder use bottom-up tabulation because the state order is visible and easy to trace during an interview.

## How to Recognize a DP Problem

Dynamic programming is worth considering when:

- the question asks for a minimum, maximum, number of ways, or possibility,
- one decision leaves a smaller version of the same problem,
- different decision paths reach the same smaller state,
- a brute-force recursive solution repeats work.

Not every minimum or maximum problem needs DP. First identify repeated smaller states and a recurrence.

## Interview Checklist

Say these points before writing code:

1. "My state means..."
2. "The base case is..."
3. "For each state, I choose between..."
4. "I fill states in this order because..."
5. "The answer is stored at..."
6. "Time is... because..."
7. "Space is... because..."

Then dry-run a tiny input and show each state changing.

## Ready for Mixed Practice

You are ready when you can state the DP state, base case, transition, fill order, final-answer location, and complexity before coding. Return to the [study plan](../INTERVIEW_STUDY_PLANS.md) for spaced review and mock interviews, and record results in the [progress tracker](../PROGRESS_TRACKER.md).
