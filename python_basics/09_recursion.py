"""Lesson 9: solve a smaller version of a problem with recursion."""


def sum_to(number: int) -> int:
    """Return 1 + 2 + ... + number for a non-negative number."""
    # Base case: stop making recursive calls.
    if number == 0:
        return 0

    # Recursive case: solve a smaller version of the same problem.
    return number + sum_to(number - 1)


def factorial(number: int) -> int:
    """Return number multiplied by every positive integer below it."""
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def reverse_text(text: str) -> str:
    """Return text in reverse using a small recursion example."""
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]


assert sum_to(0) == 0
assert sum_to(4) == 10
assert factorial(1) == 1
assert factorial(5) == 120
assert reverse_text("cat") == "tac"

print("Lesson 9 checks passed.")
