"""Lesson 3: create, inspect, slice, and combine strings."""

word = "python"

# Indexes start at 0. Negative indexes count from the end.
assert word[0] == "p"
assert word[1] == "y"
assert word[-1] == "n"

# A slice starts at the first index and stops before the second index.
assert word[0:3] == "pyt"
assert word[:2] == "py"
assert word[2:] == "thon"

assert len(word) == 6
assert word.upper() == "PYTHON"
assert "  hello  ".strip() == "hello"

sentence = "learn python today"
words = sentence.split()
assert words == ["learn", "python", "today"]
assert "-".join(words) == "learn-python-today"

name = "Ada"
score = 10
message = f"{name} scored {score}"
assert message == "Ada scored 10"

print(message)
print("Lesson 3 checks passed.")
