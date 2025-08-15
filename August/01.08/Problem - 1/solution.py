def solve():
    n, k = map(int, input().split())
    
    scores = list(map(int, input().split()))
    
    cutoffScore = scores[k-1]
    advancersCount = 0
    for score in scores:
        if score >= cutoffScore and score > 0:
            advancersCount += 1
        else:
            break
            

    print(advancersCount)


solve()