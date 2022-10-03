from deck import Deck


class Player:

    def __init__(self, player_hand, deck):
        self.player_hand = player_hand
        self.deck = deck

    def __str__(self):
        return f'{self.player_hand}'

    def decision(self):
        player_decision = '1'
        while player_decision in {'1', '2'} and self.score() < 21:
            self.hand()
            player_decision = input(f" 1 = Draw, 2 = Pass ")
            if player_decision == '1':
                self.player_hand.extend(self.deck.draw_card(1))
                print(self.score())
            elif player_decision == '2':
                break
        return self.score()

    def count(self):
        res = 0
        for i in self.player_hand:
            res += i.value
        return res

    def hand(self):
        num = self.count()
        print(f"Score is: {num} ")

    def score(self):
        return self.count()


class Dealer(Player):

    def decision(self):
        self.hand()
        while self.score() < 17:
            print('Dealer is drawing a card')
            self.player_hand.extend(self.deck.draw_card(1))
            self.hand()
        return self.score()
