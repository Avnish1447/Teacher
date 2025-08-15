def UserInput():
    wordList = []
    noOfWords = int(input(""))
    if noOfWords > 0:
        print("")
    else:
        print("")
    
    for i in range(noOfWords):
        word = input("")
        wordList.append(word)
    return wordList

def WayTooLongWords(wordList):
    abbreviation = []
    for word in wordList:
        if len(word)>10:
            firstChar = word[0]
            lastChar = word[-1]
            middleChar = len(word)-2
            short = f"{firstChar}{middleChar}{lastChar}"
            abbreviation.append(short)
        else:
            abbreviation.append(word)
    return abbreviation 

myWords = UserInput()
shortWords = WayTooLongWords(myWords)
for item in shortWords:
    print(item)
