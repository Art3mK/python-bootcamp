import card
import random
from pprint import pprint


class Deck():
    def __init__(self):
        # 52 cards
        self.deck = []
        # clubs (♣), diamonds (♦), hearts (♥) and spades (♠)
        # ♧ clubs трефы (крести)
        # ♢ diamonds бубны
        # ♤ spades пики
        # ♡ hearts червы
        #
        for suit in ["clubs", "diamonds", "spades", "hearts"]:
            self.deck += [card.Card(suit=suit, rank=rank) for rank in range(2,11)]
            self.deck.append(card.Card(suit=suit, rank="jack"))
            self.deck.append(card.Card(suit=suit, rank="queen"))
            self.deck.append(card.Card(suit=suit, rank="king"))
            self.deck.append(card.Card(suit=suit, rank="ace"))
        random.shuffle(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def print_deck(self):
        pprint(self.deck)

    def pull_card(self):
        return self.deck.pop(0)
