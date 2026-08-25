"""Lesson 12: choose and use common Python data structures."""

from collections import Counter, defaultdict, deque
import heapq


def first_repeated(values: list[int]) -> int | None:
    """Return the first value encountered twice, or None."""
    seen: set[int] = set()

    for value in values:
        if value in seen:
            return value
        seen.add(value)

    return None


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Group words under their lengths."""
    groups: defaultdict[int, list[str]] = defaultdict(list)

    for word in words:
        groups[len(word)].append(word)

    return dict(groups)


def k_largest(values: list[int], k: int) -> list[int]:
    """Return the k largest values in descending order."""
    if k <= 0:
        return []

    min_heap: list[int] = []

    for value in values:
        if len(min_heap) < k:
            heapq.heappush(min_heap, value)
        elif value > min_heap[0]:
            heapq.heapreplace(min_heap, value)

    return sorted(min_heap, reverse=True)


def breadth_first_order(
    graph: dict[str, list[str]], start: str
) -> list[str]:
    """Return nodes in breadth-first discovery order."""
    if start not in graph:
        return []

    queue = deque([start])
    visited = {start}
    order: list[str] = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    # List: ordered, mutable, and indexed.
    colors = ["red", "green", "blue"]
    colors[1] = "yellow"
    colors.append("purple")
    assert colors == ["red", "yellow", "blue", "purple"]
    assert colors.pop() == "purple"

    # Tuple: ordered and immutable.
    point = (4, 7)
    distance_by_point = {point: 11}
    assert point[0] == 4
    assert distance_by_point[(4, 7)] == 11

    # Dictionary: key to value.
    age_by_name = {"Maya": 28, "Li": 31}
    age_by_name["Li"] = 32
    assert age_by_name["Li"] == 32
    assert age_by_name.get("Unknown", 0) == 0

    # Set: unique values and fast membership.
    visited_numbers = {2, 5, 5, 8}
    assert visited_numbers == {2, 5, 8}
    assert 5 in visited_numbers
    assert first_repeated([4, 2, 7, 2, 4]) == 2
    assert first_repeated([1, 2, 3]) is None
    assert first_repeated([]) is None

    # Stack: newest item leaves first.
    stack: list[str] = []
    stack.append("first")
    stack.append("second")
    assert stack.pop() == "second"

    # Queue: oldest item leaves first.
    queue = deque(["first", "second"])
    queue.append("third")
    assert queue.popleft() == "first"
    assert list(queue) == ["second", "third"]

    # Min-heap: smallest priority leaves first.
    priorities = [5, 2, 8]
    heapq.heapify(priorities)
    assert heapq.heappop(priorities) == 2
    assert k_largest([7, 1, 9, 4, 8], 3) == [9, 8, 7]
    assert k_largest([7, 1], 0) == []
    assert k_largest([3, 3, 2], 5) == [3, 3, 2]
    assert k_largest([], 3) == []

    # Counter: frequency dictionary.
    counts = Counter(["red", "blue", "red"])
    assert counts["red"] == 2
    assert counts["missing"] == 0

    # defaultdict: create grouping lists when a key first appears.
    assert group_by_length(["cat", "tree", "sun"]) == {
        3: ["cat", "sun"],
        4: ["tree"],
    }
    assert group_by_length([]) == {}

    # Graph BFS: adjacency list + queue + visited set.
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }
    assert breadth_first_order(graph, "A") == ["A", "B", "C", "D"]
    assert breadth_first_order(graph, "missing") == []

    # Assignment creates an alias. copy() creates a new outer list.
    original = [1, 2]
    alias = original
    copied = original.copy()
    alias.append(3)
    copied.append(4)
    assert original == [1, 2, 3]
    assert copied == [1, 2, 4]

    print("Lesson 12 checks passed.")
