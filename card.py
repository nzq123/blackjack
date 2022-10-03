class Card:

    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return str(self)

