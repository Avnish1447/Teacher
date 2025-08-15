import math
def needLantern():
    n,m = map(int, input().split())
    totalSquares = n*m
    lanternNeeded = int(math.ceil(totalSquares/2.0))

    print(lanternNeeded)

t = int(input())
for _ in range(t):
    needLantern()