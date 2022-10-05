class Player:

    def __init__(self, player_hand, deck):
        self.player_hand = player_hand
        self.deck = deck

    def __str__(self):
        return f'{self.player_hand}'

    def decision(self):
        player_decision = '1'
        print('Player hand is: ')
        for card in self.player_hand:
            print(card)
        while player_decision in {'1', '2'} and self.score() < 21:
            self.hand()
            player_decision = input(f" 1 = Draw, 2 = Pass ")
            if player_decision == '1':
                card = self.deck.draw_card(1)
                self.player_hand.extend(card)
                print(f'Player drawn {card[0]}')
            elif player_decision == '2':
                break
        return self.score()

    def count(self):
        res = 0
        for card in self.player_hand:
            if card.rank == 'A' and res + card.value > 21:
                card.value = 1
            res += card.value
        return res

    def hand(self):
        num = self.count()
        print(f"Score is {num} ")

    def score(self):
        return self.count()

    def get_blackjack(self):
        if self.score() == 21 and len(self.player_hand) == 2:
            return True
        else:
            return False


class Dealer(Player):

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
