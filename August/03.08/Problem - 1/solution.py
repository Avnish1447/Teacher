def isLuckyNumber():
    num_str = input("")
    
    if not num_str:
        print(" ")
        return
    
    luckyDigitCount = 0
    isLucky = True
    for digit in num_str:
        if digit == '4' or digit == '7':
            luckyDigitCount += 1
        else:
            isLucky = False
            
    if (luckyDigitCount==4 or luckyDigitCount==7):
        print("YES")
    else:
        print("NO")

isLuckyNumber()