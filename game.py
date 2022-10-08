from deck import Deck
from player import Player, Dealer


class Game:

    def __init__(self, dealer, player):
        self.dealer = dealer
        self.player = player

    def play(self):

        player_points = 0
        dealer_points = 0
        rounds = 1

        dealer = self.dealer
        player = self.player

        while player_points < 3 and dealer_points < 3:

            dealer.get_card(dealer.draw_card())
            dealer.get_card(dealer.draw_card())
            player.get_card(dealer.draw_card())
            player.get_card(dealer.draw_card())

            print(f'***** Round {rounds}: Player {player_points} points, Dealer {dealer_points} points *****')
            rounds += 1
            print(f'Dealers first card is {dealer.player_hand[0]}')
            self.ask_player(player)
            if self.has_blackjack(player) is False:
                self.ask_player(dealer)
            else:
                print('Player got blackjack!')

            dealer_score = dealer.score()
            player_score = player.score()

            if player_score > 21:
                print(f'Player lost. He has more than 21 points ({player_score}).')
                dealer_points += 1
            elif self.has_blackjack(player) and self.has_blackjack(dealer):
                print('Dealer hand is:')
                for card in dealer.player_hand:
                    print(card)
                print(f'Both got blackjack wow')
                player_points += 1
                dealer_points += 1
            elif self.has_blackjack(player) and self.has_blackjack(dealer) is False:
                print('Player wins by black jack !')
                player_points += 1
            elif dealer_score <= 21:
                if self.has_blackjack(dealer) and self.has_blackjack(player) is False:
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

            player.discard_hand()
            dealer.discard_hand()

    def has_blackjack(self, player):
        if player.score() == 21 and len(player.player_hand) == 2:
            return True
        else:
            return False

    def ask_player(self, player):
        while player.score() < 21:
            decision = player.decision()
            if decision == '1':
                player.get_card(self.dealer.draw_card())
            else:
                break



