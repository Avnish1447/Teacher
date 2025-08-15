def museumNight():
    string = input()
    currentChar = 'a'
    totalRotations = 0

    for targetCharacter in string:
        startValue = (ord(currentChar))-(ord('a'))
        endValue = (ord(targetCharacter))-(ord('a'))
        directDis = abs(startValue-endValue)
        wrapDis = 26-directDis
        totalRotations = totalRotations + min(directDis,wrapDis)
        currentChar=targetCharacter

    print(totalRotations)

museumNight()        