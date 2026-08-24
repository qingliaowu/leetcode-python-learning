"""Lesson 5: fast lookup with dictionaries and sets."""

# A dictionary maps keys to values.
scores = {"Ada": 10, "Grace": 8}
assert scores["Ada"] == 10

scores["Linus"] = 9
scores["Ada"] = 11
assert scores["Ada"] == 11

# get returns a default instead of failing when a key is missing.
assert scores.get("Missing", 0) == 0
assert "Grace" in scores

counts = {}
for letter in "apple":
    counts[letter] = counts.get(letter, 0) + 1

assert counts == {"a": 1, "p": 2, "l": 1, "e": 1}

# A set stores unique values.
unique_numbers = {1, 2, 2, 3}
assert unique_numbers == {1, 2, 3}

unique_numbers.add(4)
assert 4 in unique_numbers

empty_set = set()
assert len(empty_set) == 0

print("Lesson 5 checks passed.")
