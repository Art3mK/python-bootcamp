from pprint import pprint

class Player():
    def __init__(self, name, card1, card2, bank, dealer=False):
        self.cards = [card1, card2]
        self.name = name
        self.bank = bank
        self.dealer = dealer
        self.score = self.__calculate_cards_value__()
        if (dealer):
            self.cards[0].secret = True

    def reset_cards(self, card1, card2):
        self.cards = [card1, card2]
        self.score = self.__calculate_cards_value__()

    def lose_bet(self, amount):
        self.bank -= amount

    def win_bet(self, amount):
        self.bank +=amount

    def can_place_bet(self,amount):
        if amount > self.bank:
            print("lol, you can't bet more than you have")
            return False
        return True

    def add_card(self, card):
        self.cards.append(card)
        self.score = self.__calculate_cards_value__()
        if self.score == 0:
            print(f"{self.name} busted!")

    def __calculate_cards_value__(self):
        """
        Calculates values for players cards
        Set value to 0, if hand is bust
        """
        score = 0
        aces = False
        # first treat all aces as 1 and track if any of the cards is ace
        # then if aces found -> try to return sum + 10 (as only one ace in hand could be 11)
        # if that is > thatn 21, try to return sum where all aces are 1
        # if that is > 21, then player is bust
        for card in self.cards:
            # first try to convert value to int
            try:
                score += int(card.rank)
            except ValueError:
                # card is some high rank card
                if card.rank in ['jack','queen','king']:
                    score += 10
                else:
                    # ace found
                    aces = True
                    score += 1
        if aces:
            if score+10 <= 21:
                return score+10
            elif score <= 21:
                return score
            else:
                return 0
        elif score <= 21:
            return score
        else:
            return 0

    def get_cards_value(self):
        return self.score

    def print_cards(self):
        print(f"{self.name} cards:")
        pprint(self.cards)
