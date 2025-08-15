def bitOPERATION():
    noOfOperations = int(input())
    x = 0
    for f in range(noOfOperations):
        operation = input()
        if '+' in operation:
             x += 1
        if '-' in operation:
             x -= 1
    print(x)    

bitOPERATION()