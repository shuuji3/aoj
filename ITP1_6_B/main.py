n = int(input())
deck = []
for i in range(n):
    deck.append(input())

for suit in 'SHCD':
    for i in range(1, 14):
        card = f'{suit} {i}'
        if card not in deck:
            print(card)
