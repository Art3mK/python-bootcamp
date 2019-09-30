from pprint import pprint

class Player():
    def __init__(self, name, card1, card2, bank, dealer=False):
        self.cards = [card1, card2]
        self.name = name
        self.bank = bank
        self.dealer = dealer
        self.calculate_cards_value()
        if (dealer):
            self.cards[0].secret = True

    def lose_bet(self, amount):
        self.bank -= amount

    def win_bet(self, amount):
        self.bank +=amount

    def place_bet(self,amount):
        if amount > self.bank:
            print("lol, you can't bet more than you have")
            return False
        return True

    def add_card(self, card):
        self.cards.append(card)
        self.calculate_cards_value()
        if self.is_busted():
            print(f"{self.name} busted!")

    def calculate_cards_value(self):
        sum1 = 0
        sum11 = 0
        for card in self.cards:
            sum1 += card.value()
            sum11 += card.value(ace11=True)
        self.sum1 = sum1
        self.sum11 = sum11

    def get_cards_value(self):
        if self.is_busted():
            return 42
        elif self.has_21():
            return 21
        elif self.sum11 > 21:
            return self.sum1
        else:
            return self.sum1 if 21 - self.sum1 < 21 - self.sum11 else self.sum11

    def print_cards(self):
        print(f"{self.name} cards:")
        pprint(self.cards)

    def is_busted(self):
        return True if self.sum1 > 21 else False

    def has_21(self):
        return True if self.sum1 == 21 or self.sum11 == 21 else False
