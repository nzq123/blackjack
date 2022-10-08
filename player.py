class Player:

    def __init__(self, name):
        self.name = name
        self.player_hand = []

    def __str__(self):
        return f'{self.player_hand}'

    def decision(self):
        print('Player hand is: ')
        for card in self.player_hand:
            print(card)
        self.hand()
        player_decision = input(f" 1 = Draw, 2 = Pass ")
        return player_decision

    def get_card(self, card):
        self.player_hand.append(card)

    def score(self):
        res = 0
        ace = False
        for card in self.player_hand:
            if card.rank == 'A':
                ace = True
            res += card.value
        if ace is True and res > 21:
            res -= 10
        return res

    def hand(self):
        num = self.score()
        print(f"Score is {num} ")

    def discard_hand(self):
        self.player_hand = []


class Dealer(Player):

    def __init__(self, name, deck):
        super().__init__(name)
        self.deck = deck

    def decision(self):
        print('Dealer hand is:')
        for card in self.player_hand:
            print(card)
        self.hand()
        while self.score() < 17:
            card = self.deck.draw_card(1)
            self.player_hand.extend(card)
            print(f'Dealer drawn {card[0]}')
            self.hand()
        return self.score()

    def draw_card(self):
        return self.deck.draw_card(1)[0]
