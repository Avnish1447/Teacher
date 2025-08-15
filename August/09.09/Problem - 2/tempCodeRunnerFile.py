def wannaGuy():
    n = int(input())
    xLevels = list(map(int, input().split()))[1:]
    yLevels = list(map(int, input().split()))[1:]
    totalLevels = xLevels+yLevels

    if n == totalLevels:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

wannaGuy()