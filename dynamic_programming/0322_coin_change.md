# 322. Coin Change

[LeetCode problem](https://leetcode.com/problems/coin-change/) | [Python solution](./0322_coin_change.py) | [DP guide](./README.md)

## What the Question Asks

You have unlimited coins of each listed value. Return the fewest coins needed to make the exact amount. Return `-1` when it is impossible.

```text
coins = [1, 2, 5], amount = 11
5 + 5 + 1 uses 3 coins
answer = 3
```

This asks for the minimum number of coins, not the number of different combinations.

## The DP State

Define one saved answer clearly:

```text
dp[x] = the minimum number of coins needed to make amount x
```

The final answer should be `dp[amount]`.

## Base Case

```python
dp[0] = 0
```

Making amount zero requires zero coins. This known answer lets larger amounts build from it.

## Transition

Suppose the last coin used is `coin`. Before adding it, the smaller amount was:

```text
current_amount - coin
```

If that smaller answer is known, using this coin creates:

```text
dp[current_amount - coin] + 1
```

Try every coin and keep the smallest result:

```python
dp[current_amount] = min(
    dp[current_amount],
    dp[current_amount - coin] + 1,
)
```

## Why Fill Amounts From Small to Large?

When calculating `dp[current_amount]`, every `current_amount - coin` is smaller. Filling amounts from `1` upward guarantees those smaller answers are already available.

## The Impossible Marker

At first, unknown amounts receive:

```python
impossible = amount + 1
dp = [impossible] * (amount + 1)
```

Why is `amount + 1` safe? If a solution exists and the smallest coin is at least `1`, no solution needs more than `amount` coins. Therefore, `amount + 1` is worse than every possible real answer.

If the final value is still this marker, return `-1`.

## Python Used Here

```python
[impossible] * (amount + 1)
```

This creates a list with one entry for every amount from `0` through `amount`.

```python
range(1, amount + 1)
```

`range` stops before its second value, so `amount + 1` makes the loop include `amount`.

## Dry Run

Use coins `[1, 3, 4]` and amount `6`:

| Amount `x` | Best construction | `dp[x]` |
| ---: | --- | ---: |
| 0 | Use no coins | 0 |
| 1 | `1` | 1 |
| 2 | `1 + 1` | 2 |
| 3 | `3` | 1 |
| 4 | `4` | 1 |
| 5 | `4 + 1` | 2 |
| 6 | `3 + 3` | 2 |

The greedy choice of taking `4` first would leave `2`, producing three coins: `4 + 1 + 1`. DP finds the better answer `3 + 3`.

## Why It Is Correct

Every solution for a positive amount has one final coin. The algorithm tries every possible final coin. For each one, it combines that coin with the already optimal answer for the remaining smaller amount. Taking the minimum covers every valid final choice.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

Let:

- `A` be the target amount,
- `C` be the number of coin values.

For every amount from `1` through `A`, the algorithm tries all `C` coins.

- Time: `O(A * C)`.
- Extra space: `O(A)` for the `dp` list.

This is pseudo-polynomial time because it depends on the numeric amount, not only the number of digits used to write that amount. In most interviews, clearly stating `O(amount * number_of_coins)` is sufficient.

## Edge Cases

- Amount `0`: return `0` without using a coin.
- No combination can make the amount: return `-1`.
- One coin equals the target: return `1`.
- Coin order should not affect the answer.
- A greedy largest-coin choice may be wrong, as `[1, 3, 4]`, amount `6` shows.

## Common Mistakes

- Using greedy choice without proving that the coin system supports it.
- Forgetting `dp[0] = 0`.
- Accessing `dp[current_amount - coin]` when the result is negative.
- Returning the impossible marker instead of `-1`.
- Counting combinations instead of minimizing coin count.
- Saying time is only `O(A)` while ignoring the inner coin loop.

## Possible Follow-up Questions

| Follow-up | Answer Direction |
| --- | --- |
| How would you return the coins used? | Save which final coin produced each best `dp` value, then follow those choices backward from `amount` to zero. |
| What if each coin has a limited supply? | The unlimited-use recurrence is no longer enough. Add remaining counts to the state or use a bounded-knapsack transition for each coin's allowed copies. |
| How would you count combinations instead of finding a minimum? | Let `dp[x]` be the number of ways to make `x`, start with `dp[0] = 1`, and loop over coins before amounts so different orders are not counted twice. |
| What if different coin orders count as different answers? | Loop over amounts before coins. Then every reachable previous amount can append each coin as a distinct final step. |
| What if `amount` is extremely large? | Point out that the DP is amount-dependent. Discuss whether BFS, number-theory properties of the coin system, or extra constraints can reduce the work. |

## Interview Explanation

> I define `dp[x]` as the minimum coins needed for amount `x`, with `dp[0] = 0`. For every amount, I try each coin as the final coin and use one plus the saved answer for the remaining amount. There are `A` amounts and `C` coin choices, so time is `O(A * C)` and space is `O(A)`.

## Test Aloud

For coins `[2]`, amount `3`, say:

```text
Amount 1 stays impossible. Amount 2 becomes one coin using dp[0]. Amount 3
cannot use a saved reachable remainder, so its marker never changes. The code
returns -1.
```

## Check Your Understanding

Try each question before opening its answer. Define `dp[x]` and its impossible marker before tracing the table.

### Question 1: Why Greedy Fails

For coins `[1, 3, 4]` and amount `6`, what is the minimum number of coins? What answer would repeatedly choosing the largest possible coin produce?

<details>
<summary>Show answer and explanation</summary>

**Answer:** The minimum is `2`, using `3 + 3`. Greedy choice produces `4 + 1 + 1`, which uses `3` coins.

Dynamic programming compares all possible final coins. For amount `6`, choosing final coin `3` uses `1 + dp[3] = 2`, while choosing final coin `4` uses `1 + dp[2] = 3`. Saving the best result for every smaller amount makes this comparison possible.

Greedy choice is correct only for coin systems with additional properties, so it cannot be assumed here.

**Complexity:** `O(A * C)` time and `O(A)` extra space for amount `A` and `C` coin types.

**Edge case:** Amount `0` needs zero coins, even when the coin list is empty.

</details>

### Question 2: Count Coin Combinations

Assume the coin values are positive and distinct. Return the number of combinations that make an amount. Different orders of the same coins count once. For coins `[1, 2, 5]` and amount `5`, return `4`.

<details>
<summary>Show answer and detailed solution</summary>

```python
def count_coin_combinations(coins: list[int], amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            dp[current_amount] += dp[current_amount - coin]

    return dp[amount]
```

Here `dp[x]` means the number of combinations that build amount `x` using the coin types processed so far. `dp[0] = 1` represents one way to make zero: choose nothing. Appending the current coin to every way of making `x - coin` creates ways to make `x`.

Coins are the outer loop, so each combination is introduced in one consistent coin-type order. Reversing the loops would count sequences such as `1 + 2` and `2 + 1` separately.

**Complexity:** `O(A * C)` time and `O(A)` extra space.

**Tests:** Coins `[1, 2, 5]`, amount `5`, return `4`; coins `[2]`, amount `3`, return `0`; amount `0` returns `1` empty combination.

</details>
