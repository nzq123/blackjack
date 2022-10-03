from deck import Deck
from player import Player, Dealer


class Game:

    def play(self):

        deck = Deck()
        dealer = Dealer(deck.draw_card(2), deck)
        player = Player(deck.draw_card(2), deck)

        print('Player turn is starting')
        player.decision()
        print('Dealer turn is starting')
        dealer.decision()

        dealer_score = dealer.score()
        player_score = player.score()

        if player_score > 21:
            print(f'Player lost. He has more than 21 points ({player_score}).')
        elif dealer_score <= 21:
            if dealer_score > player_score:
                print(f'Dealer wins! with {dealer_score} points ')
            elif dealer_score == player_score:
                print(f'Draw with {player_score} points')
            else:
                print(f'Player wins! with {player_score} points')
        elif dealer_score > 21:
            print(f'Player wins with {player_score} points!')

