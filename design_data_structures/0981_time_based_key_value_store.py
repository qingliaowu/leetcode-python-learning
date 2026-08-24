"""
LeetCode 981: Time Based Key-Value Store

Store values by key and timestamp, then find the newest value at or before a
requested timestamp.

Beginner lesson:
See 0981_time_based_key_value_store.md for the data layout, binary search,
dry run, complexity, edge cases, and interview explanation.

Complexity:
- set: O(1) average because timestamps arrive in increasing order
- get: O(log M), where M is the number of values stored for that key
- space: O(S), where S is the total number of set operations
"""


class TimeMap:
    def __init__(self):
        # key -> list of (timestamp, value) tuples in timestamp order
        self.history = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Store value for key at timestamp."""
        if key not in self.history:
            self.history[key] = []

        self.history[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """Return the newest value whose timestamp is at most timestamp."""
        entries = self.history.get(key, [])
        left = 0
        right = len(entries) - 1
        answer = ""

        while left <= right:
            middle = (left + right) // 2
            saved_time, saved_value = entries[middle]

            if saved_time <= timestamp:
                # This value works. Search right for a newer valid value.
                answer = saved_value
                left = middle + 1
            else:
                # This entry is too new, so discard it and everything right.
                right = middle - 1

        return answer


if __name__ == "__main__":
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)

    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"

    time_map.set("foo", "bar2", 4)

    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"
    assert time_map.get("foo", 0) == ""
    assert time_map.get("missing", 100) == ""
