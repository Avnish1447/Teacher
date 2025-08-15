def solve():
    n = int(input())
    availableRoom = 0
    for _ in range(n):
        p,q = map(int, input().split())
        if q-p >=2:
            availableRoom += 1

    print(availableRoom)

solve()