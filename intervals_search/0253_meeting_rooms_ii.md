# 253. Meeting Rooms II

[LeetCode problem](https://leetcode.com/problems/meeting-rooms-ii/) | [Python solution](./0253_meeting_rooms_ii.py)

## What the Question Asks

Given meeting `[start, end]` intervals, return the minimum number of rooms needed so every meeting can happen. A room can be reused when its meeting ends at or before the next one starts.

The answer is the maximum number of overlapping meetings.

## Python Used Here

Python's `heapq` module treats a list as a min-heap:

```python
import heapq

end_times = []
heapq.heappush(end_times, 30)
heapq.heappush(end_times, 10)

end_times[0]                 # 10, the smallest end time
heapq.heappop(end_times)     # removes and returns 10
```

`if end_times` checks whether the list is non-empty before reading `end_times[0]`.

## Main Idea

Process meetings by start time. The heap stores one end time for each room that has been allocated. Its smallest value is the room that becomes available first.

For each meeting:

- If the earliest end is `<= start`, reuse that room by removing its old end.
- Push the current end time for the room now holding this meeting.
- If no room is available, nothing is popped, so pushing allocates one more room.

The heap size never decreases in this implementation; it represents the number of rooms allocated at the busiest point.

## Step-by-Step Approach

1. Sort meetings by start.
2. Create an empty min-heap of room end times.
3. For each meeting, check the smallest end time.
4. Pop one end if that room is available.
5. Push the new meeting's end.
6. Return the heap size.

Only one available room needs to be popped because one new meeting only needs one room.

## Dry Run

For `[[0, 30], [5, 10], [15, 20]]`:

| Meeting | Earliest room end | Action | Heap after push |
| --- | ---: | --- | --- |
| `[0,30]` | none | New room | `[30]` |
| `[5,10]` | 30 | New room | `[10,30]` |
| `[15,20]` | 10 | Reuse earliest room | `[20,30]` |

Two rooms were allocated, so the answer is `2`.

For `[1,5]` followed by `[5,8]`, end `5 <= start 5`, so one room is enough.

## Complexity

New to Big-O? Read [Time and Space Complexity for Beginners](../python_basics/11_time_and_space_complexity.md).

- Sorting: `O(N log N)`.
- Each heap push or pop: `O(log N)`.
- Total time: `O(N log N)`.
- Space: `O(N)` in the worst case when all meetings overlap.

## Common Mistakes

- Comparing with the most recently added end instead of the earliest end.
- Treating meetings that touch at an endpoint as overlapping.
- Returning the number of meetings instead of allocated rooms.
- Forgetting to sort by start time.
- Popping every available room even though only one room is needed now.

## Interview Explanation

> I process meetings in start-time order and keep allocated room end times in a min-heap. The smallest end tells me whether any room can be reused. If it can, I replace that end with the current meeting's end; otherwise I add another room. The final heap size is the minimum room count.
