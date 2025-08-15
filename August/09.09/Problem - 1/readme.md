Of course. This problem is a nice exercise in thinking about movement on a circular path.

-----

### Clarify the Goal

The task is to calculate the total time Xenia spends completing a series of tasks. She starts at house \#1 on a circular road with `n` houses. The road is one-way (clockwise). We are given `m` tasks in a specific order, where each task `a_i` is at a certain house. Moving from one house to the next takes one unit of time.

The key challenge is calculating the travel time between tasks on a one-way, circular road.

-----

### The Analogy First: The Clock Hand ⏰

Imagine the `n` houses are numbers on a big clock face, from 1 to `n`. Xenia's position is a single clock hand that can only move **clockwise**. She is given a sequence of numbers (tasks) that the clock hand must point to, in order. We need to find the total time it takes.

Let's say the clock has 10 hours (so `n=10`) and Xenia is at 7 o'clock.

  * **Case 1 (Simple Forward Move):** If her next task is at 9 o'clock, she simply moves forward. The time taken is `9 - 7 = 2` units.
  * **Case 2 (Wrapping Around):** If her next task is at 2 o'clock, she can't go backward. She must sweep all the way past 8, 9, and 10, wrap around past 1, and finally arrive at 2. The time taken is `(10 - 7)` to get to the "end," plus `2` to get from the "start" to her destination. Total time: `3 + 2 = 5` units.

Our problem is just to add up the time for each step in her journey.

-----

### The Optimal Approach (The "Aha\!" Moment)

The "Clock Hand" analogy is the optimal way to solve this. The "Aha\!" is simply breaking down the time calculation for each step into the two cases we identified:

1.  If `destination >= current_location`, the time is `destination - current_location`.
2.  If `destination < current_location`, we have to wrap around. The time is `(n - current_location) + destination`.

Let's trace the first example: `n=4`, tasks `[3, 2, 3]`.

  * Initialize `total_time = 0`.
  * Start at `current_pos = 1`.

<!-- end list -->

1.  **Task 1: Go to house 3.**

      * `destination (3) >= current_pos (1)`. This is Case 1.
      * Time for this step = `3 - 1 = 2`.
      * `total_time` is now `0 + 2 = 2`.
      * Update `current_pos` to `3`.

2.  **Task 2: Go to house 2.**

      * `destination (2) < current_pos (3)`. This is Case 2 (wrap around).
      * Time for this step = `(n - current_pos) + destination` = `(4 - 3) + 2 = 3`.
      * `total_time` is now `2 + 3 = 5`.
      * Update `current_pos` to `2`.

3.  **Task 3: Go to house 3.**

      * `destination (3) >= current_pos (2)`. This is Case 1.
      * Time for this step = `3 - 2 = 1`.
      * `total_time` is now `5 + 1 = 6`.
      * Update `current_pos` to `3`.

All tasks are complete. The final answer is **6**.

-----

### Code Implementation

The logic translates into a simple loop that keeps a running total.

```python
def solve():
    """
    Solves the "Xenia and Ringroad" problem from Codeforces.
    """
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))

    # Xenia starts at house 1.
    current_pos = 1
    total_time = 0

    # Process each task in the given order.
    for destination in tasks:
        # Case 1: Simple forward move.
        if destination >= current_pos:
            total_time += destination - current_pos
        # Case 2: Wrap around the ringroad.
        else:
            time_to_end = n - current_pos
            time_from_start = destination
            total_time += time_to_end + time_from_start
        
        # Update Xenia's location for the next task.
        current_pos = destination

    print(total_time)

solve()
```

-----

### Complexity Analysis

  * **Time Complexity:** $O(M)$
    We simply loop through the `M` tasks once, performing a constant number of calculations for each. The runtime is directly proportional to the number of tasks.

  * **Space Complexity:** $O(M)$
    We need to store the list of `M` tasks from the input.

-----

### Final Check

This problem is about carefully calculating cumulative sums while being mindful of the "wrap-around" logic on a circular path. Does the "Clock Hand" analogy make the two cases for calculating travel time clear?