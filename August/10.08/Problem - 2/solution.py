def cheapTravel():
    n,m,a,b = list(map(int, input().split()))
    mTripPerRound = m/b
    singleAllCost = n*a
    num_mTickets = n // m
    remainingRides = n % m
    costMixed = (num_mTickets * b) + (remainingRides * a)
    costAllSpecial = ((n // m) + 1) * b
    finalDecision = min(singleAllCost,costMixed,costAllSpecial)
    print(finalDecision)
cheapTravel()
