def Presents():
    n = int(input())
    p = list(map(int,input().split()))
    gifters = [0]*n
    for i in range(n):
        giver = i +1
        receiver = p[i]
        gifters[receiver-1] = giver
    print(*gifters)

Presents()            