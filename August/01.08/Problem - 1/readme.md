Of course. This is a classic introductory problem from Codeforces. Let's break it down.

### Clarify the Goal

The task is to count how many participants advance to the next round of a contest. We're given a list of scores, already sorted in non-increasing order. The rules for advancing are simple and strict:

1.  A participant's score must be **greater than or equal to** the score of the person in the **k-th place**.
2.  The participant's score must also be **positive** (greater than 0).

Our job is to read the scores and output the total number of people who satisfy both conditions.

-----

### The Analogy First: The High Jump Competition 🤸‍♀️

Imagine a high jump competition. The judges set the rules for who makes it to the final round.

1.  **Find the Cutoff Height:** First, they look at the performance of the **k-th place** jumper. Let's say `k=5` and the 5th best jumper cleared a height of `1.80 meters`. This height becomes the **official cutoff height**.

2.  **Count the Qualifiers:** Now, the judges review the entire list of athletes. For each athlete, they check two things:

      * Did they clear a height of at least `1.80m`?
      * Was their cleared height greater than `0m`?

Anyone who satisfies both conditions makes it to the final round. Our task is simply to count how many athletes that is.

-----

### The Optimal Approach (The "Aha\!" Moment)

The "High Jump" analogy is the most direct way to solve this. The logic is a straightforward two-step process:

1.  **Determine the threshold.** The score to beat is `scores[k-1]` (using 0-based indexing for an array).
2.  **Iterate and count.** Loop through the entire list of scores and count how many meet the criteria established in the rules.

Let's trace the first example: `n=8, k=5` and scores `[10, 9, 8, 7, 7, 7, 5, 5]`.

1.  **Find the Cutoff Score:** The `k=5`-th place person is at index `k-1 = 4`. The score at this position is **7**. This is our magic number.

2.  **Count the Qualifiers:** We check each score against the cutoff score of 7 and the positive score rule.

      * `10 >= 7` and `10 > 0`? Yes. (Count: 1)
      * `9 >= 7` and `9 > 0`? Yes. (Count: 2)
      * `8 >= 7` and `8 > 0`? Yes. (Count: 3)
      * `7 >= 7` and `7 > 0`? Yes. (Count: 4)
      * `7 >= 7` and `7 > 0`? Yes. (Count: 5)
      * `7 >= 7` and `7 > 0`? Yes. (Count: 6)
      * `5 >= 7`? No. Stop.

The final count of advancers is **6**.

-----

### Code Implementation

Here is a simple and efficient implementation in Python.

```python
def solve():
    """
    Solves the "Next Round" problem from Codeforces.
    """
    # Read n and k from the first line of input.
    n, k = map(int, input().split())
    
    # Read the list of scores from the second line.
    scores = list(map(int, input().split()))
    
    # --- The High Jump Analogy ---
    
    # 1. Find the Cutoff Score.
    # The k-th place finisher is at index k-1.
    cutoff_score = scores[k-1]
    
    # 2. Count the Qualifiers.
    advancers_count = 0
    for score in scores:
        # Check if the participant meets both conditions.
        if score >= cutoff_score and score > 0:
            advancers_count += 1
        else:
            # Since the list is sorted, we can stop early
            # once we find a score that doesn't qualify.
            break
            
    # Output the final count.
    print(advancers_count)

# It's common in competitive programming to call a main solve function.
solve()

```

-----

### Complexity Analysis

  * **Time Complexity:** $O(N)$
    We make a single pass through the list of `N` scores to count the qualifiers. The work is directly proportional to the number of participants.

  * **Space Complexity:** $O(N)$
    We need to store the `N` scores from the input in a list.

-----

### Final Check

This problem is a great example of carefully reading the rules and implementing them directly. The logic of finding a threshold and then counting is a common pattern. Does this approach make perfect sense?