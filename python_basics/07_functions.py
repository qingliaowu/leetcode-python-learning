"""Lesson 7: put reusable work inside functions."""


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def is_even(number: int) -> bool:
    """Return whether number has no remainder after division by 2."""
    return number % 2 == 0


def greet(name: str = "friend") -> str:
    """Return a greeting; use friend when no name is supplied."""
    return f"Hello, {name}!"


def find_first_even(numbers):
    """Return the first even number, or None when no even value exists."""
    for number in numbers:
        if is_even(number):
            return number
    return None


assert add(2, 3) == 5
assert is_even(6) is True
assert is_even(7) is False
assert greet("Ada") == "Hello, Ada!"
assert greet() == "Hello, friend!"
assert find_first_even([1, 3, 4, 6]) == 4
assert find_first_even([1, 3]) is None

print("Lesson 7 checks passed.")
