suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
rank = ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = {}

for i in suits:
    deck[i] = rank

print(deck)