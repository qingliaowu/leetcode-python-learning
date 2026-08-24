# Coding Interview Study Plans: 5, 10, 14, 30, or 60 Days

Choose the plan that matches the number of full study days before your interview. Each plan uses the same Python course, 26 problem lessons, self-check exercises, and [solve-aloud interview process](./INTERVIEW_PLAYBOOK.md).

No schedule can guarantee an offer. Interview results also depend on the questions, role, communication, and hiring process. These plans are designed to maximize readiness with the time available.

## Choose One Plan

| Time Available | Daily Study Time | Main Goal | Best Fit |
| --- | ---: | --- | --- |
| [5 days](#5-day-emergency-plan) | 4-6 hours | Emergency coverage of the 15 core problems | Interview is this week |
| [10 days](#10-day-core-plan) | 3-4 hours | Learn the core set and complete three transfer problems | You know basic Python but need pattern practice |
| [14 days](#14-day-intensive-plan) | 3-4 hours | Give all 26 problems one serious pass | You can study intensely for two weeks |
| [30 days](#30-day-balanced-plan) | 90-150 minutes | Learn all patterns with review days and four mocks | Recommended balanced plan |
| [60 days](#60-day-beginner-to-interview-plan) | 60-120 minutes | Relearn Python, complete all problems, repeat them, and run regular mocks | Best plan for a rusty Python beginner |

Do not choose a longer plan and try to compress it. Use the plan matching the actual days available.

## What Counts as Learning a Problem?

Reading a solution is not completion. A problem counts as learned only when you can do all of these:

1. Restate the input, output, and assumptions.
2. Give a small example before coding.
3. Describe a direct approach and its bottleneck.
4. Name the optimized pattern and its invariant or DP state.
5. Write the solution without copying.
6. Test a normal case and at least two edge cases aloud.
7. Explain time and space complexity in complete sentences.
8. Answer both **Check Your Understanding** questions at the end of the lesson.
9. Explain how you would handle one follow-up requirement.

If you cannot do steps 5-7, mark the problem for review. Do not pretend that recognizing the code means you can reproduce it under interview pressure.

## Score Every Problem

Use this score after each attempt:

| Score | Meaning | Next Action |
| ---: | --- | --- |
| 0 | I could not identify a useful pattern. | Read the lesson slowly, trace the example, and retry tomorrow. |
| 1 | I understood only after seeing most of the solution. | Re-code immediately, then retry without notes tomorrow. |
| 2 | I had the right idea but needed syntax or implementation help. | Review the missing Python and retry in 2 days. |
| 3 | I solved it independently in 35 minutes and explained complexity. | Review in 3-7 days. |
| 4 | I solved it cleanly, tested it, and handled a follow-up. | Keep it in weekly mixed review. |

The goal is not to give every problem a `4`. Before interviewing, aim for at least `3` on most of the 15 core problems and at least `7/10` on recent mocks.

## The 15-Problem Core

The short plans prioritize these problems because they cover the repository's requested interview set.

| Pattern | Core Problems |
| --- | --- |
| Hash maps and sliding window | [1 Two Sum](./arrays_strings/0001_two_sum.md), [49 Group Anagrams](./arrays_strings/0049_group_anagrams.md), [3 Longest Substring](./arrays_strings/0003_longest_substring_without_repeating_characters.md) |
| Sorting and binary search | [56 Merge Intervals](./intervals_search/0056_merge_intervals.md), [704 Binary Search](./intervals_search/0704_binary_search.md) |
| Stack | [394 Decode String](./stacks_queues/0394_decode_string.md) |
| Graphs | [200 Number of Islands](./trees_graphs/0200_number_of_islands.md), [133 Clone Graph](./trees_graphs/0133_clone_graph.md), [207 Course Schedule](./trees_graphs/0207_course_schedule.md) |
| Heaps and top-k | [215 Kth Largest](./heaps/0215_kth_largest_element.md), [347 Top K Frequent](./heaps/0347_top_k_frequent_elements.md) |
| Trie | [208 Implement Trie](./trie/0208_implement_trie.md), [1268 Search Suggestions](./trie/1268_search_suggestions_system.md) |
| Stateful design | [981 Time Based Key-Value Store](./design_data_structures/0981_time_based_key_value_store.md), [146 LRU Cache](./design_data_structures/0146_lru_cache.md) |

## The 11 Expansion Problems

Longer plans add these problems to broaden pattern coverage.

| Pattern | Expansion Problems |
| --- | --- |
| Intervals and search | [33 Search Rotated Array](./intervals_search/0033_search_in_rotated_sorted_array.md), [253 Meeting Rooms II](./intervals_search/0253_meeting_rooms_ii.md) |
| Heap merging | [23 Merge K Sorted Lists](./heaps/0023_merge_k_sorted_lists.md) |
| Prefix sum and backtracking | [560 Subarray Sum Equals K](./prefix_recursion/0560_subarray_sum_equals_k.md), [79 Word Search](./prefix_recursion/0079_word_search.md) |
| Trie variations | [211 Add and Search Words](./trie/0211_design_add_and_search_words.md), [648 Replace Words](./trie/0648_replace_words.md), [677 Map Sum Pairs](./trie/0677_map_sum_pairs.md) |
| Dynamic programming | [198 House Robber](./dynamic_programming/0198_house_robber.md), [322 Coin Change](./dynamic_programming/0322_coin_change.md), [300 Longest Increasing Subsequence](./dynamic_programming/0300_longest_increasing_subsequence.md) |

## Daily Study Method

Use this sequence for every new problem:

| Step | Work | Typical Time |
| ---: | --- | ---: |
| 1 | Recall yesterday's pattern without notes | 10 minutes |
| 2 | Attempt the new problem from its summary only | 25-35 minutes |
| 3 | Read the lesson and find the first place your reasoning differed | 15-25 minutes |
| 4 | Close the lesson and code again from a blank file or editor tab | 20-30 minutes |
| 5 | Run the supplied Python file and test extra edge cases aloud | 10 minutes |
| 6 | Complete both self-check questions before revealing their answers | 15-25 minutes |
| 7 | Record the score, mistake, complexity, and next review day | 5 minutes |

Short tracks complete two or three of these blocks per day. Longer tracks usually complete one block and use the remaining time for review.

## If You Miss a Day

1. Do not double the next day's new problems.
2. Move unfinished new work to the next review day.
3. Keep the scheduled mock; it reveals which missed material actually matters.
4. In the 5- or 10-day plan, drop expansion problems before dropping core problems.
5. In the 30- or 60-day plan, use a recovery day or replace one repeated problem.
6. Protect normal sleep, especially during the final two nights.

Missing one day is recoverable. Turning the next day into an exhausted eight-hour catch-up session usually creates more mistakes than it repairs.

## Python Rescue Rule

If syntax prevents you from expressing the algorithm, stop for at most 20 minutes and read the matching beginner lesson:

| Missing Skill | Lesson |
| --- | --- |
| Strings and slicing | [03 Strings](./python_basics/03_strings.md) |
| Lists and tuples | [04 Lists and Tuples](./python_basics/04_lists_and_tuples.md) |
| Dictionaries and sets | [05 Dictionaries and Sets](./python_basics/05_dictionaries_and_sets.md) |
| Loops and conditions | [06 Conditions and Loops](./python_basics/06_conditions_and_loops.md) |
| Functions | [07 Functions](./python_basics/07_functions.md) |
| Classes and objects | [08 Classes and Objects](./python_basics/08_classes_and_objects.md) |
| Recursion | [09 Recursion](./python_basics/09_recursion.md) |
| Interview syntax | [10 Python for LeetCode](./python_basics/10_python_for_leetcode.md) |
| Big-O | [11 Time and Space Complexity](./python_basics/11_time_and_space_complexity.md) |

Return to the problem immediately after the refresher. Avoid turning a short syntax repair into an entire day of passive reading unless you are following the 60-day plan.

## 5-Day Emergency Plan

**Time:** 4-6 focused hours per day.

**Target:** See all 15 core problems, become independent on the highest-yield patterns, and complete one realistic mock. This plan deliberately skips the 11 expansion problems.

| Day | New Work | Required Review and Checkpoint |
| ---: | --- | --- |
| 1 | Read [Python for LeetCode](./python_basics/10_python_for_leetcode.md) and the [Big-O lesson](./python_basics/11_time_and_space_complexity.md). Solve Two Sum, Group Anagrams, and Longest Substring. | Re-code Two Sum and Longest Substring from memory. Say why each is `O(N)` or not. |
| 2 | Solve Binary Search, Merge Intervals, and Decode String. | Spend 20 minutes redoing the weakest Day 1 problem. Trace boundary changes and stack state aloud. |
| 3 | Solve Number of Islands, Clone Graph, and Course Schedule. | Draw the graph state for each: visited cells, clone map, or in-degree list. Re-code one traversal without notes. |
| 4 | Solve Kth Largest, Top K Frequent, Implement Trie, and Search Suggestions. | Compare what each heap or Trie node stores. Complete every self-check before reading its answer. |
| 5 | Solve Time Based Key-Value Store and LRU Cache. Run one 45-minute mock and repair the three weakest core problems. | Finish with the readiness gate below. Do not add a new topic at night. |

### 5-Day Priorities

1. Prefer a correct, clearly explained solution over a memorized clever one.
2. If one problem consumes more than 50 minutes, read its lesson, re-code once, and move on.
3. Do not spend emergency-plan time on all Trie or DP variations.
4. Sleep normally before the interview; an exhausted extra study block has low value.

**Exit target:** Score at least `3` on 8 of the 15 core problems, explain all core patterns at a high level, and score at least `6/10` on the final mock.

## 10-Day Core Plan

**Time:** 3-4 focused hours per day.

**Target:** Learn the full core, add three transfer patterns, review each major topic at least once, and run two mocks.

| Day | New Work | Review |
| ---: | --- | --- |
| 1 | Python syntax diagnostic, Interview Playbook, Two Sum, Binary Search | Re-code both with no notes. |
| 2 | Group Anagrams, Longest Substring | Retry Two Sum; compare dictionary roles across all three array problems. |
| 3 | Merge Intervals, Decode String | Retry Binary Search and explain every boundary or stack invariant. |
| 4 | Number of Islands, Clone Graph | Redo the Day 2 self-check coding questions. |
| 5 | Course Schedule, Kth Largest | Run a 30-minute checkpoint on one random problem from Days 1-4. |
| 6 | Top K Frequent, Implement Trie | Retry one graph problem and explain `O(V + E)`. |
| 7 | Search Suggestions, Time Based Key-Value Store | Re-code Implement Trie before opening notes. |
| 8 | LRU Cache, House Robber | Trace stateful operations and DP take-or-skip state on paper. |
| 9 | Coin Change, Word Search | Retry the weakest three problems and complete their follow-ups aloud. |
| 10 | Two 45-minute mocks separated by a full review break | Repair only mistakes found by the mocks. End with the readiness gate. |

**Exit target:** Score at least `3` on 10 core problems, score at least `2` on the remaining core problems, and earn `7/10` on one of the two final mocks.

## 14-Day Intensive Plan

**Time:** 3-4 focused hours per day.

**Target:** Complete all 26 problems once, revisit weak patterns, and run a final mock day.

| Day | Problems and Focus | Required Recall |
| ---: | --- | --- |
| 1 | Python diagnostic, Interview Playbook, Two Sum | Re-code Two Sum and explain complement lookup. |
| 2 | Group Anagrams, Longest Substring | Recall Day 1 before starting; finish both self-checks. |
| 3 | Binary Search, Search in Rotated Sorted Array | State the search invariant before every boundary update. |
| 4 | Merge Intervals, Meeting Rooms II | Compare sorting plus merging with sorting plus a heap. |
| 5 | Decode String, Time Based Key-Value Store | Trace stack state and rightmost-valid binary search. |
| 6 | LRU Cache, Subarray Sum Equals K | Explain every piece of persistent or prefix state. |
| 7 | Word Search, House Robber | Run a 30-minute mixed checkpoint after the new work. |
| 8 | Number of Islands, Clone Graph | Compare grid visited marking with an original-to-clone map. |
| 9 | Course Schedule, Kth Largest | Recall one Day 6 problem without notes. |
| 10 | Top K Frequent, Merge K Sorted Lists | Explain why each heap contains at most `K` candidates. |
| 11 | Implement Trie, Search Suggestions | Draw stored node state and query paths. |
| 12 | Add and Search Words, Replace Words, Map Sum Pairs | Treat these as changes to the core Trie state, not three unrelated algorithms. |
| 13 | Coin Change, Longest Increasing Subsequence | Compare both DP state sentences with House Robber. Review all scores. |
| 14 | Two timed mocks, weak-area repair, and final readiness check | No new problems. Stop after a concise pattern review. |

**Exit target:** Attempt all 26 problems, score at least `3` on 11 of the core 15, and earn `7/10` on one final mock.

## 30-Day Balanced Plan

**Time:** 90-150 focused minutes per day.

**Target:** Learn all 26 problems with spaced review, complete four mock sessions, and avoid last-week cramming.

| Day | Main Work | Review Target |
| ---: | --- | --- |
| 1 | Python lessons 1-5 diagnostic and exercises | Record every syntax gap. |
| 2 | Python lessons 6-11, Interview Playbook, Two Sum | Re-code Two Sum once. |
| 3 | Group Anagrams | Review Two Sum. |
| 4 | Longest Substring | Review Group Anagrams. |
| 5 | Binary Search | Retry Two Sum without notes. |
| 6 | Search in Rotated Sorted Array | Review Longest Substring. |
| 7 | Mixed review and one 35-minute mini-mock | Repair the first weekly error log. |
| 8 | Merge Intervals | Review Binary Search. |
| 9 | Meeting Rooms II | Review Merge Intervals. |
| 10 | Decode String | Retry Rotated Search. |
| 11 | Time Based Key-Value Store | Review Decode String. |
| 12 | LRU Cache | Compare the two stateful designs. |
| 13 | No new problem: re-code the weakest three | Complete their self-checks again. |
| 14 | Full 45-minute mock | Score it and repair one root cause. |
| 15 | Number of Islands | Review one interval problem. |
| 16 | Clone Graph | Review Number of Islands. |
| 17 | Course Schedule | Compare all three graph states. |
| 18 | Kth Largest | Retry Clone Graph. |
| 19 | Top K Frequent | Review Kth Largest. |
| 20 | Merge K Sorted Lists | Compare all three heap invariants. |
| 21 | Full 45-minute mock plus graph/heap review | Update scores and next review dates. |
| 22 | Subarray Sum Equals K | Review Course Schedule. |
| 23 | Word Search | Review prefix-sum reasoning. |
| 24 | Implement Trie | Retry Word Search's backtracking. |
| 25 | Search Suggestions | Re-code Implement Trie. |
| 26 | Add and Search Words | Review Trie exact search versus branching search. |
| 27 | Replace Words and Map Sum Pairs | Compare end markers with cached prefix totals. |
| 28 | House Robber and Coin Change | Write both DP state and transition sentences first. |
| 29 | Longest Increasing Subsequence and complete DP review | Re-code the weakest DP problem. |
| 30 | Two final mocks with a break, then light review only | Apply the readiness gate and prepare interview logistics. |

### 30-Day Spaced Review

Review a new problem on this rhythm:

```text
first retry:   next day
second retry:  3 days later
third retry:   7 days later
final retry:   14 days later
```

A retry means solving from the problem summary, not rereading the finished solution. If time is limited, write the invariant, core loop, complexity, and tests instead of typing every class definition.

**Exit target:** Score at least `3` on 12 core problems, score at least `2` on every major pattern, and earn `7/10` on two of the final three mocks.

## 60-Day Beginner-to-Interview Plan

**Time:** 60-120 focused minutes on weekdays and up to 150 minutes on mock days.

**Target:** Rebuild Python fluency, learn every pattern slowly, revisit all core problems, complete at least eight timed sessions, and arrive rested.

### Days 1-7: Python and Solve-Aloud Foundations

| Day | Work |
| ---: | --- |
| 1 | Complete Python lessons 1-2 and run every example. |
| 2 | Complete lessons 3-4; practice string, list, tuple, and index operations. |
| 3 | Complete lesson 5; write small dictionary and set examples without copying. |
| 4 | Complete lessons 6-7; practice loops and functions. |
| 5 | Complete lessons 8-9; trace an object and one recursive call stack. |
| 6 | Complete lesson 10 and write the common LeetCode syntax from memory. |
| 7 | Complete lesson 11 and the Interview Playbook; run a 25-minute verbal practice with Two Sum. |

### Days 8-14: Arrays, Strings, and Basic Search

| Day | Work |
| ---: | --- |
| 8 | Two Sum |
| 9 | Group Anagrams plus Two Sum retry |
| 10 | Longest Substring |
| 11 | Binary Search |
| 12 | Search in Rotated Sorted Array plus Longest Substring retry |
| 13 | Complete all five lessons' self-checks without revealing answers first. |
| 14 | Run one 45-minute mock, score it, and repair one repeated mistake. |

### Days 15-21: Intervals, Stack, and Stateful Design

| Day | Work |
| ---: | --- |
| 15 | Merge Intervals |
| 16 | Meeting Rooms II |
| 17 | Decode String |
| 18 | Time Based Key-Value Store |
| 19 | LRU Cache |
| 20 | Re-code Merge Intervals and one stateful design without notes. |
| 21 | Run one 45-minute mock and complete one follow-up from each topic. |

### Days 22-28: Graphs

| Day | Work |
| ---: | --- |
| 22 | Number of Islands |
| 23 | Clone Graph |
| 24 | Course Schedule |
| 25 | Re-code Number of Islands with a separate visited set. |
| 26 | Complete all graph self-checks and compare DFS with BFS. |
| 27 | Run a graph-focused 45-minute mock. |
| 28 | Recovery day: review the error log for 30 minutes and stop. |

### Days 29-35: Heaps, Prefix Sums, and Backtracking

| Day | Work |
| ---: | --- |
| 29 | Kth Largest |
| 30 | Top K Frequent |
| 31 | Merge K Sorted Lists |
| 32 | Subarray Sum Equals K |
| 33 | Word Search |
| 34 | Re-code one heap and complete both transfer exercises for the weakest topic. |
| 35 | Run one 45-minute mixed mock. |

### Days 36-42: Trie

| Day | Work |
| ---: | --- |
| 36 | Implement Trie |
| 37 | Search Suggestions |
| 38 | Add and Search Words |
| 39 | Replace Words |
| 40 | Map Sum Pairs |
| 41 | Implement the basic Trie from a blank editor and compare all five node states. |
| 42 | Run one Trie or data-design mock and practice two follow-ups aloud. |

### Days 43-49: Dynamic Programming

| Day | Work |
| ---: | --- |
| 43 | House Robber |
| 44 | Coin Change |
| 45 | Longest Increasing Subsequence |
| 46 | Write all three state, base-case, and transition sentences without code. |
| 47 | Complete all DP self-checks and re-code House Robber. |
| 48 | Retry the weakest DP problem under a 35-minute limit. |
| 49 | Run one 45-minute mixed mock. |

### Days 50-56: Second Pass and Follow-ups

| Day | Work |
| ---: | --- |
| 50 | Re-solve Two Sum, Longest Substring, and Binary Search from summaries only. |
| 51 | Re-solve Merge Intervals and Decode String; explain one variation of each. |
| 52 | Re-solve Number of Islands and Course Schedule. |
| 53 | Re-solve Kth Largest and Top K Frequent. |
| 54 | Re-solve Time Based Key-Value Store and Implement Trie. |
| 55 | Re-solve Subarray Sum and House Robber; review the weakest expansion problem. |
| 56 | Run two 45-minute mocks with a substantial break between them. |

### Days 57-60: Final Interview Rehearsal

| Day | Work |
| ---: | --- |
| 57 | Run one unseen self-check as a mock, then practice explaining three core problems without code. |
| 58 | Repair only the top two remaining weaknesses. Prepare three concise examples of collaboration, debugging, and learning from feedback. |
| 59 | Run the final mock in the same environment and time limit as the interview. Review the error, not the entire curriculum. |
| 60 | Light pattern recall, environment check, food, hydration, and normal sleep. No difficult new problem. |

**Exit target:** Score at least `3` on 12 or more core problems, solve one transfer exercise from every major pattern, and earn `7/10` on at least two of the final three mocks.

## How to Run a 45-Minute Mock

Use a problem you have not attempted recently or use a lesson's Question 2 without opening its answer.

| Time | Candidate Behavior |
| --- | --- |
| 0-5 minutes | Restate the problem, inputs, outputs, assumptions, and examples. |
| 5-10 minutes | Explain a direct approach, bottleneck, optimized pattern, and invariant. |
| 10-30 minutes | Code while naming important state changes. |
| 30-38 minutes | Dry-run a normal case and test edge cases. |
| 38-42 minutes | Explain time and space complexity. |
| 42-45 minutes | Handle one follow-up and summarize tradeoffs. |

Do not pause the timer to read a lesson. After time ends, use a different color or a separate note to record what you fixed with help.

## Mock Scorecard

Score every mock out of 10:

| Skill | Points | Full Credit Means |
| --- | ---: | --- |
| Clarification | 1 | Inputs, output, assumptions, and constraints were stated. |
| Examples and baseline | 1 | A useful example and direct approach were explained. |
| Pattern and invariant | 2 | The optimized idea and stored state were precise. |
| Implementation | 2 | Code was complete and mostly correct within time. |
| Testing | 2 | Normal, boundary, empty/small, and tricky cases were considered. |
| Complexity | 1 | Time and extra space were correct and justified. |
| Follow-up communication | 1 | The changed assumption and algorithm change were clear. |

Interpret the score consistently:

| Score | Meaning |
| ---: | --- |
| 0-4 | The pattern or Python foundation needs repair. |
| 5-6 | The approach is promising, but interview execution is unreliable. |
| 7-8 | Ready for many normal interview questions; continue mixed mocks. |
| 9-10 | Strong performance; maintain it without overstudying. |

## Error Log Template

Keep one short row after each problem or mock:

| Date | Problem | Score | First Mistake | Correct Rule | Next Review |
| --- | --- | ---: | --- | --- | --- |
| Example | Binary Search | 2 | Used `right = middle` in an inclusive range | Exclude a checked non-answer with `middle - 1` | Tomorrow |

Write the **first** mistake, not every symptom that followed it. Fixing the earliest wrong assumption or state update usually prevents several later errors.

## Final Readiness Gate

You are reasonably prepared to interview when most of these statements are true:

- I can write loops, functions, dictionaries, sets, classes, queues, stacks, and `heapq` operations without repeatedly searching for syntax.
- I can recognize hash map, sliding window, binary search, interval, DFS/BFS, heap, Trie, backtracking, prefix-sum, and basic DP patterns.
- I can solve at least 10-12 core problems independently in 35 minutes.
- I state an invariant or DP state before coding.
- I test empty or smallest input, normal input, duplicates, missing answers, and relevant boundary behavior.
- I justify both time and extra space instead of naming Big-O without explanation.
- I can adapt at least one known solution when an assumption changes.
- At least two of my last three mock scores are `7/10` or higher.
- I can recover calmly after a hint or mistake.

If the gate is not met, do not restart the entire repository. Use the score table and error log to repair the two weakest patterns, then run another mock.

## Interview-Day Strategy

1. Confirm the editor, language version, meeting link, and time zone early.
2. Keep water and a blank page for examples and state diagrams.
3. Clarify before coding; silence does not demonstrate reasoning.
4. Prefer a correct baseline plus a clear optimization over rushing into unexplained code.
5. Test before claiming completion.
6. When stuck, return to a tiny example and state what repeated work or missing information blocks the current approach.
7. After the interview, record what happened, then stop studying for the day.
