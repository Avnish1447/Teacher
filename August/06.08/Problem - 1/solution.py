def Drink():
    OrangeContainingDrinks = int(input(""))
    OrangeJuiceVolumes = list(map(int, input().split()))
    SumOfOrangeJuiceVolume = 0
    for i in OrangeJuiceVolumes:
        SumOfOrangeJuiceVolume +=  i
    print(SumOfOrangeJuiceVolume/OrangeContainingDrinks)
        
Drink()    