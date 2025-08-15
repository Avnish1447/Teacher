def MaxCard():
    n = int(input())
    CardDeck = list(map(int, input().split()))
    serenaDeck = []
    dimaDeck = []

    for i in range(n):
        if i%2 == 0:
            if CardDeck[0] > CardDeck[-1]:
                serenaDeck.append(CardDeck[0])
                CardDeck.pop(0)
            else:
                serenaDeck.append(CardDeck[-1])
                CardDeck.pop(-1)
        else:
            if CardDeck[0] > CardDeck[-1]:
                dimaDeck.append(CardDeck[0])
                CardDeck.pop(0)
            else:
                dimaDeck.append(CardDeck[-1])
                CardDeck.pop(-1)
    print(sum(serenaDeck),sum(dimaDeck))


MaxCard()