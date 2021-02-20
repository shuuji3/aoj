while True:
    deck = input()
    if deck == '-':
        break
    shuffle = int(input())
    for i in range(shuffle):
        n = int(input())
        bottom = deck[:n]
        top = deck[n:]
        deck = top + bottom
    print(deck)
