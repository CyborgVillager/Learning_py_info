from enum import Enum
from enum import IntEnum
from random import *
# Thanks in part to the card tutorial
# https://www.youtube.com/watch?v=62TmpPDs0mM @Cpt Jimmy Kirk


full_deck = []
partial_deck_drawn = []

class Playing_Card:
    def __init__(self,card_value,card_suit):
        self.card_value = card_value
        self.card_suit = card_suit

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



# function to handle the full deck of cards
def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(Playing_Card(Card(card),Suit(suit)))
    return full_deck

# return single random card from the deck
def draw_cards(deck):
    random_card = randint(0,len(deck)-1)
    # removes the card from the deck using .pop
    return deck.pop(random_card)

'''''
Test if info is success
for index in range(0,len(full_deck)):
    print('Card: ' , full_deck[index].card_value)
    print('Suit: ' , full_deck[index].card_suit)

'''''