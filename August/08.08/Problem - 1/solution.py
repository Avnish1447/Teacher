def HorseShoe():
    HorseShoeNumber = list(map(int, input().split()))
    UniqueColor = set(HorseShoeNumber)
    UniqueHorseShoe = len(UniqueColor)
    HorseShoesToBuy = 4 - UniqueHorseShoe
    print(HorseShoesToBuy)

HorseShoe()
