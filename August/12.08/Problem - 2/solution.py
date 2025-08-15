def toToast():
    n,k,l,c,d,p,nl,np = list(map(int, input().split()))
    mlToDrink = (k*l)//(n*nl)
    limeToToast = (c*d)//n
    saltToToast = p//(n*np)
    finalToast = min(mlToDrink,limeToToast,saltToToast)
    print(finalToast)

toToast()
    

