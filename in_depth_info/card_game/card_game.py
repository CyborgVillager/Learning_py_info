from enum import Enum
from enum import IntEnum
# Thanks in part to the card tutorial
# https://www.youtube.com/watch?v=62TmpPDs0mM @Cpt Jimmy Kirk

class Card(IntEnum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14



# aqiuire enum 4 playing cards
class Suit(Enum):
    Spades = 'spades'
    Clubs = 'clubs'
    Hearts = 'hearts'
    Diamonds = 'diamonds'


class Playing_Card:
    def __init__(self,card_value,card_suit):
        self.card_value = card_value
        self.card_suit = card_suit

