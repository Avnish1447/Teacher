def StonesOnTheTable():
    Stonenumber = int(input(""))
    Stonecolors = input("")
    stonesToRemove = 0

    for i in range (1,len(Stonecolors)):
        if Stonecolors[i] == Stonecolors[i-1]:
            stonesToRemove += 1
    print(stonesToRemove)

StonesOnTheTable()
