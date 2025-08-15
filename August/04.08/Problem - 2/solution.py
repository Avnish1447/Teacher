def fixWordCase():
    LowerCase = 0
    UpperCase = 0
    word = input("")
    for alphabets in word:
        if alphabets.isupper():
            UpperCase += 1
        if alphabets.islower():
            LowerCase += 1
    if UpperCase > LowerCase:
        print(word.upper())    
    elif LowerCase>UpperCase or UpperCase == LowerCase:
        print(word.lower())

fixWordCase()

