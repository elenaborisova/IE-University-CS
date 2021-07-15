import random


def main():
    ranks = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King')
    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

    random_card = (random.choice(ranks), random.choice(suits))

    print('The random card is:', random_card[0], random_card[1])


main()
