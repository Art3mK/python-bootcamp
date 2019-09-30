from deck import Deck

deck = Deck()
cards = []

cards.append(deck.pull_card())
cards.append(deck.pull_card())
cards.append(deck.pull_card())

def cards_value(*args):
    sum1 = 0
    sum11 = 0
    for card in args:
        print(card)
        sum1 += card.value()
        sum11 += card.value(ace11=True)
    print(f"sum1: {sum1}, sum11: {sum11}")

cards_value(*cards)
