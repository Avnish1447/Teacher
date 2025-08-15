def RingRoad():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    currentLocation = 1
    totalTime = 0
    for destination in tasks:
        if destination >= currentLocation:
            totalTime += destination - currentLocation
        else:
            timeFromStart = destination
            timeToEnd = n - currentLocation
            totalTime += timeToEnd + timeFromStart
        currentLocation = destination            
    print(totalTime)    

RingRoad()