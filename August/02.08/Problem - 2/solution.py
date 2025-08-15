def Team():
    try:
        numQuestions = int(input())
        
        allViews = [[int(s) for s in input().split()] for _ in range(numQuestions)]

    except (ValueError, IndexError):
        print("Invalid input format.")

    solvable = 0

    for count in allViews:
        if sum(count)>=2:
            solvable = solvable + 1
    return solvable

questionSolve = Team()
print(questionSolve)
