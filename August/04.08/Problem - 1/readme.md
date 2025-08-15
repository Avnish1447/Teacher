Ah, a classic from the university dorms. Let's find George and Alex a place to stay.

### Clarify the Goal

The task is simple. We're given the number of rooms in a dormitory, `n`. For each room, we know its total capacity (`q`) and how many people are already living there (`p`). We need to count how many of these rooms have enough space for two more people, George and Alex.

So, for every room, we just need to check if there are at least two empty spots.

-----

### The Analogy First: The Double-Decker Bus 🚌

Imagine you are a tour guide trying to find a bus for two friends, George and Alex, who want to travel together. You have a list of all the buses for the tour.

For each bus, you ask the driver two things: "What's your total capacity?" and "How many people are on board right now?"

Your process is simple:

1.  Go to the first bus. The driver says, "Capacity 10, currently 8 people." You calculate the empty spots: `10 - 8 = 2`. Perfect\! That's enough for both friends. You increment your count of available buses to 1.
2.  Go to the second bus. "Capacity 20, currently 19 people." Empty spots: `20 - 19 = 1`. Not enough room for two. You move on.
3.  Go to the third bus. "Capacity 15, currently 10 people." Empty spots: `15 - 10 = 5`. Plenty of room\! You increment your count to 2.

You repeat this for every bus. The final count is your answer.

-----

### The Optimal Approach (The "Aha\!" Moment)

The "Double-Decker Bus" analogy is the direct and optimal solution. The "Aha\!" moment is simply realizing the problem is a direct translation of a real-world question into a simple mathematical check.

The condition "has free place for both George and Alex" means:
`Number of free places >= 2`

And the number of free places is simply `capacity (q) - people already there (p)`.

So, for each room, the condition we check is: `q - p >= 2`.

Let's trace the second example: `n=3`, with rooms `(p=1, q=10)`, `(p=0, q=10)`, and `(p=10, q=10)`.

1.  **Initialize count:** `available_rooms = 0`.
2.  **Room 1:** `10 - 1 = 9`. Is `9 >= 2`? Yes. `available_rooms` is now 1.
3.  **Room 2:** `10 - 0 = 10`. Is `10 >= 2`? Yes. `available_rooms` is now 2.
4.  **Room 3:** `10 - 10 = 0`. Is `0 >= 2`? No.

The final count is **2**.

-----

### Code Implementation

The code for this is very straightforward: a simple loop with a single `if` condition.

```python
def solve():
    """
    Solves the "George and Accommodation" problem.
    """
    # Read the total number of rooms.
    n = int(input())
    
    # This will be our counter for suitable rooms.
    available_rooms_count = 0
    
    # Loop 'n' times to check each room.
    for _ in range(n):
        # Read the current occupancy (p) and capacity (q) for the room.
        p, q = map(int, input().split())
        
        # This is our check from the analogy: are there at least 2 empty spots?
        if q - p >= 2:
            available_rooms_count += 1
            
    # Print the final count.
    print(available_rooms_count)

solve()
```

-----

### Complexity Analysis

  * **Time Complexity:** $O(N)$
    We have to check each of the `N` rooms exactly once. The work is directly proportional to the number of rooms.
  * **Space Complexity:** $O(1)$
    We only need one variable to keep our count (`available_rooms_count`). We process each room's information one by one without storing the whole list, so the memory usage is constant.

-----

### Final Check

This problem is a simple exercise in reading the problem statement carefully and translating it into a basic condition inside a loop. Does this straightforward approach make sense?