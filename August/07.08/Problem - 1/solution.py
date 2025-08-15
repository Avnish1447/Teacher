def DecodeDubstep():
    dubstepRemix = input()
    DubWord = "WUB"

    OriginalSong = dubstepRemix.split("WUB")
    OriginalPhrase = []
    for word in OriginalSong:
        if word:
            OriginalPhrase.append(word)
    DecodedSong = " ".join(OriginalPhrase)
    print(DecodedSong)
    

DecodeDubstep()