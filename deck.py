import random
from card import Card


class Deck:

    def __init__(self):
        self.card_list = []
        self.create_deck()
        self.shuffle()

    def __str__(self):
        return f'{self.card_list}'

    def create_deck(self):
        '''creating a new deck'''
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

        ranks = [
            {'rank': 'A', 'value': 11},
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7},
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10}
        ]

        for i in ranks:
            for j in suits:
                card = Card(i['rank'], i['value'], j)
                self.card_list.append(card)

    def shuffle(self):
        random.shuffle(self.card_list)

    def draw_card(self, number):
        dealt_cards = []
        for i in range(number):
            dealt_cards.append(self.card_list.pop())
        return dealt_cards


a = Deck()

a.shuffle()

# print(a.draw_card(2))

