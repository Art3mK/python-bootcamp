from deck import Deck
from card import Card
from player import Player
deck = Deck()

player_name = input("How do I call you?: ")

human_player = Player(player_name, deck.pull_card(), deck.pull_card(), 200)
computer = Player("Computer", deck.pull_card(), deck.pull_card(), 1000000,True)

playing = True
hit = True
computer.print_cards()

while playing:
    bet = 0
    while True:
        bet = int(input(f"{human_player.name}, please place your bet (you have {human_player.bank}$): "))
        if human_player.place_bet(bet): break
    # Human player starts
    while hit:
        human_player.print_cards()
        if human_player.is_busted():
            playing = False
            break
        if human_player.has_21():
            break
        answer = ''
        while answer not in ('y','n'):
            answer = input(f"{human_player.name}, wanna hit? (y|n): ")
            if answer == 'y':
                human_player.add_card(deck.pull_card())
            else:
                hit = False
    if playing:
        computer.cards[0].secret = False
        # If player has a natural and the dealer does not, the dealer immediately pays that player one and a half times the amount of their bet


        while(computer.get_cards_value() < 17):
            computer.print_cards()
            computer.add_card(deck.pull_card())
        print("=========")
        computer.print_cards()
        print("=========")
        human_player.print_cards()
        if computer.is_busted() or human_player.get_cards_value() > computer.get_cards_value():
            print("Player wins!")
        elif (human_player.has_21() and computer.has_21()) or human_player.get_cards_value() == computer.get_cards_value():
            print("Nobody wins!")
        else:
            print("Computer wins!")
        pass
    else:
        print(f"{computer.name} won!")
    break

def cards_value(*args):
    sum1 = 0
    sum11 = 0
    for card in args:
        print(card)
        sum1 += card.value()
        sum11 += card.value(ace11=True)
    print(f"sum1: {sum1}, sum11: {sum11}")
