def wannaGuy():
    n = int(input())
    xLevels = list(map(int, input().split()))[1:]
    yLevels = list(map(int, input().split()))[1:]
    totalLevels = set(xLevels+yLevels)

    if n == len(totalLevels):
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

wannaGuy()