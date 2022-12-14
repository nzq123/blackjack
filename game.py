from deck import Deck
from player import Player, Dealer


class Game:

    def play(self):

        player_points = 0
        dealer_points = 0
        rounds = 1

        while player_points <= 3 or dealer_points <= 3:

            deck = Deck()
            dealer = Dealer(deck.draw_card(2), deck)
            player = Player(deck.draw_card(2), deck)

            print(f'***** Round {rounds}: Player {player_points} points, Dealer {dealer_points} points *****')
            rounds += 1
            print(f'Dealers first card is {dealer.player_hand[0]}')
            player.decision()
            if player.get_blackjack() is False:
                dealer.decision()
            else:
                print('Player got blackjack!')

            dealer_score = dealer.score()
            player_score = player.score()

            if player_score > 21:
                print(f'Player lost. He has more than 21 points ({player_score}).')
                dealer_points += 1
            elif player.get_blackjack() and dealer.get_blackjack():
                print('Dealer hand is:')
                for card in dealer.player_hand:
                    print(card)
                print(f'Both got blackjack wow')
                player_points += 1
                dealer_points += 1
            elif player.get_blackjack() and dealer.get_blackjack() is False:
                print('Player wins by black jack !')
                player_points += 1
            elif dealer_score <= 21:
                if dealer.get_blackjack() and player.get_blackjack() is False:
                    print('Dealer wins by black jack !')
                    dealer_points += 1
                elif dealer_score > player_score:
                    print(f'Dealer wins! with {dealer_score} points ')
                    dealer_points += 1
                elif dealer_score == player_score:
                    print(f'Draw with {player_score} points')
                else:
                    print(f'Player wins! with {player_score} points')
                    player_points += 1
            elif dealer_score > 21:
                print(f'Player wins with {player_score} points!')
                player_points += 1




