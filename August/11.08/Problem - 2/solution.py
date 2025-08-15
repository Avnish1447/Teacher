def CapitalizeEachWord():
    word = input()
    firstChar = word[0].upper()
    restChar = word[1:]
    character = firstChar+restChar
    print(character)
CapitalizeEachWord()