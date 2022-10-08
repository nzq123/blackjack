from game import Game
from deck import Deck
from player import Player, Dealer

deck = Deck()
dealer = Dealer('mati', deck)
player = Player('robo')

game_one = Game(dealer, player)
game_one.play()









